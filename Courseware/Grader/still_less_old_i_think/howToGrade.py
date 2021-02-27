# FIXME: This file needs to be reworked!!!!!!!!!
# TODO: This file needs to be commented.

import lines_of_code
import abc
import importlib.util
import unittest
# import importlib.machinery
import time
import os
import sys

########################################################################
# Base classes: Tester and TesterResultForStudent.
########################################################################
class Tester():
    """ Abstract base class for testing student code. """

    def __init__(self, what_to_grade, who_to_grade, repo_helper):
        """
        Tests the given  what_to_grade  for the students specified by the given
        who_to_grade, given the  repo_helper  who checked out the projects.
          type: what_to_grade: WhatToGrade
          type: who_to_grade:  WhoToGrade
          type: repo_helper:   RepoHelper
        """
        self.what_to_grade = what_to_grade
        self.who_to_grade = who_to_grade
        self.repo_helper = repo_helper
        self.where_to_grade = repo_helper.get_grading_folder()

        self.results = {}
        self.students_who_failed_tests = []
        self.students_who_passed_all_tests = []

    @abc.abstractmethod
    def do_tests_on_student(self, student):
        """
        Does this Tester's tests on this Tester's  what_to_grade
        for the given student, using this Tester's  repo_helper
        as needed.  Returns a TesterResultForStudent.
          :rtype TesterResultForStudent
        """

    def do_tests(self):
        """
        Does this Tester's tests on this Tester's  what_to_grade
        for ALL of the students specified by its  who_to_grade,
        using its  repoHelper   as needed.
        Prints appropriate messages in doing so.

        Returns a dictionary of  TesterResultForStudent  objects
        whose keys are the students.
          :rtype dict(str)
        """
        self.setup_before_tests()

        for student in self.who_to_grade.students:
            self.do_before_testing(student)
            result = self.do_tests_on_student(student)
            self.do_after_testing(student, result)

        self.teardown_after_tests()

        return self.results

    def setup_before_tests(self):
        """
        Called (once) by  do_tests  BEFORE doing tests on all the students.
        """
        pass

    def teardown_after_tests(self):
        """
        Called (once) by  do_tests  AFTER doing tests on all the students.
        """
        self.print_results()

    def do_before_testing(self, student):
        self.show_message_beginning_test(student)

    def do_after_testing(self, student, result):
        if result.passed_test():
            self.students_who_passed_all_tests.append(student)
        else:
            self.students_who_failed_tests.append(student)
        self.results[student] = result

    def show_message_beginning_test(self, student):
        # CONSIDER: Have options to limit the console output? Default template?
        print()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('TESTING:', student)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    def print_results(self):
        print()

        passed = self.students_who_passed_all_tests
        failed = self.students_who_failed_tests
        all = self.who_to_grade.students

        print('Students who PASSED all tests:', end='')
        if len(passed) == len(all):
            print(' ALL')
        else:
            print()
            for student in passed:
                print('  {}'.format(student))

        print()
        print('Students who FAILED tests:', end='')
        if len(failed) == 0:
            print(' NONE')
        else:
            print()
            for student in failed:
                print('  {}'.format(student))


class TesterResultForStudent(object):

    def __init__(self, student, what_was_tested, result):
        """
        Stores the result from running a Tester's tests on its  WhatToGrade
        for a single student.  The actual result can be of any type
        (as determined by the subclass of Tester that is being used).
          :type student:          str
          :type what_was_tested:  WhatToGrade
          :type result            object
        """
        self.student = student
        self.what_was_tested = what_was_tested
        self.result = result

    def __repr__(self):
        return '({}, {})'.format(self.student, self.result)

    def passed_test(self):
        return self.result.wasSuccessful()


########################################################################
# Concrete implementations of Tester:
#   UnitTester, CommitsTester, ...
########################################################################
class UnitTestTester(Tester):
    """
    Tests a given module by running a unittest.TestCase that tests the module.
    """
    DEFAULT_UNITTEST_FOLDER = 'SOLUTION/src/'
    DEAULT_UNITTEST_PREFIX = 'test_'

    def __init__(self, what_to_grade, who_to_grade, repo_helper,
                 testcase=None, module_with_testcases=None, is_silent=True,
                 runner=None):
        """
        Tests the given  what_to_grade  for the students specified by the given
        who_to_grade, given the  repo_helper  who checked out the projects.

        Does so by running a specified unittest.TestCase.

          type: what_to_grade: WhatToGrade
          type: who_to_grade:  WhoToGrade
          type: repo_helper:   RepoHelper
          type: testcase_or_module_with_testcase: unittest.TestCase
        """
        super().__init__(what_to_grade, who_to_grade, repo_helper)
        assert(module_with_testcases == None)  # cuz not implemented yet

        self.testcase = testcase or module_with_testcases
        self.is_silent = is_silent
        self.runner = runner or SilentTextTestRunner

    def make_testcase(self, module_with_testcase):
        pass
#         self.pathname_of_module_with_unittests = pathname_of_module_with_unittests
#         if not self.pathname_of_module_with_unittests:
#             pathname = (self.where_to_grade
#                       + UnitTestTester.DEFAULT_UNITTEST_FOLDER
#                       + UnitTestTester.DEAULT_UNITTEST_PREFIX
#                       + self.what_to_grade.module)
#             self.pathname_of_module_with_unittests = pathname


#         pathname = (unit_tests_pathanme or
#                     UnitTestTester.DEFAULT_UNITTEST_FOLDER.replace(BLAH,
#                                                                    self.what_to_grade)
#
#             or self.where_to_grade)

#     def setup_before_tests(self):
#         if self.is_silent:
#             self.old_stderr = sys.stderr
#             sys.stderr = open(os.devnull, 'w')
#
#     def teardown_after_tests(self):
#         if self.is_silent:
#             print("SILENT")
#             sys.stderr = self.old_stderr

    def do_tests_on_student(self, student):
        result = self.runner().run(self.testcase)
        return TesterResultForStudent(student, self.what_to_grade, result)

#         self.load_module(student)

    def load_module(self, student):
        folder = self.repo_helper.get_grading_folder(student)
        print(folder)
        # FIXME: this hard-codes the module name.
        module_name = 'problem1'
        module_file_path = folder + '/src/' + module_name + '.py'
        module_spec = importlib.util.spec_from_file_location(
            module_name, module_file_path)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        print(dir(module))
        getattr(module, 'test_problem1a')()


class SilentTextTestRunner(unittest.TextTestRunner):
    """ A TextTestRunner with less displayed when running a test. """

    def __init__(self):
        super().__init__(stream=open(os.devnull, 'w'))

    def run(self, test):
        result = super().run(test)

        # TODO: Allow variations on how much to display.
        if not result.wasSuccessful():
            sys.stdout.flush()
            time.sleep(1)  # Time for the flush to finish
            print('FAILED TEST!', file=sys.stderr)

        return result


class CommitsTester(UnitTestTester):
    """ Tests a by how much the student has COMMITTED the module. """

    def __init__(self, what_to_grade, who_to_grade, repo_helper,
                 commits_required=2):
        """
        Tests the given  what_to_grade  for the students specified by the given
        who_to_grade, given the  repo_helper  who checked out the projects.

        Does so by running a unittest.TestCase that returns SUCCESS if the
        student has made at least the given number of commits on the module.

          type: what_to_grade: WhatToGrade
          type: who_to_grade:  WhoToGrade
          type: repo_helper:   RepoHelper
          type: commits_required:  int
        """
        super().__init__(what_to_grade, who_to_grade, repo_helper)
        self.commits_required = commits_required

    def do_tests_on_student(self, student):
        """
          :rtype UnittestTesterResult
        """
        repo_helper = self.repo_helper
        commits_required = self.commits_required

        class TestCase(unittest.TestCase):
            def runTest(self):
                commits = repo_helper.get_number_of_commits(student)
                print('Commits by {:8}: {:2}'.format(student, commits))
                self.assertGreaterEqual(commits, commits_required)

        self.testcase = TestCase()
        return super().do_tests_on_student(student)


class ChangesTester(UnitTestTester):
    """
    Tests by examining how much (if at all) each module has changed
    since the student received it.
    """

    def __init__(self, what_to_grade, who_to_grade, where_to_grade):
        """
        Tests the given  what_to_grade  for the students specified
        by the given  who_to_grade, given that checked-out projects
        are in the given  where_to_grade  folder.

        Tests by examining how much (if at all) each module has changed
        since the student received it.

        type: what_to_grade: WWhaToGrade
        type: who_to_grade:  WhoToGrade
        type: where_to_grade: str
        """
        super().__init__(what_to_grade, who_to_grade, where_to_grade)

        # The following are set by  setup_before_tests
        #   (which is called by  do_tests).
        self.stats_for_original = None
        self.stats_for_solution = None

    def setup_before_tests(self):
        """
        For each module to be tested, get and store the statistics
        for the original and solution versions of the module.
        """
        original = self.what_to_grade.course.username_for_original
        self.stats_for_original = self.get_stats(original)

        solution = self.what_to_grade.course.username_for_solution
        self.stats_for_solution = self.get_stats(solution)

    def get_stats(self, student):
        """
        Returns ...
        """
        # TODO: Complete the above comment.

        # FIXME: The folder structure in the following statement
        # should come from elsewhere.  Right now it is both here
        # and in RepoHelper, and it is specific to projects
        # as we set them up for Eclipse in 120.

        folder = self.where_to_grade + student + '/src/'

        result = {}
        for module in self.what_to_grade.modules:
            filename = folder + module

            # CONSIDER: Move  lines_of_code  stuff to this class?
            stats = lines_of_code.evaluate_module(filename)
            result[module] = stats

        return result

    def run_tests(self, student):
        """
        """
        # TODO: Augment the above comment.

        stats = self.get_stats(student)  # stats for ALL modules
        result = ChangesTesterResult()
        vs_original = {}
        vs_solution = {}
        for module in self.what_to_grade.modules:
            original = self.stats_for_original[module]
            solution = self.stats_for_solution[module]
            vs_original[module] = stats[module].minus(original)
            vs_solution[module] = stats[module].minus(solution)

        result.stats = stats
        result.vs_original = vs_original
        result.vs_solution = vs_solution

        return result


class ChangesTesterResult(TesterResultForStudent):
    """
    The result of running a test on a student.  Includes:
      -- student tested
      -- what was tested (a ThingToGrade)
      -- for each module that was tested:
           -- The StatisticsForModule for that module
    """

    def __init__(self, student=None, what_was_tested=None,
                 stats=None, vs_original=None, vs_solution=None):
        """
        :type student: str
        :type what_was_tested: ThingToGrade
        :type stats: dict(str, StatisticsForModule)
        :type vs_original: dict(str, StatisticsForModule)
        :type vs_solution: dict(str, StatisticsForModule)
        """
        # TODO: Augment the above comment.

        # CONSIDER: The names for the fields of this class
        # are poorly chosen, maybe.

        super().__init__(student, what_was_tested)

        self.stats = stats
        self.vs_original = vs_original
        self.vs_solution = vs_solution

    # CONSIDER: repr and str below are provided to display results.
    # But what we really need is to STORE and/or LOG results.
    # The following will eventually need to change, I suspect.

    def __repr__(self):
        format_string = 'ChangesTesterResult({}, {}, {!r}, {!r}, {!r}'
        return format_string.format(self.student,
                                    self.what_was_tested,
                                    self.stats,
                                    self.vs_original,
                                    self.vs_solution)

    def __str__(self):
        line1 = 'Student: {}\n'.format(self.student)
        line2 = 'What was tested: {}\n'.format(self.what_was_tested)

        module_limit = 11  # Chop module names at this many characters.

        format_string = '{:' + str(module_limit) + '}'
        format_string += ' {:>14} {:>15} {:>15} {:>15}\n'
        header = ('Module', 'Removed',
                  'vs. Original', 'vs. Solution', 'Module itself')
        line3 = format_string.format(*header)

        result = line1 + line2 + line3
        modules = sorted(self.stats.keys())
        for module in modules:
            result += self.result_for_module(module,
                                             format_string,
                                             module_limit)

        return result

    def result_for_module(self, module, format_string, module_limit):
        """
        Returns a string representation for the given module
        in this ChangesTesterResult.
        """
        # TODO: Augment the above comment

        # CONSIDER: The following is based on things in
        # StatisticsForModule that could later change
        # (and be missed here).  Encapsulate it all in a single place.

        transformations = ('nothing_removed',
                           'wo_blank_lines',
                           'wo_docstrings',
                           'wo_comments')
        labels = ('Nothing',
                  'Blank lines',
                  ' + docstrings',
                  ' + comments')
        result = ''
        for k in range(len(transformations)):
            transformation = transformations[k]
            label = labels[k]
            vs_original = getattr(self.vs_original[module],
                                  transformation)
            vs_solution = getattr(self.vs_solution[module],
                                  transformation)
            stats = getattr(self.stats[module],
                            transformation)

            trio = (vs_original, vs_solution, stats)
            stat = []
            for k in range(len(trio)):
                stat.append(' {:3} {:4} {:5}'.format(trio[k].lines,
                                                     trio[k].words,
                                                     trio[k].characters))

            if transformation == 'nothing_removed':
                module_name = module[:module_limit]
            else:
                module_name = ''

            result += format_string.format(module_name, label, *stat)
        return result

# ----------------------------------------------------------------------
# Stuff below here is good stuff (mostly) but needs to be reworked.
# ----------------------------------------------------------------------


class ReturnedValueTester(Tester):
    """
    Tests functions in modules by, for each function to be tested,
    determining whether the function returns the correct value
    and has (only) the correct side effects.

    More precisely, a ReturnedValueTester does the following for
    each module that it tests:
      1. Reads (from a file) a collection of Tests, where a Test is:
           -- The name of the function to call.
           -- The arguments to send to the function in that Test.
           -- The correct returned value,
                and the correct side effects (if any),
                from calling the function with those arguments.

      2. For each student to be tested:
           -- Loads the student's module.
           -- Applies each Test to that student's module.
           -- Records whether or not the student's code returned
                the correct value and had the correct side effects.
           -- Also records the nature of the failure for failed tests.
    """

    def __init__(self, what_to_grade, who_to_grade, where_to_grade):
        """
        Tests the given  what_to_grade  for the students specified
        by the given  who_to_grade, given that checked-out projects
        are in the given  where_to_grade  folder.

        type: what_to_grade: FunctionToGrade
        type: who_to_grade: WhoToGrade
        type: where_to_grade: str
        """
        super().__init__(what_to_grade, who_to_grade, where_to_grade)

        # The following are set by  setup_before_tests
        #   (which is called by  do_tests).
        self.tests = None

    def setup_before_tests(self):
        """
        """
        self.tests = {}
        for module in self.what_to_grade.modules:
            filename = self.get_filename_with_tests(module)
            with open(filename, 'r') as f:
                test_text = f.read()
            self.tests[module] = self.parse_test_text(test_text)

    def get_filename_with_tests(self, module_name):
        # FIXME: Hard-coding this for now.
        return "tests.txt"

        suffix = self.what_to_grade.course.suffix_for_test_files
        tail = module_name.split('.')[0] + suffix + '.py'

        head = self.where_to_grade
        head += self.what_to_grade.course.username_for_solution
        head += '/src/'

        return head + tail

    def parse_test_text(self, test_text):
        """
        For each module to be tested, reads the tests to be applied
        to that module from a text file like this example:
           @ m2 problem2a
           [[4, 66, 9, -2, 55, 0], [7, 22, 5, 10, -5, 9]]
           [11, 88, 14, 8, 50, 9]

           [[], []]
           []

           [[-1, 0, 1], [1, 0, -1]]
           [0, 0, 0]

           @ m2 problem2b
           [[4, 66, 9, -2, 55, 0], [7, 22, 5, 10, -5, 9]]
           None
           [[11, 88, 14, 8, 50, 9], [7, 22, 5, 10, -5, 9]]

           @ m2 test_problem2a # This tests a TEST function
           [] # No parameters
           None # Nothing returned

        In particular:
          -- Lines that begin with an  @  indicate a function to test,
               with the first word after the @ being the module name
               and the second word being the function name.
               The module name can be abbreviated as indicated above.
          -- A Test has 2 or 3 lines:
               -- Line 1: a list of the arguments
                    (So a function with one argument has [BLAH].)
               -- Line 2: the correct returned value
               -- Line 3 (if present): the correct value for the
                    arguments AFTER the function call.
                    (If absent, the function should not mutate
                    the argument.)
          -- Tests for a module must be separated by one or more
               empty lines (i.e., lines with only whitespace).
          -- A  #  character and all characters on the rest of its line
               are ignored.

        Returns a list of ReturnedValueTest objects.

        :rtype list(ReturnedValueTest)
        """

        # TODO: Implement allowing module abbreviations like m2
        # TODO: Error-detection and processing.

        returned_value_tests = []

        test_strings = test_text.split('@')[1:]

        for test_string in test_strings:
            tests = test_string.split('\n\n')

            module = tests[0].split()[0]
            function = tests[0].split()[1]
            tests[0] = tests[0].replace(module, '', 1).replace(function,
                                                               '', 1)
            for test in tests:
                if test == '':
                    continue
                lines = test.strip().splitlines()
                arguments = eval(lines[0])  # FIXME: ugh!  Better way?
                returned_value = eval(lines[1])

                # FIXME:  The following is WRONG.
                # It does not handle mutation (or not) correctly.
                if len(lines) > 2:
                    arguments_after_test = eval(lines[2])
                else:
                    arguments_after_test = arguments

                rv_test = ReturnedValueTest(module,
                                            function,
                                            arguments,
                                            returned_value,
                                            arguments_after_test)
                returned_value_tests.append(rv_test)

        print(returned_value_tests)
        return returned_value_tests

    def run_tests(self, student):
        """
        """
        # TODO: Augment the above comment.
        folder = self.where_to_grade + student + '/src/'

        rv_result = ReturnedValueTestResult()
        result = {}
        for module in self.what_to_grade.modules:
            tests = self.tests[module]
            pathname = folder + module
            result[module] = self.run_returned_value_tests(tests,
                                                           module,
                                                           pathname,
                                                           student)
        rv_result.results_by_module = result
        return rv_result

    def run_returned_value_tests(self, tests, module, pathname,
                                 student):
        """
        :type tests: list(ReturnedValueTest)
        :type module: module [A real module, NOT a filename]
        :type pathname: str [Pathname of the file to be tested]
        :type student: str
        """
        # TODO: Augment the above comment.

        # CRITICAL NOTE: The following is ugly.
        # The challenge is for this function to load a module
        # WITHOUT RETAINING the definitions loaded when this function
        # exits.  We need that because if student 1 has a correct
        # function and student 2 does not define that function at all,
        # the definition from student 1 is used.
        # There is probably a better way to solve this problem that
        # what is done below, which is to load the student's module
        # into a UNIQUELY-NAMED module and use that uniquely-named
        # module when running the tests. The uniquely-named module
        # is obtained by appending the student's username to the
        # module name.  That may fail if [something unforeseen].
        # A better approach would be to "wipe" the namespace when
        # this function exits, but I don't know how to do that.
        module_name = module + '_' + student

        spec = importlib.util.spec_from_file_location(module_name,
                                                      pathname)

        # TODO: The  load_module  method is deprecated,
        #       but I haven't figured out how to do it that method.
        # TODO: Need to deal with inability to load, can't read tests, etc.
        module = spec.loader.load_module(module_name)

        test = ReturnedValueTestCase(tests, module)
        result = test.run()
        result.subtest_results = test.subtest_results  # Extend on the fly
        return result


class ReturnedValueTestResult():
    """
    """
    # TODO: Augment the above comment.

    def __repr__(self):
        format_string = 'ReturnedValueTestResult({})'
        return format_string.format(self.results_by_module)

#     def __str__(self):
#         for result in self.result:
#         if result.wasSuccessful():
#             print('{:8}: OK'.format(result.student))
#         else:
#             print('{:8} ERRORS: {}'.format(result.student,
#                                              result.errors))
#             print('{:8} FAILURES: {}'.format(result.student,
#                                              result.failures))
#             for subtest in result.subtest_results:
#                 if subtest[0] == 'PASSED_TEST':
#                     continue
#                 print('{:8} FAILED {:9}: {}'.format(result.student,
#                                                     subtest[2][0],
#                                                     subtest))


class ReturnedValueTest():

    def __init__(self, module, function, arguments, returned_value,
                 arguments_after_test):
        self.module = module
        self.function = function
        self.arguments = arguments
        self.returned_value = returned_value
        self.arguments_after_test = arguments_after_test

    def __repr__(self):
        format_string = 'ReturnedValueTest({}, {}, {!r}, {!r}, {!r}'
        return format_string.format(self.module,
                                    self.function,
                                    self.arguments,
                                    self.returned_value,
                                    self.arguments_after_test)


class ReturnedValueTestCase(unittest.TestCase):
    """
    A TestCase that tests a function in a module by running
    this TestCase's list of  ReturnedValueTest  instances on this
    TestCase's module.  As such, it  determines whether the function
    returns the correct value and has (only) the correct side effects.
    """

    def __init__(self, tests, module):
        """
        :type tests: list(ReturnedValueTest)
        :type module: module
        """
        # Augment the above comment.
        self.subtests = tests
        self.module = module
        super().__init__('runSubTestsOnModule')

        self.subtest_results = []

    def runSubTestsOnModule(self):
        """
        """
        # TODO: Augment the above comment.
        print('***** OUTPUT from student\'s run: *****')
        for test in self.subtests:
            f = test.function
            args = test.arguments
            rv = test.returned_value
            args_after_call = test.arguments_after_test

            with self.subTest():
                error = ''  # so far
                try:
                    function = getattr(self.module, f)
                except Exception as exception:
                    # FIXME: These should be ENUMSs.
                    error = 'FUNCTION_NOT_IMPLEMENTED'
                    message = 'Function {} is not implemented'
                    triple = (error, message.format(f), test)
                    self.subtest_results.append(triple)
                    raise exception
                try:
                    result = function(*args)
                except Exception as exception:
                    error = 'THROWS_EXCEPTION'
                    message = 'Function {} throws an exception: {}'
                    triple = (error,
                              message.format(f, exception), test)
                    self.subtest_results.append(triple)
                    raise exception
                try:
                    self.assertEqual(result, rv,
                                     'Wrong returned value')
                except Exception as exception:
                    error = error + 'WRONG_RETURNED_VALUE'
                    message = 'Expected: {}. Got: {}.'
                    message = message.format(rv, result)
                try:
                    self.assertEqual(args, args_after_call,
                                     'Wrong mutation')
                except Exception as exception:
                    if error:
                        error = error + ' and BAD_MUTATION'
                        message = message + ' '
                    else:
                        error = error + 'BAD_MUTATION'
                        message = ''
                    message2 = 'Expected arguments to be: {}\nGot: {}'
                    message2 = message2.format(args_after_call, args)
                    message = message + message2

                if not error:
                    error = 'PASSED_TEST'
                    message = 'OK'

                triple = (error, message, test)
                self.subtest_results.append(triple)
                if error != 'PASSED_TEST':
                    raise exception

        print()
        print('***** RESULTS of tests: *****')
        for result in self.subtest_results:
            print(result)

        return self.subtest_results


StandardTester = ReturnedValueTester

HowToGrade = Tester  # Synonyms
StandardHowToGrade = StandardTester

#
# class TesterTest(unittest.TestCase):
#     """
#     A subclass of unittest.TestCase for testing whether a TESTING
#     function calls the function to be tested enough times.
#     For example, it might test whether  test_blah() calls blah(...)
#     at least 4 times (for 4 tests).
#     A TesterTest:
#       -- Has a module (NOT name of moudule -- the module itself)
#       -- Has the name X of a function in that module
#       -- Has a positive integer N
#     and
#       -- Runs test_X() [where X is the name of the function]
#            (and catches and ignores any exception)
#       -- Counts how many times X is called
#     The test passes if that count >= N.  Else the test fails.
#     """
#
#     def __init__(self, module, name_of_test_function,
#                  name_of_function_it_tests, min_number_of_tests):
#         self.module = module
#         self.name_of_test_function = name_of_test_function
#         self.name_of_function_it_tests = name_of_function_it_tests
#         self.min_number_of_tests = min_number_of_tests
#         super().__init__('runTestsOnModule')

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

# def test_decorator():
#     import m1
#     old = m1.foo
#     def bar():
#         print('bar')
#         old()
#     m1.foo = bar
#     m1.foo()

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
