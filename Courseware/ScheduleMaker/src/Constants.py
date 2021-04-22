"""
Constants used throughout the ScheduleMaker.
Author: David Mutchler and his colleagues.
"""

import enum

TERM = "202130"  # Spring, 2020-21
FOLDER_FOR_HOME_PAGE = "/Users/davidmutchler/csse120-public/WWW/{}".format(TERM)

NUMBER_OF_SESSIONS = 30
HOME_PAGE = "{}/index.html".format(FOLDER_FOR_HOME_PAGE)
TERM_INFO_FILE = "{}/term_info.txt".format(FOLDER_FOR_HOME_PAGE)

TEMPLATES_FOLDER = "{}/Templates".format(FOLDER_FOR_HOME_PAGE)
HOME_PAGE_TEMPLATE = "{}/home_page_template.html".format(TEMPLATES_FOLDER)
NAVIGATION_BAR_TEMPLATE = "{}/navigation_bar_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_TEMPLATE = "{}/schedule_template.html".format(TEMPLATES_FOLDER)
FOOTER_TEMPLATE = "{}/footer_template.html".format(TEMPLATES_FOLDER)

SCHEDULE_WEEK_NUMBER_TEMPLATE = "{}/schedule_week_number_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_SESSION_TEMPLATE = "{}/schedule_session_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_EXAM_TEMPLATE = "{}/schedule_exam_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_NO_CLASS_TEMPLATE = "{}/schedule_no_class_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_BREAK_TEMPLATE = "{}/schedule_break_template.html".format(
    TEMPLATES_FOLDER)

LEARNING_OBJECTIVES_FOLDER = "{}/LearningObjectives".format(
    FOLDER_FOR_HOME_PAGE)
SESSION_TITLES_FILENAME = "{}/SessionTitles.md".format(
    LEARNING_OBJECTIVES_FOLDER)

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

SESSIONS_FOLDER = "{}/Sessions".format(FOLDER_FOR_HOME_PAGE)
EXAM_INFO_FOLDER = "{}/ExamInformation".format(SESSIONS_FOLDER)

SESSION_TEMPLATE = "{}/page_for_session_template.html".format(TEMPLATES_FOLDER)
EXAM_INFO_TEMPLATE = "{}/page_for_exam_information_template.html"
SESSION_SECTION_VIDEOS_READING_TEMPLATE = \
    "{}/session_section_videos_reading_template.html".format(TEMPLATES_FOLDER)
SESSION_SECTION_QUIZ_TEMPLATE = \
    "{}/session_section_quiz_template.html".format(TEMPLATES_FOLDER)
SESSION_SECTION_FOLLOW_ME_TEMPLATE = \
    "{}/session_section_follow_me_template.html".format(TEMPLATES_FOLDER)

SESSION_ITEM_VIDEO_TEMPLATE = \
    "{}/session_item_video_template.html".format(TEMPLATES_FOLDER)
SESSION_ITEM_READING_TEMPLATE = \
    "{}/session_item_reading_template.html".format(TEMPLATES_FOLDER)
SESSION_ITEM_OTHER_TEMPLATE = \
    "{}/session_item_other_template.html".format(TEMPLATES_FOLDER)

SESSION_VIDEOS_READING_FILENAME = "videos-reading"
SESSION_QUIZ_FILENAME = "quiz-answers"
SESSION_FOLLOW_ME_FILENAME = "follow-me"


@enum.unique
class ExamOrReviewType(enum.Enum):
    PAPER_AND_PENCIL = 1
    ON_THE_COMPUTER = 2
    BOTH = 3
    OTHER = 4


@enum.unique
class SessionType(enum.Enum):
    REGULAR = 1
    REVIEW = 2
    EVENING_EXAM = 3
    IN_CLASS_EXAM = 4
    CAPSTONE_PROJECT = 5
    OTHER = 6


@enum.unique
class SessionSectionType(enum.Enum):
    VIDEOS_READING = 1
    QUIZ = 2
    FOLLOW_ME = 3
