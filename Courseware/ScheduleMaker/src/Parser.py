"""
The parsing code for the ScheduleMaker.
Author: David Mutchler and his colleagues.
"""

import dateutil.parser
from typing import List
from Constants import *  # All constants, and only constants, are in ALL_CAPS.
from Topic import Topic
import re


class Parser:

    @staticmethod
    def parse_first_and_last_days_of_term(lines: List[str]) -> (str, str):
        # CONSIDER: Reformat data to make this method less brittle.
        datestring = " ".join(lines[0].split()[2:])
        first_day_of_term = dateutil.parser.parse(datestring).date()

        datestring = " ".join(lines[1].split()[2:])
        last_day_of_tenth_week = dateutil.parser.parse(datestring).date()

        return first_day_of_term, last_day_of_tenth_week

    @staticmethod
    def parse_class_meeting_days_of_week(lines: List[str]) -> List[int]:
        # CONSIDER: Reformat data to make this method less brittle.
        class_meeting_days_of_week_text = lines[2].split()[2:]

        # Check for bad data:
        assert (len(class_meeting_days_of_week_text) == 3)
        for day_of_week in class_meeting_days_of_week_text:
            assert (day_of_week in DAYS_OF_WEEK)

        # Store class meeting days as integers: 0 = Monday, 1 = Tuesday, etc:
        class_meeting_days_of_week = []
        for day_of_week in class_meeting_days_of_week_text:
            class_meeting_days_of_week.append(
                DAYS_OF_WEEK.index(day_of_week))
        return class_meeting_days_of_week

    @staticmethod
    def parse_days_for_break(lines: List[str]) -> (str, str):
        # Days for break (Fall break, Winter break, Spring break):
        datestring = " ".join(lines[3].split()[2:])
        start_date_of_break = dateutil.parser.parse(datestring).date()

        datestring = " ".join(lines[4].split()[2:])
        end_date_of_break = dateutil.parser.parse(datestring).date()

        return start_date_of_break, end_date_of_break

    @staticmethod
    def parse_piazza_url(lines: List[str]) -> str:
        return lines[5].split()[2]

    @staticmethod
    def parse_session_number(lines: List[str]) -> int:
        session_blah = lines[0].split(":")[0]
        session_number = int(session_blah.split(" ")[1])
        return session_number

    @staticmethod
    def parse_session_title(lines: List[str]) -> str:
        return lines[0].split(":")[1]

    @staticmethod
    def parse_session_type(lines: List[str]) -> SessionType:
        # FIXME: The following is brittle.
        session_title = Parser.parse_session_title(lines)
        topic_lines = "\n".join(lines[1:]).lower()
        if session_title.strip()[:5] == "Exam " \
                and "practice" not in  session_title.lower():
            if "evening" in topic_lines.lower():
                return SessionType.EVENING_EXAM
            else:
                return SessionType.IN_CLASS_EXAM
        if "exam" in session_title.lower() and \
                "practice" in  topic_lines.lower():
            return SessionType.REVIEW
        elif "capstone project" in topic_lines.lower():
            return SessionType.CAPSTONE_PROJECT
        else:
            return SessionType.REGULAR
        # old, throw away when change is OK
        # topic_lines = "\n".join(lines[1:]).lower()
        # if "Practice for Exam" in topic_lines:
        #     return SessionType.REVIEW
        # elif "exam " in topic_lines and "evening" in topic_lines:
        #     return SessionType.EVENING_EXAM
        # elif "exam" in topic_lines:
        #     return SessionType.IN_CLASS_EXAM
        # elif "capstone project" in topic_lines:
        #     return SessionType.CAPSTONE_PROJECT
        # else:
        #     return SessionType.REGULAR

    @staticmethod
    def parse_topics(lines: List[str]) -> List[Topic]:
        topics = []
        for k in range(1, len(lines)):
            line = lines[k]
            before_dash = re.sub(r"- .*$", "", line)
            if len(before_dash) % 2 == 0:
                level = len(before_dash) // 2
                topic_item = re.sub(r"^ +- ", "", line)
                topics.append(Topic(topic_item, level))
                print(level, topic_item)
            else:
                raise ValueError("Bad topic line {}: {}".format(k, lines[k]))

        return topics

    @staticmethod
    def parse_type_of_exam_or_review(lines: List[str]) -> ExamOrReviewType:
        pass

    @staticmethod
    def parse_exam_information(lines: List[str]) -> (str, str, str, str):
        # FIXME: the following is brittle
        exam_number = int(Parser.parse_session_title(lines)[6])
        day_of_week = lines[1].split(": ")[1].strip()
        date = lines[2].split(": ")[1].strip()
        time = lines[3].split(": ")[1].strip()
        no_regular_class = lines[4].split(": ")[1].strip()
        return exam_number, day_of_week, date, time, no_regular_class

    @staticmethod
    def parse_sprint_number(lines: List[str]) -> int:
        pass

