"""
Tests (informally) the Grader and other classes in this project.

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 1.1:  May, 2015.
"""

import course
import grader
import tester

# ----------------------------------------------------------------------
# NOTES to David Lam:
#   1. This project is incomplete but runs.
#
#   2. Run this module to see what gets printed.
#
#   3. In a nutshell, this project currently:
#        a. Constructs a ThingToGrade (course and project)
#             and a Grader.  See  test_Grader  below.
#
#        b. Determines the students in the course
#             and the non-example modules in the project.
#             TODO: Currently student usernames are read from a file
#             and the  Course.get_modules  method is faked
#             (hard-coded to a particular module).
#
#        c. ChangesTester: "Tests" by computing how many lines, words,
#           and characters the student file has, compared to the same
#           data for the original (no solution) file and a solution file.
#
#           ReturnedValueTester: The solution file specifies tests,
#           each of which specifies a function, arguments to send
#           the function, the correct returned value, and the mutation
#           that should occur (if any).
#
#        d. Records the result.  Currently just by printing.
#
# Major TODO's include:
#   1. Completing   Course.get_usernames()  and  Course.get_modules().
#
#   2. Restructure to have a ModuleTester and let ChangesTester
#        extend ModuleTester (not ChangesTester).  Then a ProjectTester
#        can be generic and do little other than construct and use
#        one ModuleTester per module tested.
#
#   3. Test everything far more carefully than I did.
#
# and see the  TODO, FIXME and CONSIDER comments for more to do.
# ----------------------------------------------------------------------


def main():
    """
    Tests (informally) the Grader and other classes in this project.
    """
    test_ChangesTester()
    test_ReturnedValueTester()


def test_ChangesTester():
    tester.StandardTester = tester.ChangesTester
    test_Grader()


def test_ReturnedValueTester():
    tester.StandardTester = tester.ReturnedValueTester
    test_Grader()


def test_Grader():
    # CONSIDER: This testing is inadequate.  Should we take the time
    # to make unit-tests for the classes/methods in this project?

    # TODO: At the least, test (informally) better than the following.
    csse120 = course.CSSE120
    what_to_grade = grader.ThingToGrade(csse120, 0)  # Session 16
    grader_for_testing = grader.Grader(what_to_grade)
    grader_for_testing.grade()


# ----------------------------------------------------------------------
# Code below here was once useful but is no longer correct.
#
# CONSIDER: Maybe rejuventate the following when UnitTester
# becomes operative again.
# ----------------------------------------------------------------------

# def test_UnitTester():
# #     svn.start(16)
#     t = StandardTester('Session16_Test2_201430', 'm4',
#                         file_with_tests='m4b_tests.py')
#     results = t.run()
#     print_results(results)
#
# def print_results(results):
#     for result in results:
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

if __name__ == '__main__':
    main()
