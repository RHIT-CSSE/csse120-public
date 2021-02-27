# FIXME: This file needs to be reworked!!!!!!!!!

# CONSIDER: This testing is inadequate.  Should we take the time
# to make unit-tests for the classes/methods in this project?

"""
Tests (informally) the Grader and other classes in this project.

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 1.2:  March, 2017.
"""

from grader import Grader
from whatToGrade import WhatToGrade
from whoToGrade import WhoToGrade
from howToGrade import CommitsTester
from howToGrade import UnitTestTester
from course import CSSE120


def main():
    """
    Tests (informally) the Grader and other classes in this project.
    """
#     test_UnitTester()
    test_CommitsTester()


def test_UnitTester():
    what = WhatToGrade(CSSE120, 31)
    who = WhoToGrade('usernames.txt')
#     how = UnitTestTester()
    Grader(what, who, None).grade()


def test_CommitsTester():
    what = WhatToGrade(CSSE120, 1)
    who = WhoToGrade('usernames.txt')
    how = CommitsTester
    Grader(what, who, how).grade()

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


# def grade(name, test1, test2, final_pp, final_computer, project):
#     test1_percent = 0.10
#     test2_percent = 0.15
#     final_percent = 0.40
#     project_percent = 0.35
#     final = (final_pp + final_computer) / 2
#     test_points = ((test1 * test1_percent)
#                    + (test2 * test2_percent)
#                    + (final * final_percent))
#     test_percent = test1_percent + test2_percent + final_percent
#     test_average = test_points / test_percent
#
#     overall = (((test_average * test_percent) + (project * project_percent))
#                /
#                (test_percent + project_percent))
#
#     print('{:6} {:3} {:3} {:5.1f} {:3} {:5.1f} {:5.1f}'.format(
#         name, test1, test2, final, project, test_average, overall))
#
# # Ally:
# test1 = test2 = (45 + 55)
# final_pp = (35.5 / 42) * 100
# final_computer = 0  # Would have been ??
# project = 88
# grade('Ally', test1, test2, final_pp, final_computer, project)
#
# # Casey:
# test1 = test2 = (33 + 55)
# final_pp = (29 / 42) * 100
# final_computer = 0  # 100 * 7 / 58  # per actual final exam
# project = 88
# grade('Casey', test1, test2, final_pp, final_computer, project)
#
# # Katie:
# test1 = test2 = (28 + 55)
# final_pp = (12 / 42) * 100
# final_computer = 0
# project = 80
# grade('Katie', test1, test2, final_pp, final_computer, project)
#
#
def grade2(name, test1, test2, test3, final, project):
    test1_percent = 0.10
    test2_percent = 0.15
    test3_percent = 0.20
    final_percent = 0.20
    project_percent = 0.35

    test_points = ((test1 * test1_percent)
                   + (test2 * test2_percent)
                   + (test3 * test3_percent)
                   + (final * final_percent))
    test_percent = test1_percent + test2_percent + \
        test3_percent + final_percent
    test_average = test_points / test_percent

    overall = (((test_average * test_percent) + (project * project_percent))
               /
               (test_percent + project_percent))

    print('{:6} {:3} {:3} {:5.1f} {:5.1f} {:3} {:5.1f} {:5.1f}'.format(
        name, test1, test2, test3, final, project, test_average, overall))

# # Ally:
# test1 = test2 = (45 + 55)
# test3 = (35.5 / 42) * 100
# final = 0  # Would have been ??
# project = 88
# grade2('Ally', test1, test2, test3, final, project)
#
# # Casey:
# test1 = test2 = (33 + 55)
# final_pp = (29 / 42) * 100
# final_computer = 0  # 100 * 7 / 58  # per actual final exam
# project = 88
# grade2('Casey', test1, test2, final_pp, final_computer, project)
#
# # Katie:
# test1 = test2 = (28 + 55)
# final_pp = (12 / 42) * 100
# final_computer = 0
# project = 80
# grade2('Katie', test1, test2, final_pp, final_computer, project)

if __name__ == '__main__':
    main()
