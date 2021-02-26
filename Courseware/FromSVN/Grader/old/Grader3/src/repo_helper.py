"""
A RepoHelper can checkout repositories,
return the pathname where a repository is stored,
and return the usernames from a course.

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 1.1:  May, 2015.
"""
# FIXME: Above comment is no longer correct.

import os
import re
import subprocess

# NOTE: Change the GRADING_FOLDER as needed for your computer.
GRADING_FOLDER = 'C:/EclipseWorkspaces/csse120-grading/'
URL_FOR_SVN_REPOS = 'http://svn.csse.rose-hulman.edu/repos/'


# TODO: Move the SVN-specific stuff from the following class
#       to SVNHelper class.  Leave RepoHelper an abstract class.
class RepoHelper(object):
    """
    Abstract class, subclass must specify ???
    A RepoHelper can checkout repositories for a course,
    return the pathname where a repository is stored,
    and return the usernames from a course.
    """
    # TODO: Fix the above comment.

    def __init__(self, what_to_grade):
        self.what_to_grade = what_to_grade

    def project_name(self, session):
        """
        Returns the project name for the given session number.
        """
        # FIXME: This is not adequate, see comments elsewhere about it.
        session = int(session)  # To allow a string, e.g. '01' for 1
        return self.course.projects[session]

    def checkout_for_grading(self, what_to_grade, students,
                             force_checkout=False):
        """
        Checkouts the given project for all the given list of students.
        Returns three lists:
          -- students for which the checkout appears to have failed
          -- students skipped (because they were already checked out)
          -- all remaining students
        """
        # CONSIDER: Allow checking out things other than projects??
        failures, skips, successes = [], [], []
        for student in students:
            url = self.get_url(what_to_grade, student)
            folder = self.get_grading_folder(student)
            if not force_checkout and os.access(folder, os.F_OK):
                skips.append(student)
                continue

            result = self.checkout(url, folder)
            if result:
                successes.append(student)
            else:
                failures.append(student)

        # FIXME: fix_all_for_eclipse does not appear to be working?
        # CONSIDER: It is not necessary for the autograding,
        # but would still be wise to do????
        self.fix_all_for_eclipse(students, what_to_grade.project_name)
        return (failures, skips, successes)

    def get_url(self, what_to_grade, student):
        """
        Returns the URL for the given student's ThingToGrade.
        :type what_to_grade: ThingToGrade
        """
        repo = URL_FOR_SVN_REPOS + what_to_grade.course.students_repo \
            + '-' + student + '/' + what_to_grade.project_name
        return repo

    def get_grading_folder(self, student=None):
        """
        Returns the folder into which to checkout
        this RepoHelper's project (or the folder into which it was
        checked out, if student is not None).

        :rtype str
        """
        # FIXME:
        # This presumes a folder structure that others might not want.
        # But at least the structure is encapsulated in this function.
        folder = GRADING_FOLDER
        folder += self.what_to_grade.course.term + '/'
        folder += self.what_to_grade.project_name + '/'

        if student:
            folder += student + '/'

        return folder

    def get_usernames(self, groups=None):
        """
        The argument, if present, is either a section number
        or a sequence of group names.  Returns a list of usernames
        for that section or for that sequence of group names.
        """
        if not groups:
            sections = self.course.sections
        else:
            # TODO: Is there a better way to tell whether
            #       groups is a sequence?
            try:
                len(groups)
                # FIXME: Deal with this case.  See commented-out code.
            except:
                sections = [groups]

        # FIXME: Really should get this information from the
        #        course web site.  See commented-out code.
        usernames = []
        for section in sections:
            file = open('usernames-' + str(section) + '.txt', 'r')
            for username in file.readlines():
                usernames.append(username.strip())
        return usernames

#     url_prefix = roster_folder + COURSE + '-' + TERM + '-'
#     for group in groups:
#         url = url_prefix + group + '.txt'
#         print(url)
#         usernames_as_byte_array = urllib.request.urlopen(url).read()
#         usernames_in_group = usernames_as_byte_array.decode().split()
#         usernames.extend(usernames_in_group)
#
#     return usernames

    def checkout(self, url, folder):
        """
        Checks out the given URL into the given folder.
        Returns True if the checkout succeeded, else False.
        """
        # FIXME: You need to make Tortoise learn your password somehow.
        #    Otherwise, use something like:
        #      os.system('svn checkout ' + url + ' ' + folder
        #            + ' --username mutchler --password XXX')
        #    But note that the latter is a security hazard
        #    (see me for details).
        try:
            command = 'svn checkout ' + url + ' ' + folder
            result = subprocess.call(command, stderr=subprocess.DEVNULL)
#             result = os.system('svn checkout ' + url + ' ' + folder)
            return (True if result == 0 else False)
        except:
            return False

    def fix_all_for_eclipse(self, project, students):
        """
        For each of the given students, renames the project to be the
        student's username.  This allows all the projects to exist in a
        single Eclipse workspace.
        Returns a list of students for whom this failed for any reason.
        """
        failures = []
        for student in students:
            try:
                folder = self.get_grading_folder(student, project)
                result = self.fix_for_eclipse(folder, project, student)
                if not result:
                    failures.append(student)
            except:
                failures.append(student)

        return failures

    def fix_for_eclipse(self, folder, project, student):
        """
        Modifies the  .project  file in the given folder to rename
        the project from its name to the given student (username).
        This allows Eclipse to import  multiple students' projects
        for the same assignment (all of which share the same project
        name before running this function).
        Returns  True  if this action succeeded, else returns  False.
        """
        # FIXME: The following is brittle and WILL BREAK if
        #        Eclipse changes its project filenames.
        filename = folder + '/.project'
        try:
            with open(filename, 'r') as file:
                file_contents = file.read()

            lines = file_contents.split('\n')
            with open(filename, 'w') as file:
                for line in lines:
                    print(re.sub(project, student, line), file=file)
        except:
            # FIXME: Figure out whether this detects failures correctly.
            print('Could not open the file:')
            print('   ', filename)
            ('Fix and try again.\n')
            return False

        return True


# ----------------------------------------------------------------------
# NOTE: The following code assumes that you have installed Tortoise SVN
#       and put command-line tools (e.g.   svn   ) in your system path.
# ----------------------------------------------------------------------
class SVNRepoHelper(RepoHelper):
    """
    An Subversion (SVN) implementation, hosted by CSSE,
    of the RepoHelper abstract class.
    """
    # TODO: Pull SVN-specific stuff from RepoHelper (above) to here.


class StandardRepoHelper(SVNRepoHelper):
    """ The default class to use as RepoHelper is a SVNRepoHelper. """


# ----------------------------------------------------------------------
# NOTE: The following code is not currently used.
# ----------------------------------------------------------------------
#
#
# class Student(object):
#     def __init__(self, username, name, campus_mail, major, class_, year,
#                  advisor, email):
#         self.username = username
#
#
# # class Checker_Outer(object):
# #     default_course = 'csse120'
# #
# #     def __init__(self, course=Checker_Outer.default_course, term=None):
# #         self.course = course
# #         # TODO: Determine the term from today's date.
# #         self.term = 201510
# #         # TODO: Determine the sections from Schedule Lookup Page.
# #         self.sections = ['01', '02', '03', '04']
# #
# #         self.url_for_course_lookup = URL_FOR_SCHEDULE_LOOKUP
# #
# #     def enrolled_students(self, section=None):
# #         """
# #         Returns a list of all the Student  (u that are members of the given sequence
# #         of groups.  The usernames must be stored in text files that
# #         are in the appropriate place.
# #         """
# #         students = []
# #         url_prefix = roster_folder + COURSE + '-' + TERM + '-'
# #     for group in groups:
# #         url = url_prefix + group + '.txt'
# #         usernames_as_byte_array = urllib.request.urlopen(url).read()
# #         usernames_in_group = usernames_as_byte_array.decode().split()
# #         usernames.extend(usernames_in_group)
# #
# #     return usernames
#
#
# # def main():
# #     start(0)
# #
# #
# # def start(project_number):
# #     project = PROJECTS[project_number]
# #     students = get_usernames_from_rosters()
# #
# #     failures1 = checkout_all(project, students)
# #     failures2 = fix_all_for_eclipse(project, students)
# #     print('Failed checkout:', failures1)
# #     print('Failed fix-for-Eclipse:', failures2)
# #
# #     remove_extra(project, students)
#
#
# #     checkout_solution(project)
# #     folder = get_grading_folder(SOLUTION_USERNAME, project)
# #     fix_for_eclipse(folder, project + SOLUTION_SUFFIX,
# #                     SOLUTION_USERNAME)
#
#
#
#
#
#
#
# def checkout_solution(project_to_grade, solution_name=None):
#     """
#     Checkouts the solution for the given project.
#     Puts it in the same place as the student solutions are placed.
#     Returns True if succeeded, else False.
#     """
#
#     url = get_solution_url(project_to_grade)
#     folder = get_grading_folder(SOLUTION_USERNAME, project_to_grade)
#     if os.access(folder, os.F_OK):
#         print('WARNING: SKIPPING', folder, 'because it already exists')
#         return False
#     success_or_failure = checkout(url, folder)
#     return success_or_failure
#
#
#
# def get_solution_url(project_to_grade):
#     """ Returns the URL for the solution for the given project. """
#     repo = COURSE_REPO_NAME + '/' + ECLIPSE_PROJECTS + '/' + TERM
#     solution = project_to_grade + SOLUTION_SUFFIX
#     return URL_FOR_SVN_REPOS + repo + '/' + solution
#
#
#
#
#
#
#
#
# # Functions below are NOT correct.
#
# def remove_extra(project_to_grade, students):
#     """
#     Removes all unnecessary information from the projects:
#       -- All SVN information
#       -- All .docx and .pdf files
#     """
#     for student in students:
#         folder = get_grading_folder(student, project_to_grade)
#         remove_extra_in_folder(folder)
#
#
# def remove_extra_in_folder(folder):
#     """
#     At the TOP level of the given folder,
#     as well as in the   src   subfolder (if it exists),
#     removes any of the following that exist:
#       *.docx, *.pdf, *.gif
#     """
#     # FIXME: THIS IS A DANGEROUS FUNCTION.
#     #        If the folder is somehow not what is intended,
#     #        LOTS of files can be IRREVOCABLY DELETED.
#
#     # Temporary attempt at safety:
#     try:
#         assert(folder.startswith(GRADING_FOLDER))
#     except:
#         print('ERROR ERROR ERROR in remove_extra_in_folder')
#         raise Exception('Error in remove_extra_in_folder')
#
#     # Here is the dangerous part:
#     for file in os.listdir(folder):
#         if (file == '.svn'):
#             pass  # shutil.rmtree(folder + '/.svn')
#         if fnmatch.fnmatch(file, '*.pdf'):
#             os.remove(folder + '/' + file)
#         if fnmatch.fnmatch(file, '*.docx'):
#             os.remove(folder + '/' + file)
#
#     for file in os.listdir(folder + '/src'):
#         if fnmatch.fnmatch(file, '*.gif'):
#             os.remove(folder + '/src/' + file)
#

