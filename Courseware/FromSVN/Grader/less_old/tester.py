# TODO: Put a comment here.

import lines_of_code
import main_for_testing
import abc
import importlib.util
import unittest
import os.path


class Tester(object):
    """
    Base class for testing student code.
    """
    # TODO: Augment the above comment.

    def __init__(self, what_to_grade, who_to_grade, where_to_grade):
        """
        Can run tests on the given  what_to_grade
        for the students specified by the given  who_to_grade,
        assuming that checked-out projects are in
        the given   where_to_grade   folder.

        type: what_to_grade: WhatToGrade
        type: who_to_grade: WhoToGrade
        type: where_to_grade: str
        """
        # TODO: Make the where_to_grade an instance of a WhereToGrade
        self.what_to_grade = what_to_grade
        self.who_to_grade = who_to_grade
        self.where_to_grade = where_to_grade

    def do_tests_on_students(self):
        """
        Does this Tester's tests:
          -- on its WhatToGrade,
          -- for ALL of the students specified by its WhoToGrade,
          -- in the folder specified where its WhereToGrade.
        Prints appropriate messages in doing so.
        Returns a TesterResult.
          :rtype TesterResult
        """
        tester_result = TesterResult(self)

        self.initialize_tests_for_all_students()

        for student in self.who_to_grade.students:
            (tester_result.
             add_student_results(self.do_tests_on_student(student)))

        return tester_result

    def initialize_tests_for_all_students(self):
        """
        Called (once) by do_tests_on_students  prior to doing any tests.

        Raises an exception that is a subclass of  OSError
        if the WhereToGrade object does not exist, is not a folder,
        or is not accessible.

        Subclasses should raise an Exception if anything else
        goes wrong with the initialization they do.
        """
        # Check that  where to grade  exists and is readable:
        os.listdir(self.where_to_grade)

    def do_tests_on_student(self, student):
        # Foo.
        print('hi')
        """
        Does this Tester's tests on 
        for the given student.  Prints appropriate messages, runs the test,
        and returns a TesterUnitResult for this student.

        :rtype TesterUnitResult
        """
        self.start_tests(student)
        results_for_student = ResultsForStudent(student,
                                                self.what_to_grade)
        # Just testing.
        if self.initialize_tests_for_student(student,
                                             results_for_student):
            self.run_tests(student, results_for_student)

        self.end_tests(student)
        return results_for_student

    def initialize_tests_for_student(self, student,
                                     results_for_student):
        """
        Called (once) by  do_tests_on_student  prior to doing tests
        on all the modules for that student.
        Mutates the given  results_for_student  to reflect any tests
        that can be skipped.

        Returns False if ALL tests should be skipped.
          :type results_for_student: ResultsForStudent
        """
        # The following assumes the Python structure.
        (project_folder,
         folder_with_modules) = self.get_student_folders(student)

        # Make sure that the student's required folders exist:
        #  project folder and folder with modules.
        for folder in (project_folder, folder_with_modules):
            if not os.path.exists(folder):
                result = MissingFolder(student, folder)
                results_for_student.results.append(result)
                results_for_student.contains_errors = True
                return False

#         # Mark any modules that do not exist.
#         for module in self.what_to_grade.modules:
#             pathname = folder_with_modules + module
#             if not os.path.exists(pathname):
#                     tester_result.results_by_module[module] = 'No such module'
#                     message = 'PARTIAL FAILURE: Missing module(s)'
#
#         tester_result.error_message = message

    def get_student_folders(self, student):
        project_folder = self.where_to_grade + student
        folder_with_modules = project_folder + '/src/'

        return project_folder, folder_with_modules

    @abc.abstractmethod
    def run_tests(self, student, tester_result):
        """
        Runs all of this Tester's tests on the given student.
        Mutates the given TesterUnitResult to reflect
        the results of the tests.
        """
        # TODO: Augment the above comment.

        # CONSIDER: The following assumes that the top-level
        # of what_to_grade is MODULES.  Make it broader???
#         print(tester_result.results_by_module)
        for module in self.what_to_grade.modules:
            if module not in tester_result.results_by_module:
                self.run_tests_on_module(student,
                                         module,
                                         tester_result)

    def start_tests(self, student):
        print()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('TESTING:', student)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    def end_tests(self, student):
        pass

    def run_tests_on_module(self, student, module, tester_result):
        # Override in subclass.
        pass


class TesterResult(object):

    def __init__(self, tester):
        self.tester = tester
        self.results_by_student = {}

    def add_student_results(self, student_results, overwrite=False):
        """
        Add the given  student_results  to  self.results_by_student.

        Raises an exception if  overwrite  is False and there is an
        existing TesterResultForStudent in self.results_by_student.

          :type student_results: TesterResultForStudent
        """
        student = student_results.student

        if overwrite and (student in self.results_by_student):
            message = ('Attempted to add a TesterResultForStudent'
                       + ' where one already exists.\n'
                       + 'Existing: {}\n'
                       + 'New:      {}\n'.format(
                           self.results_by_student.student,
                           student_results))
            raise KeyError(message)

        self.results_by_student[student] = student_results


class ResultsForStudent(object):

    def __init__(self, student, what_to_test):
        self.student = student
        self.what_was_tested = what_to_test

        # The rest are set as the testing proceeds:
        self.contains_errors = False
        self.results = []
        self.results_by_module = {}

    def add_tester_result(self, tester_result, contains_error=False):
        self.contains_errors = contains_error and self.contains_errors
        self.results.append(tester_result)
        if tester_result.module:
            self.results[tester_result.module].append(tester_result)


class TesterResultsForStudent(object):

    def __init__(self, student=None, what_was_tested=None,
                 where_to_grade=None,
                 error_message=None):
        """
        The result from ALL of a Tester's tests
        on its  WhatToGrade  for a SINGLE student.

        :type student: str
        :type what_was_tested: WhatToGrade
        """
        # TODO: The above arguments are not what is needed, I think.
        # TODO: Clarify the above comment.
        # TODO: This is a base class, describe and organize it as such.
        self.student = student
        self.what_was_tested = what_was_tested

        self.contains_errors = False

        self.error_message = error_message or ''
        self.results_by_module = {}

        # Python-specific:
        self.where_to_run_tests = where_to_grade + student + '/src/'

    def __repr__(self):
        s = 'Student: {}.\nContains errors: {}.\n'
        return s


class TesterUnitResult(object):

    def __init__(self,
                 student=None, what_was_tested=None, module=None,
                 score=None, contains_errors=False, error_code=None,
                 error_messages=None, other_messages=None):
        """
        The result from running ONE of a Tester's tests
        in its  WhatToGrade  for a single student.

        :type student: str
        :type what_was_tested: WhatToGrade
        """
        # TODO: Clarify the above comment.
        # TODO: Is this a base class?
        #       If so, describe and organize it as such.
        self.student = student
        self.what_was_tested = what_was_tested
        self.module = module

        self.score = score
        self.contains_errors = contains_errors or False
        self.error_code = error_code
        self.error_messages = error_messages or []
        self.other_messages = other_messages or []

        # Can the rest go away?

#         self.error_message = error_message or ''
#         self.results_by_module = {}

        # Python-specific:
#         self.where_to_run_tests = where_to_grade + student + '/src/'


class MissingFolder(TesterUnitResult):

    def __init__(self, student, missing_folder):
        self.missing = missing_folder
        message = 'The followed required folder does not exist: {}'

        super().__init__(student, missing_folder,
                         score=0, contains_errors=True,
                         error_code=-1,  # FIXME: Need specific error code.
                         error_messages=[message.format(missing_folder)],
                         other_messages=[])


class MissingModule(TesterUnitResult):

    def __init__(self, student, what_was_tested, missing_module):
        message = 'The followed required module does not exist: {}'

        super().__init__(student, what_was_tested,
                         score=0, contains_errors=True,
                         error_code=-1,  # FIXME: Need specific error code.
                         error_messages=[message.format(missing_module)],
                         other_messages=[])


class NoSrcFolderTesterResult(TesterUnitResult):
    pass


# ----------------------------------------------------------------------
# New:  tries to use the unittest module by, for each student:
#  1. Create a new file that contains their file minus the call to main.
#     Name the new file with a unique-to-student name.
#  2. In the same folder as the new file, put a copy of the unittest
#     file that I make, but with the import using the module (file)
#     name specific to that student.
#  3. Import the unitest file (which will import the new file) into
#     a module, as is already done below.
#  4. Run the unitest file.
#  5. Extract the results from the unitest run.
# ----------------------------------------------------------------------
class UnittestTester(Tester):
    # TODO: Incorporate the above comment into the doc-string(s) here.

    def __init__(self, what_to_grade, who_to_grade, where_to_grade):
        # CONSIDER:
        # If the superclass call is all that is needed,
        # remove this method definition (maybe with a comment added).
        super().__init__(what_to_grade, who_to_grade, where_to_grade)

        # FIXME: THe next lines have gotten garbled!!!!!
#         temp_folder = self.where_to_grade
#         if not os.path():
#         try:
#             os.mkdir(where_to_grade + 'UnittestsGenerated')
#         except:

    def initialize_tests_for_all_students(self):
        super().initialize_tests_for_all_students()

        # Assumes a particular structure.
        # Check whether the   UnitTests   folder exists and is readable:
        unittests_folder = self.where_to_grade + 'UnitTests/'
        os.listdir(unittests_folder)

        # Check whether each module to be tested has a corresponding
        # module in the   UnitTests   folder.
        # TODO: This is not the best way to do this,
        # and it assumes a file-naming that might not be best.
        for module in self.what_to_grade.modules:
            with open(unittests_folder + 'test_' + module, 'r'):
                pass

    def run_tests_on_module(self, student, module, tester_result):

        #  1. Create a new file that contains their file minus the call
        #     to main.  Name the new file with a unique-to-student name.
        pass


class ChangesTester(Tester):
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

        type: what_to_grade: ThingToGrade
        type: who_to_grade: WhoToGrade
        type: where_to_grade: str
        """
        super().__init__(what_to_grade, who_to_grade, where_to_grade)

        # The following are set by  initialize_tests_for_all_students
        #   (which is called by  do_tests).
        self.stats_for_original = None
        self.stats_for_solution = None

    def initialize_tests_for_all_students(self):
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


class ChangesTesterResult(TesterUnitResult):
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

        # The following are set by  initialize_tests_for_all_students
        #   (which is called by  do_tests).
        self.tests = None

    def initialize_tests_for_all_students(self):
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

        return returned_value_tests

    def run_tests_on_module(self, student, module, tester_result):
        """
        """
        # TODO: Augment the above comment.
        folder = self.where_to_grade + student + '/src/'
        pathname = folder + module

        tests = self.tests[module]

        result = self.run_returned_value_tests(tests,
                                               module,
                                               pathname,
                                               student)

        tester_result.results_by_module[module] = result

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

        # These two lines seem to be the non-deprecated way to ...
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # do this:
#         module = spec.loader.load_module(module_name)

        # TODO: Test that the above non-deprecated way really works
        #       like I need it to.
        # TODO: Need to deal with inability to load, can't read tests, etc.

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


def main():
    main_for_testing.main()

if __name__ == '__main__':
    main()

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
