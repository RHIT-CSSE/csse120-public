"""
Generates an HTML schedule for CSSE 120 from the list of
learning objectives and relevant information about the term dates.

Author: David Mutchler and his colleagues.
"""

from Constants import *  # All constants, and only constants, are in ALL_CAPS.
from TermInfo import TermInfo
from Session import SessionMaker
import HTMLWriter


class HomePageMaker:
    """ Generates the HTML for the CSSE 120 Home Page for a given term. """

    def __init__(self, banner_term: str):
        """
        The parameter  banner_term  should be a string like 202110
        (for the fall term of the 2020-21 academic year).
        """
        self.term_info = TermInfo(banner_term)
        self.learning_objectives = SessionMaker(SESSION_TITLES_FILENAME)
        self.schedule = HTMLWriter.Schedule(self.term_info,
                                            self.learning_objectives.sessions)
        self.home_page = HomePage(self.term_info, self.schedule)

    def make_html(self) -> str:
        return self.home_page.make_html()

    def write_html_file(self):
        with open(HOME_PAGE, "w") as file_handle:
            file_handle.write(self.make_html())


class HomePage:
    def __init__(self, term_info: TermInfo, schedule: HTMLWriter.Schedule):
        self.term_info = term_info
        self.schedule = schedule
        with open(HOME_PAGE_TEMPLATE, "r") as file_handle:
            self.template = file_handle.read()
        with open(NAVIGATION_BAR_TEMPLATE, "r") as file_handle:
            self.navigation_bar = file_handle.read()
        with open(FOOTER_TEMPLATE, "r") as file_handle:
            self.footer = file_handle.read()

    def make_html(self) -> str:
        return self.template.replace(
            "NAVIGATION_BAR", self.navigation_bar).replace(
            "SCHEDULE", self.schedule.make_html()).replace(
            "FOOTER", self.footer).replace(
            "TERM_AND_YEAR", self.term_info.term_and_year).replace(
            "TERM_PER_BANNER", self.term_info.banner_term)


def main():
    """ Make the HTML for the CSSE 120 HomePage for the indicated term. """
    #     html = gfm.markdown(xx)

    maker = HomePageMaker(TERM)
    html = maker.make_html()
    print(html)
    maker.write_html_file()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
