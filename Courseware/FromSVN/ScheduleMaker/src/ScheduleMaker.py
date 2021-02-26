"""
Generates an HTML schedule for CSSE 120 from the list of
learning objectives and relevant information about the term dates.

Requires (via pip):  gfm bs4 htmllib

Author: David Mutchler and his colleagues.
"""

import datetime
import string
import re
import abc
import gfm
import bs4  # BeautifulSoup
import enum


COMMENT_BEGIN_INDICATOR = "!!! BEGIN COMMENT"
COMMEND_END_INDICATOR = "!!! END COMMENT"
COMMENT_INDICATOR = "!!!"
SESSION_INDICATOR = r'^.*Session[ ]*[0-9]*:'
EXAM_INDICATOR = r'Exam '

EVENING_EXAM_TEMPLATE = string.Template("""
      <div class=evening_exam>
        <p>
          The regular in-class session on $REGULAR_DAY
          is an OPTIONAL review session.
          The test itself is
            <span class=exam_date_time>
              $EXAM_DAY
              evening from 7:30 p.m. to 9:30 p.m.
              (with an additional 30-minute grace period)
            </span>
            <span class=exam_rooms> in rooms TBA.</span>
        </p>
      </div>
      """)

SHOW_TOPICS = False


@enum.unique
class SessionType(enum.Enum):
    REGULAR = 1
    NO_CLASS = 2
    EVENING_EXAM = 3
    IN_CLASS_EXAM = 4
    PROJECT = 5
    OTHER = 6


# The following really are defined, but PyDev does not think so, apparently.
RE_MULTILINE = re.MULTILINE  # @UndefinedVariable
RE_DOTALL = re.DOTALL  # @UndefinedVariable


class TermInfo(object):
    """
    Everything the ScheduleMaker needs to know about the term,
    except for the learning objectives.
    """

    def __init__(self, term):
        """ term is a string that identifies the term, e.g. 201720 """
        # FIXME: Some of this does not belong in TERM information.
        # TODO: Get the following from a file(s) instead of like this:
        self.term = term
        self.start_date = datetime.date(2017, 8, 28)
        self.end_date = datetime.date(2017, 11, 9)
        self.days_of_week = [1, 3, 4]  # isoweekday: Monday is 1, Sunday is 7
        self.weekdays_of_week = ['Monday', 'Wednesday', 'Thursday']
        self.dates_to_skip = [ScheduleDate(2017, 8, 28, "No class"),
                              ScheduleDate(2017, 8, 30, "No class"),
                              ScheduleDate(2017, 10, 12, "Fall break")
                              ]
        exam1_msg = EVENING_EXAM_TEMPLATE.substitute(REGULAR_DAY='Thursday',
                                                     EXAM_DAY='Thursday')
        exam2_msg = exam1_msg
        self.evening_exams = [ScheduleDate(2017, 9, 14, exam1_msg),
                              ScheduleDate(2017, 10, 5, exam2_msg)]
        self.start_session_number = 1

        csse120_folder = "/Users/david/classes/120/"
        term_folder = csse120_folder + 'Public/' + self.term + '/'

        le_folder = term_folder + 'LearningObjectives/'
        le_file = 'LearningObjectives.txt'
        self.learning_objectives_filename = le_folder + le_file

        st_folder = term_folder
        st_file = 'index.html'  # EVENTUALLY RETURN to:  schedule_table.html
        self.schedule_table_filename = st_folder + st_file

        self.number_of_sessions = 30


class ScheduleDate(object):
    def __init__(self, year, day, month, message=None):
        self.datetime_date = datetime.date(year, day, month)
        self.message = message

    def __repr__(self):
        return '{} {}'.format(self.datetime_date, self.message)

    def __eq__(self, date):
        # Date may be a ScheduleDate or it may be a datetime.date.
        try:
            return (self.datetime_date == date.datetime_date
                    and self.message == date.message)
        except AttributeError:
            return self.datetime_date == date


class ScheduleMaker(object):
    """
    Generates an HTML schedule for CSSE 120 from the list of
    learning objectives and relevant information about the term dates.
    """
    def __init__(self, term_info):
        """
        Given a file of Learning Objectives and information about the
        current term, makes an HTML file for the Schedule Page.
          :type term_info: TermInfo
        """
        self.term_info = term_info
        self.raw_data = None
        self.topics_by_session = None

    def make_schedule(self):
        # Get the data from the Learning Objectives file:
        self.get_raw_data()

        # Parse the Learning Objectives file to get a list of ClassSession
        # objects, one per session, with each ClassSession object having
        # a title and GFM topics:
        self.split_into_sessions()

        # Go through the list of sessions, adding dates, session numbers,
        # and (where needed) NoClassSession objects:
        self.add_dates_numbers_and_NoClassSessions()

        # Make the HTML for each session:
        for session in self.sessions:
            session.make_html()

        # Make and prettify the entire table of sessions.
        self.make_html_table()
        # Prettify here?? Or just per session???

        self.write_html(self.html)

    def get_raw_data(self):
        with open(self.term_info.learning_objectives_filename, 'r') as file:
            self.raw_data = file.read()

    def split_into_sessions(self):
        """
        Parses the raw data to make a list of ClassSession objects.
        The object will NOT yet have a correct Session Number or Date.
        """
        # FIXME: The above comment is no longer completely accurate.

        # Strip comments from the raw data:
        data = self.strip_comments()

        # Split the data by sessions:
        self.topics_by_session = re.split(SESSION_INDICATOR, data,
                                          flags=RE_MULTILINE)
        self.topics_by_session = self.topics_by_session[1:]  # Ignore 1st item

        # Confirm that the number of topics matches the number of sessions.
        try:
            assert(len(self.topics_by_session)
                   == self.term_info.number_of_sessions)
        except AssertionError:
            raise AssertionError("Number of topics != number of sessions")

        # Make the ClassSession objects.  No dates or session numbers yet.
        self.sessions = []
        for k in range(len(self.topics_by_session)):
            lines = self.topics_by_session[k].split('\n')

            # Title is first line (which was on the same line as SessionXX.
            title = lines[0]

            # Rest are the topics for that session, in GFM.
            topics = '\n'.join(lines[1:])
            self.topics_by_session[k] = topics
            session = ClassSession(title=title, topics=topics)
            self.sessions.append(session)

    def strip_comments(self):
        # Parse by lines.
        lines = self.raw_data.split('\n')

        # Remove lines between a COMMENT_BEGIN_INDICATOR
        # and the next COMMENT_END_INDICATOR, then any with COMMENT_INDICATOR.
        i_am_inside_a_comment = False
        lines_to_keep = []
        for line in lines:
            if i_am_inside_a_comment:
                if COMMEND_END_INDICATOR in line:
                    i_am_inside_a_comment = False
            else:
                if COMMENT_BEGIN_INDICATOR in line:
                    i_am_inside_a_comment = True
                elif COMMENT_INDICATOR not in line:
                    lines_to_keep.append(line)

        return '\n'.join(lines_to_keep)

    def add_dates_numbers_and_NoClassSessions(self):
        date = self.term_info.start_date

        session_number = self.term_info.start_session_number
        session_index = 0
        while True:
            # Go through each date from the start of term to end of term.

            # Done when we get to the last date of the term.
            if date > self.term_info.end_date:
                break

            # Deal only with dates that are on class days-of-week.
            if date.isoweekday() in self.term_info.days_of_week:
                if date in self.term_info.dates_to_skip:
                    # Make a NoClassSession
                    index = self.term_info.dates_to_skip.index(date)
                    schedule_date = self.term_info.dates_to_skip[index]

                    session = NoClassSession(schedule_date)
                    self.sessions.insert(session_index, session)
                else:
                    # Add date and session number to this session.
                    session = self.sessions[session_index]
                    session.datetime_date = date

                    session.session_number = session_number
                    session_number = session_number + 1

                    if date in self.term_info.evening_exams:
                        evening_exams = self.term_info.evening_exams
                        session.session_type = SessionType.EVENING_EXAM
                        index = evening_exams.index(date)
                        session.message = evening_exams[index].message

                session_index = session_index + 1
            date = date + datetime.timedelta(1)

    def make_html_table(self):
        """
        Sets self.html to the HTML for the schedule page,
        based on the (previously computed) HTML for the self.sessions
        """
        days_in_week = len(self.term_info.days_of_week)
        sessions_html = ''
        for k in range(len(self.sessions)):
            if k % days_in_week == 0:
                sessions_html += ScheduleTable.ROW_START

            sessions_html += (ScheduleTable.ITEM_START
                              + self.sessions[k].html
                              + ScheduleTable.ITEM_END)

            if k % days_in_week == days_in_week - 1:
                sessions_html += ScheduleTable.ROW_END

        self.html = (ScheduleHeader(self.term_info.weekdays_of_week).html
                     + sessions_html
                     + ScheduleTrailer().html)

    def write_html(self, html):
        with open(self.term_info.schedule_table_filename, 'w') as file:
            file.write(html)

#     def add_topics_and_html_to_sessions(self, topics_by_session, sessions):
#         k = 0
#         for session in sessions:
#             if isinstance(session, NoClassSession):
#                 continue
#             session.topics = topics_by_session[k]
#             session.topics_html = self.make_html_from_topics(session.topics)
#             k = k + 1

    def make_html_from_topics(self, topics_for_session):
        # Make the session title become a top-level list item,
        # and increase the indentation of all subsequent lines.
        topics_for_session = topics_for_session.replace('\n',
                                                        '\n    ')
        topics_for_session = '+ ' + topics_for_session
#         print(topics_for_session)

        # Convert each topic to HTML using Github Flavored Markdown.
        html = gfm.markdown(topics_for_session)
#         print(html)

        # Add class info to the HTML for topics, tests, and sprints.
        # The following is brittle.
        ul_class = 'topics collapsibleList'
        li_class = 'topic'
        if re.match(r'.*Test [0-9]\..*', html, RE_DOTALL):
            ul_class += ' exam'
            li_class += ' exam'
        elif re.match(r'.*Sprint [0-9].*', html, RE_DOTALL):
            ul_class += ' sprint'
            li_class += ' sprint'

        # CONSIDER: the following adds the class to the FIRST <ul>
        # but to ALL <li>'s.  Is that what we want for sub-lists?
        html = html.replace('<ul>',
                            '<ul class="' + ul_class + '">',
                            1)
        html = html.replace('<li>',
                            '<li class="' + li_class + '">')

        # Add details for Tests.
        for_tests = ExamTopic.EVENING_EXAM_TEMPLATE.substitute()
        html = re.sub(r'(Test [0-9]\.)', r'\1' + for_tests, html)

        # Parenthetical expressions are additional markup:
        DOUBLE_OPEN_PARENTHESES = '!!!START_CANNOT_OCCUR_I_HOPE!!!'
        DOUBLE_CLOSE_PARENTHESES = '!!!END_CANNOT_OCCUR_I_HOPE!!!'
        html = html.replace('((', DOUBLE_OPEN_PARENTHESES)
        html = html.replace('))', DOUBLE_CLOSE_PARENTHESES)
        html = html.replace('(', '<span class=parenthetical>(')
        html = html.replace(')', ')</span>')
        html = html.replace('</span>.', '.</span>')
        html = html.replace(DOUBLE_OPEN_PARENTHESES, '(')
        html = html.replace(DOUBLE_CLOSE_PARENTHESES, ')')

        pretty_html = bs4.BeautifulSoup(html, "html.parser").prettify()

        lines = pretty_html.split('\n')
        for k in range(len(lines)):
            lines[k] = re.sub(r'^( *)', r'\1\1', lines[k])

        final_html = '\n'.join(lines)
        # TODO: Deal with punctuation after a tag end.

        return final_html


def prettify(markup):
    soup = bs4.BeautifulSoup(markup, "html5lib")
    return soup.prettify()


class Session(abc.ABC):
    """ Data associated with a single Session. """

    def __init__(self, datetime_date=None, title=None, session_number=None,
                 topics=None, session_type=None, message=None):

        self.datetime_date = datetime_date
        self.title = title
        self.session_number = session_number
        self.topics = topics
        self.session_type = session_type
        self.message = None

    @abc.abstractmethod
    def make_html(self):
        """ Returns the HTML for this Session. """
        # Subclasses must implement this method.

    def __repr__(self):
        return '{} {}'.format(self.datetime_date, self.session_number)

    def date_as_string(self):
        return (self.datetime_date.strftime('%B')
                + ' ' + str(self.datetime_date.day))


class NoClassSession(Session):
    NO_CLASS_TEMPLATE = string.Template("""
        <div class="no_class_title">$SessionTitle</div>
        <div class="session_date">$SessionDate</div>""")

    def __init__(self, schedule_date):
        # TODO maybe should set the session type here too.
        super().__init__(schedule_date.datetime_date, schedule_date.message,
                         session_type=SessionType.NO_CLASS)

    def make_html(self):
        self.html = NoClassSession.NO_CLASS_TEMPLATE.substitute(
            SessionTitle=self.title,
            SessionDate=self.date_as_string())


class ClassSession(Session):
    SESSION_TEMPLATE = string.Template("""
        <div class=session_identifier>
          <span class="session_preparation">$SessionPreparationLink</span>
          <span class="for_session">for session</span>
          <span class="session_number">$SessionNumber</span>
          <span class="session_date">($SessionDate)</span>
        </div>
        <div class="session_title"> $SessionTitle </div>
        """)
    SESSION_TOPICS_TEMPLATE = string.Template("""
        <div class=session_topics>$SessionTopics
        </div>""")

    TOPICS_INDENT = "              "
    LINK_TO_PREP = ('<a href="Sessions/Session{:02}/index.html">'
                    + 'Preparation</a>')

    def __init__(self, title, topics):
        session_type = self.find_session_type(topics)
        super().__init__(title=title, topics=topics, session_type=session_type)

    def make_html(self):
        self.preparation_link = ClassSession.LINK_TO_PREP.format(
            self.session_number)

        title = gfm.markdown(self.title.replace('/', '<br>\n'))

        print('Title:' + title)
        self.html = ClassSession.SESSION_TEMPLATE.substitute(
            SessionPreparationLink=self.preparation_link,
            SessionNumber=self.session_number,
            SessionDate=self.date_as_string(),
            SessionTitle=title)

        if self.session_type == SessionType.EVENING_EXAM:
            self.add_exam_info()

        if SHOW_TOPICS and self.topics.strip():
            self.make_topics_html()
            self.html += ClassSession.SESSION_TOPICS_TEMPLATE.substitute(
                SessionTopics=self.topics_html)

    def add_exam_info(self):
        self.html += self.message

    def make_topics_html(self):
        """
        Generate the HTML for the topics for this Session
        from the topics as a string written in Git-Flavored Markdown,
        along with the previously-determined type of this Session:
          -- Exam, Sprint, or Regular
        """
        # Start with the topics:
        self.topics_html = gfm.markdown(self.topics)


#         topics_for_GFM = self.topics

        # Add text (in HTML) for special sessions, e.g. Tests.
#         for_tests = ExamTopic.EVENING_EXAM_TEMPLATE.substitute(
#             RegularClassDay=self.date.strftime('%A'),
#             ExamDay=(self.date + datetime.timedelta(1)).strftime('%A'))
#
#         topics_for_GFM = re.sub(r'(Test [0-9]\.)', r'\1' + for_tests,
#                                 topics_for_GFM)

        # Prepare for GFM -> HTML:
        #  -- Isolate the Session Title.
        #  -- Add markup for parenthetical expressions
        #  -- TODO: Anything else here?
        # Then generate the HTML from GFM.
#         topics_for_GFM = topics_for_GFM.replace('\n', '\n\n', 1)

#         topics_for_GFM = re.sub(r'([^(]\([^(])',
#                                 '<span class=parenthetical>' + r'\1',
#                                 topics_for_GFM)
#         topics_for_GFM = re.sub(r'([^)]\)[^)])',
#                                 r'\1' + '</span>',
#                                 topics_for_GFM)
#         topics_for_GFM = topics_for_GFM.replace(
#             '((', '(').replace('))', ')')

#         DOUBLE_OPEN_PARENTHESES = '!!!START_CANNOT_OCCUR_I_HOPE!!!'
#         DOUBLE_CLOSE_PARENTHESES = '!!!END_CANNOT_OCCUR_I_HOPE!!!'
#         html = html.replace('((', DOUBLE_OPEN_PARENTHESES)
#         html = html.replace('))', DOUBLE_CLOSE_PARENTHESES)
#         html = html.replace('(', '<span class=parenthetical>(')
#         html = html.replace(')', ')</span>')
#         html = html.replace('</span>.', '.</span>')
#         html = html.replace(DOUBLE_OPEN_PARENTHESES, '(')
#         html = html.replace(DOUBLE_CLOSE_PARENTHESES, ')')


        # Format the html, then return it.
#         pretty_html = bs4.BeautifulSoup(html, "html.parser").prettify()
#
#         lines = pretty_html.split('\n')
#         for k in range(len(lines)):
#             lines[k] = re.sub(r'^( *)', r'\1\1', lines[k])
#
#         final_html = '\n'.join(lines)

        # TODO: Deal with punctuation after a tag end.

        # Add class info to the HTML for topics, tests, and sprints.
        # The following is brittle.
#         ul_class = 'topics collapsibleList'
#         li_class = 'topic'
#         if re.match(r'.*Test [0-9]\..*', html, re.DOTALL):
#             ul_class += ' exam'
#             li_class += ' exam'
#         elif re.match(r'.*Sprint [0-9].*', html, re.DOTALL):
#             ul_class += ' sprint'
#             li_class += ' sprint'

        # CONSIDER: the following adds the class to the FIRST <ul>
        # but to ALL <li>'s.  Is that what we want for sub-lists?
#         html = html.replace('<ul>',
#                             '<ul class="' + ul_class + '">',
#                             1)
#         html = html.replace('<li>',
#                             '<li class="' + li_class + '">')

        # Add details for Tests.

    def find_session_type(self, topics):
        pass


class ScheduleHeader(object):
    """ Data associated with the Schedule as a whole """
    HEADER_TEMPLATE = string.Template("""\
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" \
href="http://fonts.googleapis.com/css?family=Open+Sans">
    <link rel="stylesheet" type="text/css" href="styles/style.css">
    <link rel="stylesheet" type="text/css" href="styles/navigation_bar.css">
    <link rel="stylesheet" type="text/css" href="styles/home_page.css">
    <link rel="stylesheet" type="text/css" href="styles/schedule_page.css">

    <title> CSSE 120 Home Page </title>
</head>

<body>

<nav>
  <img src="../Images/girls_who_code2_90x60.png" alt="Girls coding together"/>
  <div>
    <p>
      <span class="course_number"> CSSE 120</span>
      <br>
      <span class="course_title">Introduction to Software Development</span>
      <br>
      <span class="course_term">Fall term, 2017-18 (aka 201810)</span>
    </p>
  </div>
  <a href="Syllabus_CourseInformation/syllabus.html">SYLLABUS</a>
  <a href="Resources/CSSE120_Setup">SETUP</a>
  <a href="../Resources/Piazza">PIAZZA (Q&A)</a>
  <a href="../Resources/Python">PYTHON</a>
  <a href="../Resources/Graphics">GRAPHICS</a>
  <a href="../Resources/Robotics">ROBOTICS</a>
</nav>

<section class="course_schedule">
<table>
  <caption>What to do, When</caption>
  <thead>
    <tr>${THs_FOR_CLASSDAYS}
    </tr>
  </thead>
  <tbody>""")

    GOOGLE_FONT = "http://fonts.googleapis.com/css?family=Open+Sans"
    TH_FOR_DAY_OF_WEEK_TEMPLATE = string.Template("""
      <th class=schedule_caption> $DAY </th>""")

    def __init__(self, weekdays_of_week):
        TH_template = ScheduleHeader.TH_FOR_DAY_OF_WEEK_TEMPLATE
        THs = ''
        for weekday in weekdays_of_week:
            THs += TH_template.substitute(DAY=weekday)

        t = ScheduleHeader.HEADER_TEMPLATE

        self.html = t.substitute(GOOGLE_FONT=ScheduleHeader.GOOGLE_FONT,
                                 THs_FOR_CLASSDAYS=THs)


class ScheduleTable(object):
    ROW_START = """
    <tr>"""

    ROW_END = """
    </tr>"""

    ITEM_START = """

      <td>"""

    ITEM_END = """
      </td>"""


class ScheduleTrailer(object):
    TRAILER = """
</table>
</section>
</body>
</html>"""

    FINAL_EXAM = """
  </tbody>
  <tfoot>
    <tr>
      <th colspan=3>
    PROJECT DEMOs and FINAL EXAM during exam week, times TBD.
     </th>
     </tr>
  </tfoot>"""

    def __init__(self):
        self.html = ScheduleTrailer.FINAL_EXAM + ScheduleTrailer.TRAILER


class ExamTopic(object):
    EVENING_EXAM_TEMPLATE = string.Template("""
<ul class="topic evening_exam">
  <li class="topic evening_exam">
    The regular in-class session on $RegularClassDay
    is an OPTIONAL review session.
  </li>
  <li class="topic exam_day_time_rooms">
    The test itself is
    <span class=exam_date_time>
      $ExamDay evening from 7:30 p.m. to 9:30 p.m.
      (with an additional 30-minute grace period)
    </span>
    <span class=exam_rooms>
    in rooms TBA.
    </span>
    <ul>
      <li>
        So NOT $RegularClassDay, NOT daytime.
      </li>
    </ul>
  </li>
  <li class="topic exam_requirement">
    You MUST have completed this test's PRACTICE project
    <span class="parenthetical">
      (including its paper-and-pencil exercise)
    </span>
    BEFORE you take this test.
    <ul>
      <li>
        It is your ADMISSION TICKET to the test.
      </li>
      <li>
        Talk to your instructor if that poses a problem for you.
      </li>
    </ul>
  </li>
</ul>
""")


def main():
    """ Make a schedule for the indicated term. """
    #     html = gfm.markdown(xx)

    maker = ScheduleMaker(TermInfo('201810'))
    html = maker.make_schedule()
#     print(html)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
