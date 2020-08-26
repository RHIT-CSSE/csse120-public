"""
The code for describing a Term, used throughout the ScheduleMaker..
Author: David Mutchler and his colleagues.
"""

from Constants import *
from Parser import Parser
import datetime


class TermInfo:
    """
    Everything the HomePageMaker needs to know about the term,
    except for the learning objectives and HTML formatting.
    """

    def __init__(self, banner_term: str):
        """
        The parameter  banner_term  should be a string like 202110
        (for the fall term of the 2020-21 academic year).
        """
        self.banner_term = banner_term
        filename = TERM_INFO_FILE

        with open(filename, "r") as file_handle:
            self.text = file_handle.read()
        lines = self.text.split("\n")

        # First and last day of term:
        self.first_day_of_term, self.last_day_of_tenth_week = \
            Parser.parse_first_and_last_days_of_term(lines)

        # Days of the week that the class meets:
        self.class_meeting_days_of_week = \
            Parser.parse_class_meeting_days_of_week(lines)

        # Days for break (Fall break, Winter break, Spring break):
        self.start_date_of_break, self.end_date_of_break = \
            Parser.parse_days_for_break(lines)

        # Term (Fall, Winter, Spring), Year (e.g. 2020-21)
        # and Term and Year (e.g. Fall term, 2020-21):
        self.term, self.year, self.term_and_year = \
            self.set_term_and_year(self.first_day_of_term)

    @staticmethod
    def set_term_and_year(first_day_of_term: datetime.date) -> (str, str, str):
        # CONSIDER: Should the things determined here be viewed as formatting
        # and set elsewhere?
        # CONSIDER: Make the following less quarter-specific, perhaps??
        if first_day_of_term.month in [8, 9]:
            term = "Fall"
        elif first_day_of_term.month in [11, 12]:
            term = "Winter"
        elif first_day_of_term.month in [2, 3]:
            term = "Spring"
        else:
            s = "The month  '{}'  is an impossible value" \
                + " for the month that starts a term."
            raise ValueError(s.format(first_day_of_term.month))

        if term == "Spring":
            start = first_day_of_term.year - 1
            end = str(first_day_of_term.year)[2:]
        else:
            start = first_day_of_term.year
            end = str(first_day_of_term.year + 1)[2:]
        year = "{}-{}".format(start, end)

        term_and_year = "{} term, {}".format(term, year)

        return term, year, term_and_year
