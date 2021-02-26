"""
Functions to get student projects for CSSE 120 (or other courses)
from SVN and to prepare them to be graded.

Authors: David Mutchler, Chandan Rupakheti, Amanda Stouder, David Lam,
         and their colleagues, December 2013, modified May 2015.
"""

#-----------------------------------------------------------------------
# NOTE: This code assumes that you have installed Tortoise SVN
#       and put command-line tools (e.g.   svn   ) in your system path.
#-----------------------------------------------------------------------

import urllib.request
import os
import re
import shutil
import fnmatch

# NOTE: Change the GRADING_FOLDER as needed for your computer.
GRADING_FOLDER = 'C:/EclipseWorkspaces/csse120-grading/'

# Don't forget to change the TERM each term, and the SECTIONS.
COURSE = 'csse120'
TERM = '201510'
SECTIONS = ('01', '02', '03', '04')

COURSE_REPO_NAME = 'csse120-python/branches/robonew/'
ECLIPSE_PROJECTS = 'EclipseProjects'
SOLUTION_SUFFIX = '_SOLUTION'
SOLUTION_USERNAME = '0_SOLUTION'

PROJECTS = ['Session25_Test3',
            'Session01_IntroductionToPython',
            'Session02_InputComputeOutput',
            'Session03_LoopsAndUsingObjects',
            'Session04_FunctionsAndAccumulators',
            'Session05',
            'Session06',
            'Session07',
            'Session08_Test1',
            'Session09_',
            'Session10',
            'Session11_AccumulatingSequencesAndFancyIterating',
            'Session12',
            'Session13',
            'Session14',
            'Session15_Test2',
            'Session16_Test2_201430',
            'Session30_Test3_Part2',
            ]

URL_FOR_SVN_REPOS = 'http://svn.csse.rose-hulman.edu/repos/'
URL_FOR_CSSE_HOME = 'http://www.rose-hulman.edu/class/csse/'
FOLDER_FOR_ROSTERS = 'Rosters'
URL_FOR_ROSTERS = URL_FOR_CSSE_HOME + COURSE + '/' + TERM + '/' \
    + FOLDER_FOR_ROSTERS + '/' + TERM + '/'


class Student(object):
    def __init__(self, username, name, campus_mail, major, class_, year, advisor, email):
        self.username = username


class RepoHelper():
    def __init__(self):
        pass
    
    def 

# class Checker_Outer(object):
#     default_course = 'csse120'
#
#     def __init__(self, course=Checker_Outer.default_course, term=None):
#         self.course = course
#         # TODO: Determine the term from today's date.
#         self.term = 201510
#         # TODO: Determine the sections from Schedule Lookup Page.
#         self.sections = ['01', '02', '03', '04']
#
#         self.url_for_course_lookup = URL_FOR_SCHEDULE_LOOKUP
#
#     def enrolled_students(self, section=None):
#         """
#         Returns a list of all the Student  (u that are members of the given sequence
#         of groups.  The usernames must be stored in text files that
#         are in the appropriate place.
#         """
#         students = []
#         url_prefix = roster_folder + COURSE + '-' + TERM + '-'
#     for group in groups:
#         url = url_prefix + group + '.txt'
#         usernames_as_byte_array = urllib.request.urlopen(url).read()
#         usernames_in_group = usernames_as_byte_array.decode().split()
#         usernames.extend(usernames_in_group)
#
#     return usernames


def main():
    start(0)


def start(project_number):
    project = PROJECTS[project_number]
    students = get_usernames_from_rosters()

    failures1 = checkout_all(project, students)
    failures2 = fix_all_for_eclipse(project, students)
    print('Failed checkout:', failures1)
    print('Failed fix-for-Eclipse:', failures2)

    remove_extra(project, students)


#     checkout_solution(project)
#     folder = get_grading_folder(SOLUTION_USERNAME, project)
#     fix_for_eclipse(folder, project + SOLUTION_SUFFIX,
#                     SOLUTION_USERNAME)


def get_usernames_from_rosters(groups=SECTIONS, roster_folder=URL_FOR_ROSTERS):
    """
    Returns a list of usernames that are members of the given sequence
    of groups.  The usernames must be stored in text files that
    are in the appropriate place.
    """
    file = open('usernames.txt', 'r')
    usernames = []
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


def checkout_all(project_to_grade, students):
    """
    Checkouts the given project for all the given students.
    Returns a list of all students SKIPPED or for which checkout
    appears to have failed.
    """
    failures = []
    for student in students:
        url = get_url(student, project_to_grade)
        folder = get_grading_folder(student, project_to_grade)
        if os.access(folder, os.F_OK):
            print('WARNING: SKIPPING', folder, 'because it already exists')
            failures.append(student)
            continue
        success = checkout(url, folder)
        if not success:
            failures.append(student)

    return failures

def checkout_solution(project_to_grade, solution_name=None):
    """
    Checkouts the solution for the given project.
    Puts it in the same place as the student solutions are placed.
    Returns True if succeeded, else False.
    """

    url = get_solution_url(project_to_grade)
    folder = get_grading_folder(SOLUTION_USERNAME, project_to_grade)
    if os.access(folder, os.F_OK):
        print('WARNING: SKIPPING', folder, 'because it already exists')
        return False
    success_or_failure = checkout(url, folder)
    return success_or_failure

def get_url(student, project_to_grade):
    """ Returns the URL for the given student's project. """
    repo = COURSE + '-' + TERM + '-' + student + '/' + project_to_grade
    return URL_FOR_SVN_REPOS + repo

def get_solution_url(project_to_grade):
    """ Returns the URL for the solution for the given project. """
    repo = COURSE_REPO_NAME + '/' + ECLIPSE_PROJECTS + '/' + TERM
    solution = project_to_grade + SOLUTION_SUFFIX
    return URL_FOR_SVN_REPOS + repo + '/' + solution

def get_grading_folder(student, project_to_grade):
    """
    Returns the folder into which to checkout
    the given student's project.
    """
    # FIXME: This presumes a folder structure that others might not want.
    #        But at least the structure is encapsulated in this function.
    parent = GRADING_FOLDER + TERM + '/'
    return parent + project_to_grade + '/' + student


def checkout(url, folder):
    """
    Checks out the given URL into the given folder.
    Returns True if the checkout succeeded, else False.
    """
#    FIXME: You need to make Tortoise learn your password somehow.
#    Otherwise, use something like:
#      os.system('svn checkout ' + url + ' ' + folder + ' --username mutchler --password XXX')
#    But note that the latter is a security hazard (see me for details).
    try:
        # FIXME: Figure out how to find if the checkout failed.
        os.system('svn checkout ' + url + ' ' + folder)
    except:
        # FIXME: Figure out whether this detects failures correctly.
        return False
    return True

def fix_all_for_eclipse(project_to_grade, students):
    """
    For each of the given students, renames the project to be the
    student's username.  This allows all the projects to exist in a
    single Eclipse workspace.
    """
    failures = []
    for student in students:
        try:
            folder = get_grading_folder(student, project_to_grade)
            success = fix_for_eclipse(folder, project_to_grade, student)
            if not success:
                failures.append(student)
        except:
            failures.append(student)

    return failures

def fix_for_eclipse(folder, project_to_grade, student):
    """
    Modifies the .project in the given folder
    to rename the project from its name to the given student (username).
    This allows Eclipse to import  multiple students' projects for the
    same assignment (all of which share the same project name before
    running this function).
    Returns True if the fix-for-Eclipse succeeded, else False.
    """
    # FIXME: The following is somewhat brittle and WILL BREAK if
    #        Eclipse changes its project filenames.
    filename = folder + '/.project'
    try:
        with open(filename, 'r') as file:
            file_contents = file.read()

        lines = file_contents.split('\n')
        with open(filename, 'w') as file:
            for line in lines:
                print(re.sub(project_to_grade, student, line), file=file)
    except:
        # FIXME: Figure out whether this detects failures correctly.
        print('Could not open the file:')
        print('   ', filename)
        print('Fix and try again.\n')
        return False

    return True

# Functions below are NOT correct.

def remove_extra(project_to_grade, students):
    """
    Removes all unnecessary information from the projects:
      -- All SVN information
      -- All .docx and .pdf files
    """
    for student in students:
        folder = get_grading_folder(student, project_to_grade)
        remove_extra_in_folder(folder)


def remove_extra_in_folder(folder):
    """
    At the TOP level of the given folder,
    as well as in the   src   subfolder (if it exists),
    removes any of the following that exist:
      *.docx, *.pdf, *.gif
    """
    # FIXME: THIS IS A DANGEROUS FUNCTION.
    #        If the folder is somehow not what is intended,
    #        LOTS of files can be IRREVOCABLY DELETED.

    # Temporary attempt at safety:
    try:
        assert(folder.startswith(GRADING_FOLDER))
    except:
        print('ERROR ERROR ERROR in remove_extra_in_folder')
        raise Exception('Error in remove_extra_in_folder')

    # Here is the dangerous part:
    for file in os.listdir(folder):
        if (file == '.svn'):
            pass  # shutil.rmtree(folder + '/.svn')
        if fnmatch.fnmatch(file, '*.pdf'):
            os.remove(folder + '/' + file)
        if fnmatch.fnmatch(file, '*.docx'):
            os.remove(folder + '/' + file)

    for file in os.listdir(folder + '/src'):
        if fnmatch.fnmatch(file, '*.gif'):
            os.remove(folder + '/src/' + file)

if __name__ == '__main__':
    main()
