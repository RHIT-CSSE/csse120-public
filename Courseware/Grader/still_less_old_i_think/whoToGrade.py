# FIXME: This file needs to be reworked!!!!!!!!!


class WhoToGrade(object):
    """ Specifies the usernames to be graded. """

    # CONSIDER: The following does not feel Pythonic to me.
    # Not sure exactly why.
    def __init__(self, who_to_grade=None, course=None):
        """
        If  who_to_grade  is:
          -- None or empty list: Grade all students in the course.
          -- An integer:         Grade all students in that section.
          -- Sequence:           Grade all students listed.
          -- Filename (string):  Grade all students listed in that file.

        :type who_to_grade: (list, tuple, int)
        :type course: Course
        """
        # CONSIDER: Allow other types for  who_to_grade  ???
        # CONSIDER: Allow GROUP names in the sequence or file?

        self.who_to_grade = who_to_grade
        self.course = course

        if not self.who_to_grade:
            # None or empty list - grade all the students
            self.students = course.get_usernames()
        else:
            try:
                # integer - grade all students in that section
                self.students = course.get_usernames(who_to_grade)
            except:
                try:
                    # filename - grade all students in that file
                    with open(who_to_grade, 'r') as file:
                        self.students = file.read().split()
                except:
                    # who_to_grade is a sequence of students to grade
                    self.students = who_to_grade


class StandardWhoToGrade(WhoToGrade):
    """ All the students in the course. """

    def __init__(self, course):
        super().__init__(None, course)
