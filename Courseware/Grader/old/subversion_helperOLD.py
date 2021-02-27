"""
Functions to get student projects for CSSE 120 (or other courses)
from SVN and to prepare them to be graded.

Authors: David Mutchler, Chandan Rupakheti, Amanda Stouder,
         and their colleagues, December 2013.
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

COURSE = 'csse120'
TERM = '201420'
SECTIONS = ('01', '02', '03', '04',)
REPO = COURSE + '-' + TERM
PROJECTS = [None,
            'Session01_IntroductionToPython',
            'Session02_InputComputeOutput',
            'Session03_LoopsAndUsingObjects',
            'Session04_FunctionsAndAccumulators',
            ]

URL_FOR_SVN_REPOS = 'http://svn.csse.rose-hulman.edu/repos/'
URL_FOR_CSSE_HOME = 'http://www.rose-hulman.edu/class/csse/'
FOLDER_FOR_ROSTERS = 'Rosters'
URL_FOR_ROSTERS = URL_FOR_CSSE_HOME + COURSE + '/' + TERM + '/' + FOLDER_FOR_ROSTERS + '/' + TERM + '/'


def main():
    start()


def start():
    project = PROJECTS[4]
    
    # SECTIONS Sequence defined above
    students = get_usernames_from_rosters(['01', '02', '03', '04'])
    #    students = get_usernames_from_rosters(SECTIONS)

    checkout_all(project, students)
    fix_for_eclipse(project, students)


def get_usernames_from_rosters(groups, roster_folder=URL_FOR_ROSTERS):
    """
    Returns a list of usernames that are members of the given sequence
    of groups.  The usernames must be stored in text files that
    are in the appropriate place.
    """
    usernames = []
    url_prefix = roster_folder + COURSE + '-' + TERM + '-'
    for group in groups:
        print(group)
        url = url_prefix + group + '.txt'
        usernames_as_byte_array = urllib.request.urlopen(url).read()
        usernames_in_group = usernames_as_byte_array.decode().split()
        usernames.extend(usernames_in_group)

    return usernames


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
        if not checkout(url, folder):
            failures.append(student)

    return failures


def get_url(student, project_to_grade):
    """ Returns the URL for the given student's project. """
    repo = COURSE + '-' + TERM + '-' + student + '/' + project_to_grade
    return URL_FOR_SVN_REPOS + repo


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
    os.system('svn checkout ' + url + ' ' + folder)

    #    FIXME: Need to figure out how to detect failures.
    return True


def fix_for_eclipse(project_to_grade, students):
    """
    For each of the given students, renames the project to be the
    student's username.  This allows all the projects to exist in a
    single Eclipse workspace.
    """
    for student in students:
        folder = get_grading_folder(student, project_to_grade)
        fix_project_for_eclipse(folder, project_to_grade, student)

def fix_project_for_eclipse(folder, project_to_grade, student):
    """
    Modifies the .project in the given folder
    to rename the project from its name to the given student (username).
    This allows Eclipse to import  multiple students' projects for the
    same assignment (all of which share the same project name before
    running this function).
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
        print('Could not open the file:')
        print('   ', filename)
        print('Fix and try again.\n')
        raise

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
    # FIXME: THIS IS A DANGEROUS FUNCTION.  If the folder is somehow
    #        not what is intended, lots can be wiped out.
    for file in os.listdir(folder):
        if (file == '.svn'):
            shutil.rmtree(folder + '/.svn')
        if fnmatch.fnmatch(file, '*.pdf'):
            os.remove(folder + '/' + file)
        if fnmatch.fnmatch(file, '*.docx'):
            os.remove(folder + '/' + file)


if __name__ == '__main__':
    main()

