# FIXME: This file needs to be reworked!!!!!!!!!

"""
"""
# FIXME: This file needs to be reworked!

# TODO: Put a comment above.

URL_FOR_COURSES = 'http:www.rose-hulman.edu/class/csse/'

# CONSIDER: May need the following to automate getting rosters, etc.
# FOLDER_FOR_ROSTERS = 'Rosters'
# URL_FOR_ROSTERS = URL_FOR_CSSE_HOME + COURSE + '/' + TERM + '/' \
#     + FOLDER_FOR_ROSTERS + '/' + TERM + '/'


# TODO: information other than prefix, number and term
# should come from a lookup on the schedule lookup page.
# Even the term should default to the current term,
# so only 'csse120' is needed.
class Course(object):

    def __init__(self, prefix, number, term,
                 sections,
                 projects=None,
                 course_repo=None,
                 students_repo=None,
                 course_url=None,
                 username_for_solution='solution',
                 username_for_original='original',
                 suffix_for_test_files='_tests'):
        self.prefix = prefix
        self.number = number
        self.term = str(term)
        self.sections = sections
        self.course_name = self.prefix + str(self.number)

        self.projects = projects  # FIXME to look up projects

        self.course_repo = course_repo or (self.course_name + '/trunk/')
        self.students_repo = students_repo or \
            (self.course_name + '-' + self.term)

        self.course_url = course_url or \
            (URL_FOR_COURSES + self.course_name)

        # CONSIDER: I created SVN accounts whose usernames are
        # are 'solution' and 'original'.  These could conflict
        # with a future student, but are highly unlikely to do so.
        self.username_for_solution = username_for_solution
        self.username_for_original = username_for_original

        self.suffix_for_test_files = suffix_for_test_files

    def __repr__(self):
        number_of_parameters = 11

        format_string = 'Course('
        format_string += '{}'
        format_string += (number_of_parameters - 1) * ', {}'
        format_string += ')'

        return format_string.format(self.prefix,
                                    self.number,
                                    self.term,
                                    self.sections,
                                    self.projects,
                                    self.course_repo,
                                    self.students_repo,
                                    self.course_url,
                                    self.username_for_solution,
                                    self.username_for_original,
                                    self.suffix_for_test_files)

    def get_usernames(self, section=None):
        # TODO: Implement this.  No section means all students.
        #       Lookup data up from the web.

        # For now (for testing):
        with open('usernames.txt', 'r') as file:
            return file.read().split()

    def get_modules(self, project_name, include_examples=False):
        """
        Returns a list of all the modules in a project,
        excluding the example modules (unless include_examples is True).
        """
        # TODO: Implement this.  For now (for testing):
        return ['problem1.py']


# Don't forget to change the TERM each term, and the SECTIONS.
# TODO: Automate that.  Also automate finding the project names.
CSSE120 = Course('csse', '120', '201810', ['01', '03', '04'],
                 [None,
                  'Session01_IntroductionToPython',
                  'Session02_InputComputeOutput',
                  'Session03_LoopsAndUsingObjects',
                  'Session04_FunctionsAndAccumulators',
                  '', '', 'Session07_Test1', '', '', '', '', '', '', '',
                  '',
                  'Session16_Test2', '', '', '', '', '',
                  'Session22_Test3', '', '', '', '', '', '', '', '',
                  'Session31_FinalExam',
                  ],
                 'csse120-python/branches/robonew/'
                 )
