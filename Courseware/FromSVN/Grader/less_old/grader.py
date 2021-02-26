"""
A Grader grades a ThingToGrade, using a:
  -- WhoToGrade
  -- RepoHelper (for checking out files)
  -- WhereToGrade (where the checked-out files live)
  -- Tester
  -- Recorder.

A ThingToGrade specifies the:
  -- Course (including Term)
       [and hence Course information like the students enrolled, etc]
  -- Project
  -- [optionally, NOT YET IMPLEMENTED]
       -- module(s) within the project,
       -- functions within module(s), and
       -- ???

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 1.1:  May, 2015.
"""

import repo_helper
import tester
import recorder
import main_for_testing


class Grader(object):
    """
    A Grader grades a ThingToGrade,
    for students expressed by a WhoToGrade, using a:
      -- RepoHelper (for checking out files)
      -- Tester
      -- Recorder.

    If  who_to_grade_argument      is None:  Grade all students in the course.
    If  this_tester       is None:  Use a StandardTester.
    If  this_recorderr    is None:  Use a StandardRecorder.
    If  this_repo_helper  is None:  Use a StandardRepoHelper.

    :type what_to_grade: ThingToGrade
    :type who_to_grade_argument: WhoToGrade
    :type tester: Tester
    :type recorder Recorder
    :type repo_helper RepoHelper
    """

    def __init__(self,
                 what_to_grade,
                 who_to_grade=None,
                 this_tester=None,
                 this_recorder=None,
                 this_repo_helper=None):

        self.what_to_grade = what_to_grade
        course = what_to_grade.course

        self.who_to_grade = WhoToGrade(who_to_grade, course)

        self.repo_helper = this_repo_helper or \
            repo_helper.StandardRepoHelper(what_to_grade, who_to_grade)

        self.tester = this_tester or \
            tester.StandardTester(self.what_to_grade,
                                  self.who_to_grade,
                                  self.repo_helper.get_grading_folder())

        self.recorder = this_recorder or recorder.StandardRecorder()

    # TODO: Implement use of replace_existing_repos.
    def checkout(self, replace_existing_repos=True,
                 more_usernames=None):
        """ Checkout the projects for the students to grade. """
        usernames = self.who_to_grade.students
        if more_usernames:
            usernames = usernames + more_usernames

        result = self.repo_helper.checkout_for_grading(
            usernames, replace_existing_repos)
        self._display_result_of_checkout(result)

    # TODO: Should this always skip checkout, or allow as an option?
    def grade(self, do_checkout=False, replace_existing_repos=False,
              more_usernames=None):
        """
        Grade this Grader's WhatToGrade,
        for the students/teams in this Grader's WhoToGrade,
        using this Grader's Tester,
        recording results using this Grader's Recorder.

        Optional arguments:
          -- replace_existing_repos:  indicates whether or not
               to re-checkout projects (overwriting what was there).
          -- more_usernames:   lists additional usernames whose project
               should be checked out (e.g. a SOLUTION username).
        """
#         print(self.who_to_grade_argument.students)
        # Checkout the specified students (usernames):
        if do_checkout:
            self.checkout(replace_existing_repos, more_usernames)

        # TODO: Add the replace_existing_repos as an optional argument
        #   to the RepoHelper's checkout_for_grading,
        #   so that checkout can be on a student-by-student basis.

        # TODO: Embed the following in the type of Grader or ???
#         # Checkout the  original  and  solution  projects:
#         if include_original:
#             original = self.what_to_grade.course.username_for_original
#             self.repo_helper.checkout_for_grading(what, [original])
#
#         if include_solution:
#             solution = self.what_to_grade.course.username_for_solution
#             self.repo_helper.checkout_for_grading(what, [solution])
#
        # Do the tests on the specified students (usernames)
        # and record the results:
        results = self.tester.do_tests_on_students()
#         self.recorder.record_all_results(results)
#         print('Failures:')
#         self.recorder.record_failures(results)

    @staticmethod
    def _display_result_of_checkout(result):
        """
        Display the given result, which is a 2-tuple containing:
          -- the list of failed checkouts
          -- the list of skipped checkouts

        :type result: tuple(list(str))
        """
        failures, skipped, _ = result  # Ignore the 3rd item: successes

        if failures:
            print('Checkout FAILED for the following students:')
            print(' ', *failures, sep=' ')

        if skipped:
            print('Checkout SKIPPED the following students')
            print('because their projects were already checked out:')
            print(' ', *skipped, sep=' ')


class ProjectGrader(Grader):
    # TODO: Move the part of Grader (above) that is specific to
    # grading a project to this class.

    # CONSIDER: Should a ProjectGrader use ModuleGraders?

    def __init__(self, what_to_grade):
        """
        :type what_to_grade: ThingToGrade
        """
        super().__init__(what_to_grade)


class ModuleGrader(Grader):
    # CONSIDER: Is this subclass a good thing to implement?
    # If so, implement this.
    pass


class FunctionGrader(Grader):
    # CONSIDER: Is this subclass a good thing to implement?
    # If so, implement this.
    pass


class StandardGrader(ProjectGrader):
    """
    A StandardGrader is a ProjectGrader that uses a StandardTester and
    StandardRecorder to grade all students in the ThingToGrade's Course.
    """

    def __init__(self, what_to_grade):
        """
        :type what_to_grade: ThingToGrade
        """
        super().__init__(what_to_grade)


class ThingToGrade(object):
    """
    A ThingToGrade specifies the:
      -- Course (including Term, and also course information
                 like the students enrolled, etc)
      -- Project
      -- (optionally) module(s) within the project
    """
    # CONSIDER: Perhaps allow grading of other things too,
    # e.g. listing the functions/methods/classes within a project
    # to grade.

    def __init__(self, course, project, modules=None):
        """
        Stores the given course, project and (optionally) modules.
        The project can be specified as either:
          -- a positive integer that is the session number, or
          -- the project name itself.

        :type course: Course
        :type project (int, str)
        :type modules list((int, str))
        """
        # NOTE: Throughout I have used extensions of the hint-notation
        #       despite them not yet being implemented in PyDev.
        #       In particular, PyDev does not yet allow  (int, str).

        self.course = course
        self.project = project

        try:
            # project can be a session number
            self.project_name = course.projects[project]
        except:
            # or the project name itself
            self.project_name = project

        self.modules = modules or course.get_modules(self.project_name)

    def __repr__(self):
        return 'ThingToGrade({}, {}, {})'.format(self.course,
                                                 self.project,
                                                 self.modules)


class WhoToGrade(object):
    """
    A list of usernames, or something that determines such a list.
    """

    def __init__(self, course, students_or_sections=None):
        """
        If  students_or_sections  is:
          -- None or []:  Grade all students in the course.
          -- An integer:  Grade all students in that section.
          -- A string:           Grade all usernames listed in that file.
          -- Sequence:           Grade all students listed.
          -- Filename (string):  Grade all students listed in that file.

        :type who_to_grade_indicator: (list, tuple, int)
        :type course: Course
        """
        # CONSIDER: Allow other types for  who_to_grade_indicator  ???
        #    For example, allow a single username?
        #    If so, must distinguish from a file.
        # CONSIDER: Allow GROUP names in the sequence or file?

        # Keep the indicator and course, just in case they are needed:
        self.who_to_grade_indicator = who_to_grade_indicator
        self.course = course

        if not who_to_grade_indicator:
            # None or empty list - grade all the students
            self.students = course.get_usernames()
        elif type(who_to_grade_indicator) is int:
            # integer - grade all students in that section
            self.students = course.get_usernames(who_to_grade_indicator)
        elif type(who_to_grade_indicator) is str:
            # filename - grade all students in that file
            with open(who_to_grade_indicator, 'r') as file:
                self.students = file.read().split()
        else:
            # sequence - of students to grade
            self.students = who_to_grade_indicator

        # TODO: Error handling in the above.


def main():
    main_for_testing.main()

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------
# Code below here was once useful but is no longer correct.
#
# CONSIDER: Maybe rejuventate it.
# ----------------------------------------------------------------------

#     def choose_testers(self):
#         for thing_to_grade in self.things_to_grade:
#             self.tester[thing_to_grade] = tester.Tester(thing_to_grade)
#
#         (self.grader[thing_to_grade]).grade(thing_to_grade)
#         if not self.students_to_grade:
#             self.get_students_to_grade()
#         if not self.thing_to_grade:
#             self.get_thing_to_grade()
#         results = []
#         for student in self.thing_to_grade.students:
#             for tester in self.testers:
#                 result = tester.run_tests(self.thing_to_grade, student)
#                 results.append(result)
#         self.recorder.record(results)

# class ThingToGrade:
#     """
#     Something to be graded:
#       -- A project, or a module in the project, or a function
#             in a module in the project, or a collection of these,
#          along with
#       -- a list of students (usernames, or perhaps team names)
#             whose submissions are to be graded.
#     """
#     def __init__(self,
#                  name_of_thing_to_grade=None, course=None, term=None)
#         """
#         If the thing_to_grade is:
#           -- a list => grade all the things in the list
#           -- a number N => grade all of the Session N project
#           -- a (N, M) pair => grade module M in the Session N project
#           -- a (N, M, s) triple => grade function s in module M
#                                      in the Session N project
#           -- ...
#         """
#
#         # TODO: Handle situations other than the above.
#         self.parse_name(name_of_thing_to_grade)
#         self.course = course if course else self.default_course()
#         self.term = term if term else self.current_term()
#
#
#     def parse_name(self, name_of_thing_to_grade):
#         # All these can be a list
#         self.session # 1, 2, ...
#         self.project # Session01_..., Session02_..., ...
#         self.modules
#
#     def default_course(self):
#         # TODO: Get from a   defaults.txt   file.
#         return 'csse120'
#
#     def current_term(self):
#         # TODO: Use the current date.
#         return '201510'
#
#
#     def all_students(self):
#         return
#
#         self.students = students
#         self.function_name = function_name
#         if recheckout:
#             self.checkout(True)
#
#     def checkout(self, overwrite=False):
#         svn.checkout(self.project, self.students)
