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
        self.navigation_bar = self.navigation_bar.replace(
            'src="', 'src="../../').replace(
            'href="', 'href="../../').replace(
                "../../http", "http")

        with open(SESSION_SECTION_VIDEOS_READING_TEMPLATE, "r") as file_handle:
            self.videos_reading_template = file_handle.read()
        with open(SESSION_SECTION_QUIZ_TEMPLATE, "r") as file_handle:
            self.quiz_template = file_handle.read()
        with open(SESSION_SECTION_FOLLOW_ME_TEMPLATE, "r") as file_handle:
            self.follow_me_template = file_handle.read()

        with open(FOOTER_TEMPLATE, "r") as file_handle:
            self.footer = file_handle.read()

        with open(SESSION_ITEM_VIDEO_TEMPLATE, "r") as file_handle:
            self.item_video_template = file_handle.read()
        with open(SESSION_ITEM_READING_TEMPLATE, "r") as file_handle:
            self.item_reading_template = file_handle.read()
        with open(SESSION_ITEM_OTHER_TEMPLATE, "r") as file_handle:
            self.item_other_template = file_handle.read()


class SessionPageItem:
    def __init__(self, data: str, templates: SessionTemplates):
        self.data = data
        self.lines = data.split("\n")
        print("Lines:")
        print(self.lines)
        if self.lines[0] == "":  # CONSIDER: fix this more elegantly??
            self.lines = self.lines[1:]
        self.item_type = self.lines[0]
        self.title = self.lines[1]

        self.url = ""
        self.minutes = ""
        self.note = []
        if self.item_type == "VIDEO":
            self.url = self.lines[2]
            self.minutes = self.lines[3]
            note_starts_at = 4
            self.template = templates.item_video_template
        elif self.item_type == "READING":
            self.url = self.lines[2]
            note_starts_at = 3
            self.template = templates.item_reading_template
        elif self.item_type == "OTHER":
            note_starts_at = 2
            self.template = templates.item_other_template
        elif self.item_type == "EXAM":  # FIXME
            note_starts_at = 2  # FIXME
            self.template = templates.item_other_template  # FIXME
        else:
            message = "Bad data in an item for a session page: {}"
            raise ValueError(message.format(data))

        self.note = self.lines[note_starts_at:]

    def make_html(self):
        note_string = self.make_html_for_note()
        html = self.template.replace(
            "__TITLE__", self.title).replace(
            "__URL__", self.url).replace(
            "__MINUTES__", self.minutes).replace(
            "__NOTE__", note_string)

        lines = html.split("\n")
        html = ""
        for line in lines:
            html += "      " + line + "\n"

        return html

    def make_html_for_note(self) -> str:
        note_string = ""
        inside_note = False
        for line in self.note:
            if line == "":
                if inside_note:
                    note_string += "    </li>\n"
                    inside_note = False
                else:
                    pass  # Extra blank line, ignore it
            else:
                if not inside_note:
                    inside_note = True
                    note_string += "    <li>\n"
                note_string += "      " + line + "\n"
        # if inside_note:
        #     note_string += "      </ul>\n"
        return note_string


class SessionSection:
    def __init__(self, data: str, templates: SessionTemplates,
                 section_type: SessionSectionType):
        self.data = data
        self.templates = templates
        self.section_type = section_type
        if not data:
            self.raw_items = []
        else:
            self.raw_items = self.data.split("---")
        self.items = []
        for k in range(len(self.raw_items)):
            if self.raw_items[k].replace("\n", "") == "":  # Just empty lines
                continue
            self.items.append(SessionPageItem(self.raw_items[k],
                                              self.templates))

    def make_html(self) -> str:
        """ Returns the HTML for this SessionSection on a Session page. """
        if self.section_type == SessionSectionType.VIDEOS_READING:
            template = self.templates.videos_reading_template
        elif self.section_type == SessionSectionType.QUIZ:
            template = self.templates.quiz_template
        elif self.section_type == SessionSectionType.FOLLOW_ME:
            template = self.templates.follow_me_template
        else:
            raise ValueError("Bad SessionSectionType: {}".format(
                self.section_type))

        html = ""
        for item in self.items:
            html = html + item.make_html()  # FIXME to add spaces

        return template.replace("      __SESSION_SECTION_ITEMS__", html)  #
        # FIXME


class SessionPage:
    def __init__(self, session_number: int,
                 term_info: TermInfo,
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

        processed_lines = []
        for filename in (SESSION_VIDEOS_READING_FILENAME,
                         SESSION_QUIZ_FILENAME,
                         SESSION_FOLLOW_ME_FILENAME):
            full_filename = "{}/{}".format(self.session_folder, filename)
            with open(full_filename, "r") as file_handle:
                lines = file_handle.readlines()
            processed_lines.append(
                self.strip_comments(self.handle_line_continuations(lines)))

        self.videos_reading_data = "".join(processed_lines[0])
        self.quiz_data = "".join(processed_lines[1])
        self.follow_me_data = "".join(processed_lines[2])

        self.videos_reading = SessionSection(self.videos_reading_data,
                                             self.templates,
                                             SessionSectionType.VIDEOS_READING)
        self.quiz = SessionSection(self.quiz_data,
                                   self.templates,
                                   SessionSectionType.QUIZ)
        self.follow_me = SessionSection(self.follow_me_data,
                                        self.templates,
                                        SessionSectionType.FOLLOW_ME)

    @staticmethod
    def strip_comments(lines: List[str]) -> List[str]:
        non_comment_lines = []
        for line in lines:
            if len(line) > 0 and line[0] == "#":
                continue
            non_comment_lines.append(line)
        return non_comment_lines

    @staticmethod
    def handle_line_continuations(lines: List[str]) -> List[str]:
        print("lines =", lines)
        lines_after_continuations = []
        in_continuation = False
        continuation_line = ""
        for line in lines:
            if in_continuation:
                continuation_line = continuation_line + line
                print("in continuation:", continuation_line)
            else:
                continuation_line = line
            in_continuation = (len(continuation_line) > 1
                               and continuation_line[-2] == "\\")
            if in_continuation:
                continuation_line = continuation_line[:-2]
                print("in continuation again:", continuation_line)
            else:
                lines_after_continuations.append(continuation_line)
        # Assumes that the last line does NOT end with \
        return lines_after_continuations

    def make_html(self) -> str:
        videos_reading = self.videos_reading.make_html()
        quiz = self.quiz.make_html()
        follow_me = self.follow_me.make_html()

        return self.templates.session_template.replace(
            "__NAVIGATION_BAR__", self.templates.navigation_bar).replace(
            "__VIDEOS_READING_SECTION__", videos_reading).replace(
            "__QUIZ_SECTION__", quiz).replace(
            "__FOLLOW_ME_SECTION__", follow_me).replace(
            "__FOOTER__", self.templates.footer).replace(
            "TERM_AND_YEAR", self.term_info.term_and_year).replace(
            "TERM_PER_BANNER", self.term_info.banner_term).replace(
            "__PIAZZA_URL__", self.term_info.piazza_url).replace(
            "__QUIZ_NUMBER__", self.session_number_string).replace(
            "__SESSION_NUMBER__", str(self.session_number)).replace(
            "../../http", "http")


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
        print(session_page)
        print(session_page.make_html())

    def write_html_files(self):
        for k in range(NUMBER_OF_SESSIONS):
            session_page = self.session_pages[k]
            print("Writing {}".format(session_page.filename))
            with open(session_page.filename, "w") as file_handle:
                file_handle.write(session_page.make_html())


def main():
    """ Make the HTML for the CSSE 120 HomePage for the indicated term. """
    maker = SessionPagesMaker(TERM)
    maker.write_html_files()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
