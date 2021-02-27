# FIXME: This file needs to be reworked!!!!!!!!!


# TODO: Add a comment here.

class WhatToGrade(object):
    """
    A WhatToGrade specifies the:
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
        return 'WhatToGrade({}, {}, {})'.format(self.course,
                                                self.project,
                                                self.modules)
