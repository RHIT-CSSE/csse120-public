"""
A Grader grades a WhatToGrade (e.g. a Session, Module in a Session,
Function in a Module, ...), for each username in Students, using a:
  -- Getter (to get the data needed to grade)
  -- Tester (to run tests that form the result of the Grader's grading)
  -- Recorder (to record the results of the tests)

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 2.0:  March, 2021.
"""

from WhatToGrade import WhatToGrade, StandardWhatToGrade
from WhoToGrade import WhoToGrade, StandardWhoToGrade
from Getter import Getter, StandardGetter
from Tester import Tester, StandardTester
from Recorder import Recorder, StandardRecorder


class Grader:
    """ Grades a Session, Module, Function, ... for a list of Students """

    def __init__(self, what_to_grade: WhatToGrade = None,
                 who_to_grade: WhoToGrade = None,
                 getter: Getter = None,
                 tester: Tester = None,
                 recorder: Recorder = None):
        if not what_to_grade:
            what_to_grade = StandardWhatToGrade()
        if not who_to_grade:
            who_to_grade = StandardWhoToGrade()
        if not getter:
            getter = StandardGetter(what_to_grade, who_to_grade)
        if not tester:
            tester = StandardTester(what_to_grade, who_to_grade)
        if not recorder:
            recorder = StandardRecorder(what_to_grade, who_to_grade)

        self.what_to_grade = what_to_grade
        self.who_to_grade = who_to_grade
        self.getter = getter
        self.tester = tester
        self.recorder = recorder

    def grade(self):
        self.getter.get()
        results = self.tester.test()
        self.recorder.record(results)

#
#         self.what_to_grade = what_to_grade
#         course = what_to_grade.course
#
#         self.who_to_grade = (this_who_to_grade
#                              or StandardWhoToGrade(course))
#         self.repo_helper = (this_repo_helper
#                             or StandardRepoHelper(what_to_grade))
#         how = (this_how_to_grade or StandardHowToGrade)
#         self.how_to_grade = how(self.what_to_grade,
#                                 self.who_to_grade,
#                                 self.repo_helper)
#         self.recorder = this_recorder or StandardRecorder()
#
#     def grade(self, force_checkout=False, display_results=True):
#         """ Do the grading. """
#         # Checkout:
#         checkout = self.repo_helper.checkout_for_grading  # Abbreviation
#         result = checkout(self.what_to_grade,
#                           self.who_to_grade.students,
#                           force_checkout)
#         if display_results:
#             self._display_result_of_checkout(result)
#
#         # Grade:
#         results = self.how_to_grade.do_tests()
#         # Record:
#
# #         # Checkout the  original  and  solution  projects:
# #         if include_original:
# #             original = self.what_to_grade.course.username_for_original
# #             self.repoHelper.checkout_for_grading(what, [original])
# #
# #         if include_solution:
# #             solution = self.what_to_grade.course.username_for_solution
# #             self.repoHelper.checkout_for_grading(what, [solution])
# #
# #         # Do the tests on the specified students (usernames)
# #         # and record the results:
# #         results = self.howToGrade.do_tests_on_students()
# #         self.recorder.record_all_results(results)
# #         print('Failures:')
# #         self.recorder.record_failures(results)
#
#     @staticmethod
#     def _display_result_of_checkout(result):
#         """
#         Display the given result, which is a 2-tuple containing:
#           -- the list of failed checkouts
#           -- the list of skipped checkouts
#
#         :type result: tuple(list(str))
#         """
#         failures, skipped, _ = result  # Ignore the 3rd item: successes
#
#         if failures:
#             print('\nCheckout FAILED for the following students:')
#             print(' ', *failures, sep=' ')
#
#         if skipped:
#             print('\nCheckout SKIPPED the following students')
#             print('because their projects were already checked out:')
#             print(' ', *skipped, sep=' ')
#
#
# class ProjectGrader(Grader):
#     # TODO: Move the part of Grader (above) that is specific to
#     # grading a project to this class.
#
#     # CONSIDER: Should a ProjectGrader use ModuleGraders?
#
#     def __init__(self, what_to_grade):
#         """
#         :type what_to_grade: ThingToGrade
#         """
#         super().__init__(what_to_grade)
#
#
# class ModuleGrader(Grader):
#     # CONSIDER: Is this subclass a good thing to implement?
#     # If so, implement this.
#     pass
#
#
# class FunctionGrader(Grader):
#     # CONSIDER: Is this subclass a good thing to implement?
#     # If so, implement this.
#     pass
#
#
# class StandardGrader(ProjectGrader):
#     """
#     A StandardGrader is a ProjectGrader that uses a StandardTester and
#     StandardRecorder to grade all students in the ThingToGrade's Course.
#     """
#
#     def __init__(self, what_to_grade):
#         """
#         :type what_to_grade: ThingToGrade
#         """
#         super().__init__(what_to_grade)
#
#
# # ----------------------------------------------------------------------
# # Code below here was once useful but is no longer correct.
# #
# # CONSIDER: Maybe rejuventate it.
# # ----------------------------------------------------------------------
#
# #     def choose_testers(self):
# #         for thing_to_grade in self.things_to_grade:
# #             self.howToGrade[thing_to_grade] = howToGrade.Tester(thing_to_grade)
# #
# #         (self.grader[thing_to_grade]).grade(thing_to_grade)
# #         if not self.students_to_grade:
# #             self.get_students_to_grade()
# #         if not self.thing_to_grade:
# #             self.get_thing_to_grade()
# #         results = []
# #         for student in self.thing_to_grade.students:
# #             for howToGrade in self.testers:
# #                 result = howToGrade.run_tests(self.thing_to_grade, student)
# #                 results.append(result)
# #         self.recorder.record(results)
#
# # class ThingToGrade:
# #     """
# #     Something to be graded:
# #       -- A project, or a module in the project, or a function
# #             in a module in the project, or a collection of these,
# #          along with
# #       -- a list of students (usernames, or perhaps team names)
# #             whose submissions are to be graded.
# #     """
# #     def __init__(self,
# #                  name_of_thing_to_grade=None, course=None, term=None)
# #         """
# #         If the thing_to_grade is:
# #           -- a list => grade all the things in the list
# #           -- a number N => grade all of the Session N project
# #           -- a (N, M) pair => grade module M in the Session N project
# #           -- a (N, M, s) triple => grade function s in module M
# #                                      in the Session N project
# #           -- ...
# #         """
# #
# #         # TODO: Handle situations other than the above.
# #         self.parse_name(name_of_thing_to_grade)
# #         self.course = course if course else self.default_course()
# #         self.term = term if term else self.current_term()
# #
# #
# #     def parse_name(self, name_of_thing_to_grade):
# #         # All these can be a list
# #         self.session # 1, 2, ...
# #         self.project # Session01_..., Session02_..., ...
# #         self.modules
# #
# #     def default_course(self):
# #         # TODO: Get from a   defaults.txt   file.
# #         return 'csse120'
# #
# #     def current_term(self):
# #         # TODO: Use the current date.
# #         return '201510'
# #
# #
# #     def all_students(self):
# #         return
# #
# #         self.students = students
# #         self.function_name = function_name
# #         if recheckout:
# #             self.checkout(True)
# #
# #     def checkout(self, overwrite=False):
# #         svn.checkout(self.project, self.students)
