"""
Constants used throughout the ScheduleMaker.
Author: David Mutchler and his colleagues.
"""

import enum

TERM = "202110"  # Fall, 2020

FOLDER_FOR_HOME_PAGE = "/Users/davidmutchler/csse120-public/WWW/{}".format(TERM)
# FOLDER_FOR_HOME_PAGE = "../../../WWW/{}".format(TERM)

HOME_PAGE = "{}/index.html".format(FOLDER_FOR_HOME_PAGE)
TERM_INFO_FILE = "{}/term_info.txt".format(FOLDER_FOR_HOME_PAGE)

TEMPLATES_FOLDER = "{}/Templates".format(FOLDER_FOR_HOME_PAGE)
HOME_PAGE_TEMPLATE = "{}/home_page_template.html".format(TEMPLATES_FOLDER)
NAVIGATION_BAR_TEMPLATE = "{}/navigation_bar_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_TEMPLATE = "{}/schedule_template.html".format(TEMPLATES_FOLDER)
SCHEDULE_SESSSION_TEMPLATE = "{}/schedule_session_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_NO_CLASS_TEMPLATE = "{}/schedule_no_class_template.html".format(
    TEMPLATES_FOLDER)
SCHEDULE_BREAK_TEMPLATE = "{}/schedule_break_template.html".format(
    TEMPLATES_FOLDER)
FOOTER_TEMPLATE = "{}/footer_template.html".format(TEMPLATES_FOLDER)

LEARNING_OBJECTIVES_FOLDER = "{}/LearningObjectives".format(
    FOLDER_FOR_HOME_PAGE)
SESSION_TITLES_FILENAME = "{}/SessionTitles.md".format(
    LEARNING_OBJECTIVES_FOLDER)

NUMBER_OF_SESSIONS = 30

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

SESSIONS_FOLDER = "{}/Sessions".format(FOLDER_FOR_HOME_PAGE)
SESSION_TEMPLATE = "{}/session_page_template.html".format(TEMPLATES_FOLDER)
SESSION_VIDEO_TEMPLATE = \
    "{}/session_video_template.html".format(TEMPLATES_FOLDER)
SESSION_READING_TEMPLATE = \
    "{}/session_reading_template.html".format(TEMPLATES_FOLDER)
SESSION_FOLLOW_ME_TEMPLATE = \
    "{}/session_follow_me_template.html".format(TEMPLATES_FOLDER)
SESSION_OTHER_ITEM_TEMPLATE = \
    "{}/session_other_item_template.html".format(TEMPLATES_FOLDER)
SESSION_PREPARATION_FILENAME = "preparation.html"
SESSION_FOLLOW_ME_FILENAME = "follow_me.html"


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
