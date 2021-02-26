import unittest
import importlib.util
import subversion_helperOLD as svn

def main():
#     svn.start(16)
    t = StandardTester('Session16_Test2_201430', 'm4',
                        file_with_tests='m4b_tests.py')
    results = t.run()
    print_results(results)

def print_results(results):
    for result in results:
        if result.wasSuccessful():
            print('{:8}: OK'.format(result.student))
        else:
            print('{:8} ERRORS: {}'.format(result.student,
                                             result.errors))
            print('{:8} FAILURES: {}'.format(result.student,
                                             result.failures))
            for subtest in result.subtest_results:
                if subtest[0] == 'PASSED_TEST':
                    continue
                print('{:8} FAILED {:9}: {}'.format(result.student,
                                                    subtest[2][0],
                                                    subtest))

class Tester():
    """ Base class for testing student code. """

    def __init__(self, project, module_name=None, students=None):
        if type(project) is int:
            self.project_name = self.get_project_name(project)
        else:
            self.project_name = project

        if not module_name:
            self.module_name = 'm1'  # FIXME
            # FIXME, make a list of ALL non-e modules in project
        else:
            self.module_name = module_name  # FIXME: eventually a list

        if not students:
            self.students_to_test = svn.get_usernames_from_rosters()
        else:
            self.students_to_test = students

        # FIXME: Get next few from DATA.
        self.solution = svn.get_grading_folder(svn.SOLUTION_USERNAME,
                                                self.project_name)

    def get_project_name(self, project):
        # FIXME.
        return 'Session16_Test2_201430'

    def initialize_tests(self):
        # Override in subclass.
        pass

    def run(self):
        self.initialize_tests()
        results = []
        for student in self.students_to_test:
            print()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('TESTING:', student)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            result = self.run_test(student)
            result.student = student  # Extend on the fly
            results.append(result)

        return results

    def run_test(self, student):
        # Override in subclass.
        pass


class StandardTester(Tester):

    def __init__(self, project, module_name=None, students=None,
                 file_with_tests=None):
        super().__init__(project, module_name, students)

        self.students_to_test.append(svn.SOLUTION_USERNAME)

        # FIXME
        src = '/src/'
        if file_with_tests:
            tail = file_with_tests
        else:
            suffix = '_tests.py'
            tail = self.module_name + suffix
        self.file_with_tests = self.solution + src + tail

    def read_tests(self):
        f = open(self.file_with_tests, 'r')
        tests = []
        parity = 0
        for line in f:
            if not line or line[0] == '\n':
                parity = 0
                continue
            elif line[0] == '#':
                function_to_test = line.split()[2]
                parity = 0
            elif parity == 0:
                arguments = eval(line.strip())
                arguments_after_call = eval(line.strip())
                parity = 1
            elif parity == 1:
                correct_result = eval(line.strip())
                quad = [function_to_test, arguments, correct_result,
                        arguments_after_call]
                tests.append(quad)
                parity = 2
            else:
                mutated_arguments = eval(line.strip())
                tests[len(tests) - 1][3] = mutated_arguments
                parity = 0
        f.close()

        return tests

    def run_test(self, student):
        # TODO: Need to deal with inability to load, can't read tests, etc.
        tests = self.read_tests()
        folder = svn.get_grading_folder(student, self.project_name)

        src = '/src/'
        suffix = '.py'
        file_location = folder + src + self.module_name + suffix

        # Critical: The module_for_student must be a UNIQUE name.
        # If it is re-used during this Python execution, then the
        # definitions are combined. So if a student does not define
        # some function, the definition from the previous student
        # is used.
        module_for_student = self.module_name + '_' + student

        spec = importlib.util.spec_from_file_location(module_for_student,
                                                      file_location)

        module = spec.loader.load_module(module_for_student)

        test = StandardTest(tests, module)
        result = test.run()
        result.subtest_results = test.subtest_results  # Extend on the fly
        return result


class StandardTest(unittest.TestCase):
    """
    A subclass of unittest.TestCase that:
      -- Has a set of tests in a standard form:
      -- Has a module (the module itself, NOT just its name)
    and:
      -- Runs the set of tests on the module, as subtests.

    Runs a given set of tests (arguments/result) on a given module. """

    def __init__(self, tests, module):
        self.subtests = tests
        self.module = module
        super().__init__('runSubTestsOnModule')

        self.subtest_results = []

    def runSubTestsOnModule(self):
        for test in self.subtests:
            with self.subTest():
                error = ''  # so far
                try:
                    function = getattr(self.module, test[0])
                except Exception as exception:
                    # FIXME: These should be ENUMSs.
                    error = 'FUNCTION_NOT_IMPLEMENTED'
                    message = 'Function {} is not implemented'
                    triple = (error, message.format(test[0]), test)
                    self.subtest_results.append(triple)
                    raise exception
                try:
                    result = function(*test[1])
                except Exception as exception:
                    error = 'THROWS_EXCEPTION'
                    message = 'Function {} throws an exception: {}'
                    triple = (error,
                              message.format(test[0], exception), test)
                    self.subtest_results.append(triple)
                    raise exception
                try:
                    self.assertEqual(result, test[2],
                                     'Wrong returned value')
                except Exception as exception:
                    error = error + 'WRONG_RETURNED_VALUE'
                    message = 'Expected: {}. Got: {}.'
                    message = message.format(test[2], result)
                try:
                    self.assertEqual(test[1], test[3], 'Wrong mutation')
                except Exception as exception:
                    if error:
                        error = error + ' and BAD_MUTATION'
                        message = message + ' '
                    else:
                        error = error + 'BAD_MUTATION'
                        message = ''
                    message2 = 'Expected arguments to be: {}\nGot: {}'
                    message2 = message2.format(test[3], test[1])
                    message = message + message2
                if not error:
                    error = 'PASSED_TEST'
                    message = 'OK'
                triple = (error, message, test)
                self.subtest_results.append(triple)
                if error != 'PASSED_TEST':
                    raise exception

class TesterTest(unittest.TestCase):
    """
    A subclass of unittest.TestCase for testing whether a TESTING
    function calls the function to be tested enough times.
    For example, it might test whether  test_blah() calls blah(...)
    at least 4 times (for 4 tests).
    A TesterTest:
      -- Has a module (NOT name of moudule -- the module itself)
      -- Has the name X of a function in that module
      -- Has a positive integer N
    and
      -- Runs test_X() [where X is the name of the function]
           (and catches and ignores any exception)
      -- Counts how many times X is called
    The test passes if that count >= N.  Else the test fails.
    """

    def __init__(self, module, name_of_test_function,
                 name_of_function_it_tests, min_number_of_tests):
        self.module = module
        self.name_of_test_function = name_of_test_function
        self.name_of_function_it_tests = name_of_function_it_tests
        self.min_number_of_tests = min_number_of_tests
        super().__init__('runTestsOnModule')

#         self.number_of_calls = 0
#         test_function_name = 'test_' + self.function_name
#         try:
#             test_function = getattr(self.module, test_function_name)
#
#         except:
#             message = 'Function {} is not implemented'
#             self.fail(message.format(test_function_name))
#             return


#     def runTestsOnModule(self):
#         number_of_calls = 0
#
#         # If the test_function or the function it tests does not exist,
#         # fail immediately.
#         try:
#             test_function = getattr(self.module,
#                                     self.name_of_test_function)
#         except:
#             message = 'Function {} is not implemented'
#             self.fail(message.format(test[0]))
#
#             function_it_tests = getattr(self.module,
#                                     self.name_of_function_it_tests)
#         # Redefine the function the test_function tests
#         # to include a counter.
#
#         # Call the test_function, catching and ignoring any exceptions.
#
#         # Test passes if number_of_calls >= min_number_of_tests
#
#         def count_calls(function_name, ):
#             self.number_of_calls = self.number_of_calls + 1
#             try:
#
#
#                 message = 'Function {} is not implemented'
#             self.fail(message.format(test_function_name))
#             return
#
#
#
#             with self.subTest(i=test):
#                 try:
#                     function = getattr(self.module, test[0])
#                 except:
#                     message = 'Function {} is not implemented'
#                     self.fail(message.format(test[0]))
#                     continue
#                 try:
#                     result = function(*test[1])
#                 except Exception as e:
#                     message = 'Function {} throws an exception: {}'
#                     self.fail(message.format(test[0], e))
#                     continue
#                 self.assertEqual(result, test[2], 'Wrong returned value')
#                 self.assertEqual(test[1], test[3], 'Wrong mutation')

# Test more carefully:
#   1. Catches inadvertant mutations?
#   2. Are the catches for not-implemented and throws-exception correct?

def test_decorator():
    import m1
    old = m1.foo
    def bar():
        print('bar')
        old()
    m1.foo = bar
    m1.foo()

if __name__ == '__main__':
#     test_decorator()
    main()

#     project = 'Session16_Test2_201430_mutchler'
#     src = 'src/'
#     module = 'm1'
#     suffix = '.py'
#     t = UnitTester(project, module)
#     print(t.tests)
#     result = t.run_tests()
#     print(result)
#     path = folder + session + src + module + suffix
#     t = StandardTest('m1', 'm1_tests.py')
#     print(t.read_tests())
#     result = t.run()
#     print(result)
#     print(result.failures[0])
#     t = StandardTest('m1a', 'foo')
#     result = t.run()
#     print(result)
#     print(result.errors)
#     m5 = importlib.import_module('m5')
#     m5.foo()
#   FAILS:
#     m = importlib.import_module('C:\\EclipseWorkspaces\\csse120\\Session16_Test2_201430_SOLUTION\\src\\m5.py')
#     m.foo()

#     folder = 'C:/EclipseWorkspaces/csse120/'
#     session = 'Session16_Test2_201430_mutchler/'
#     src = 'src/'
#     module = 'm6'
#     suffix = '.py'
#     path = folder + session + src + module + suffix
#     spec = importlib.util.spec_from_file_location(module, path)
#     print(spec.loader)
#     m = spec.loader.load_module(module)
#     m.foo()
#
#     module = 'm7'
#     suffix = '.py'
#     path = folder + session + src + module + suffix
#     spec = importlib.util.spec_from_file_location('m6', path)
#     print(spec.loader)
#     m = spec.loader.load_module('m6')
#     m.foo()



# importlib.util.spec_from_file_location(name, location, *, loader=None, submodule_search_locations=None)

        # FIXME: The next two change from term to term. Unify with Grader.
#         self.root_folder = 'C:/EclipseWorkspaces/csse120-grading'
#         self.term = '201430'
#         self.grading_folder = self.root_folder + '/' + self.term + '/'
#         self.folder_to_grade = self.grading_folder + self.project + '/'
#
#         print(self.folder_to_grade)
        # Where the tests are:



#         project = 'Session16_Test2_201430_SOLUTION/'  # FIXME
#         prefix = folder1 + project + src
#         suffix_for_tests = '_tests.py'
#         self.file_with_tests = prefix + self.module_name + suffix_for_tests
#         self.tests = self.read_tests()

        # Where the student modules are:
