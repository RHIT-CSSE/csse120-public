"""
Generates an HTML file for each Session of CSSE 120.
The file contains instructions for students to do:
  -- Preparation Videos and Reading and associated Quizzes in Moodle
  -- A Start-the-Session quiz (and self-check answers and turn it in in Moodle)
  -- Follow-Me videos

Author: David Mutchler and his colleagues.
"""

from Constants import *  # All constants, and only constants, are in ALL_CAPS.
from TermInfo import TermInfo
from typing import List


class SessionTemplates:
    def __init__(self):
        with open(SESSION_TEMPLATE, "r") as file_handle:
            self.session_template = file_handle.read()
        with open(NAVIGATION_BAR_TEMPLATE, "r") as file_handle:
            self.navigation_bar = file_handle.read()
        with open(FOOTER_TEMPLATE, "r") as file_handle:
            self.footer = file_handle.read()

        with open(SESSION_VIDEO_TEMPLATE, "r") as file_handle:
            self.video_template = file_handle.read()
        with open(SESSION_READING_TEMPLATE, "r") as file_handle:
            self.reading_template = file_handle.read()
        with open(SESSION_FOLLOW_ME_TEMPLATE, "r") as file_handle:
            self.follow_me_template = file_handle.read()
        with open(SESSION_OTHER_ITEM_TEMPLATE, "r") as file_handle:
            self.other_item_template = file_handle.read()


class SessionPage:
    def __init__(self, session_number: int, term_info: TermInfo,
                 session_templates: SessionTemplates):
        self.session_number = session_number
        self.term_info = term_info
        self.templates = session_templates

        if self.session_number < 10:
            self.session_number_string = "0{}".format(session_number)
        else:
            self.session_number_string = "{}".format(session_number)

        self.session_folder = "{}/Session{}".format(
            SESSIONS_FOLDER, self.session_number_string)
        self.filename = "{}/index.html".format(self.session_folder)

        session_preparation_filename = "{}/{}".format(
            self.session_folder, SESSION_PREPARATION_FILENAME)
        session_follow_me_filename = "{}/{}".format(
            self.session_folder, SESSION_FOLLOW_ME_FILENAME)

        with open(session_preparation_filename, "r") as file_handle:
            self.preparation_data = file_handle.read()
        with open(session_follow_me_filename, "r") as file_handle:
            self.follow_me_data = file_handle.read()

    def make_html(self) -> str:
        if self.session_number > 1:  # FIXME
            return ""

        preparation = self.make_preparation()
        follow_me = self.make_follow_me()
        return self.templates.session_template.replace(
            "__NAVIGATION_BAR__", self.templates.navigation_bar).replace(
            'src="', 'src="../../').replace(
            'href="', 'href="../../').replace(
            " __PREPARATION_VIDEOS_AND_READING__", preparation).replace(
            " __FOLLOW_ME_VIDEOS__", follow_me).replace(
            "__FOOTER__", self.templates.footer).replace(
            "TERM_AND_YEAR", self.term_info.term_and_year).replace(
            "TERM_PER_BANNER", self.term_info.banner_term).replace(
            "__QUIZ_NUMBER__", self.session_number_string).replace(
            "__SESSION_NUMBER__", str(self.session_number))

    def make_preparation(self) -> str:
        if not self.preparation_data:
            return ""
        preparation_items = self.preparation_data.split("\n\n")
        for k in range(len(preparation_items)):
            preparation_items[k] = preparation_items[k].split("\n")
            if preparation_items[k][0] == "":
                preparation_items[k] = preparation_items[k][1:]

        html = ""
        for preparation_item in preparation_items:
            html += self.make_preparation_item_html(preparation_item)
        return html

    def make_preparation_item_html(self, preparation_item):
        # Read the data.
        # For each data item:
        #   Identify its type.
        #   Replace its template items with their values.
        # return the accumulated result.
        print(self.session_number, preparation_item)
        item_type = preparation_item[0]
        if item_type == "VIDEO" or item_type == "READING":
            return self.make_video_reading_item(item_type,
                                                preparation_item[1:])
        elif item_type == "EXAM":  # FIXME
            return ""
        elif item_type == "OTHER":
            return self.make_other_item(preparation_item[1:])
        else:
            raise ValueError("Bad data in {}".format(preparation_item))

    def make_video_reading_item(self, item_type: str, data: List[str]) -> str:
        title = data[0]
        url = data[1]
        minutes = data[2]
        note = ""
        for k in range(3, len(data)):
            if k == 3:
                note += data[k] + "\n"
            else:
                note += "            " + data[k] + "\n"
        if item_type == "VIDEO":
            template = self.templates.video_template
        else:
            template = self.templates.reading_template

        html = template.replace(
            "__TITLE__", title).replace(
            "__URL__", url).replace(
            "__MINUTES__", minutes).replace(
            "__NOTE__", note)  # FIXME: leaves an extra <p></p>
        return html

    def make_other_item(self, data: List[str]) -> str:
        template = self.templates.other_item_template
        note = ""
        for k in range(len(data)):
            if k == 0:
                note += data[k] + "\n"
            else:
                note += "          " + data[k] + "\n"
        return template.replace("__ITEM__", note)

    def make_follow_me(self) -> str:
        # follow_me_data = self.follow_me_data.split("\n\n")
        # print(follow_me_data)
        return ""
        # Read the data.
        # For each data item:
        #   Identify its type.
        #   Replace its template items with their values.
        # return the accumulated result.


class SessionPagesMaker:
    """ Generates the HTML for a CSSE 120 Session. """
    def __init__(self, banner_term: str):
        """
        The parameter  banner_term  should be a string like 202110
        (for the fall term of the 2020-21 academic year).
        """
        self.term_info = TermInfo(banner_term)
        self.templates = SessionTemplates()

        self.session_pages = []
        for k in range(NUMBER_OF_SESSIONS):
            session_page = SessionPage(k + 1, self.term_info, self.templates)
            self.session_pages.append(session_page)

    def print_html(self, session_index: int):
        session_page = self.session_pages[session_index]
        print(session_page.make_html())

    def write_html_files(self):
        for k in range(NUMBER_OF_SESSIONS):
            session_page = self.session_pages[k]
            print("Writing {}".format(session_page.filename))
            with open(session_page.filename, "w") as file_handle:
                file_handle.write(session_page.make_html())


def main():
    """ Make the HTML for the CSSE 120 HomePage for the indicated term. """
    #     html = gfm.markdown(xx)

    maker = SessionPagesMaker(TERM)
    maker.print_html(0)
    maker.write_html_files()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
