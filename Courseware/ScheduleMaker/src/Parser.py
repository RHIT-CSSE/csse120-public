"""
The parsing code for the ScheduleMaker.
Author: David Mutchler and his colleagues.
"""

import dateutil.parser
from typing import List
from Constants import *  # All constants, and only constants, are in ALL_CAPS.
from Topic import Topic


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
    def parse_session_number(lines: List[str]) -> int:
        session_blah = lines[0].split(":")[0]
        session_number = int(session_blah.split(" ")[1])
        return session_number

    @staticmethod
    def parse_session_title(lines: List[str]) -> str:
        return lines[0].split(":")[1]

    @staticmethod
    def parse_session_type(lines: List[str]) -> SessionType:
        topic_lines = "\n".join(lines[1:]).lower()
        if "Practice for Exam" in topic_lines:
            return SessionType.REVIEW
        elif "exam " in topic_lines and "evening" in topic_lines:
            return SessionType.EVENING_EXAM
        elif "exam" in topic_lines:
            return SessionType.IN_CLASS_EXAM
        elif "capstone project" in topic_lines:
            return SessionType.CAPSTONE_PROJECT
        else:
            return SessionType.REGULAR

    @staticmethod
    def parse_topics(lines: List[str]) -> List[Topic]:
        topics = []
        for k in range(1, len(lines)):
            if lines[k].startswith("  - "):
                topic_item = lines[k].replace("  - ", "").strip()
                topics.append(Topic(topic_item, 1))
            elif lines[k].startswith("    - "):
                topic_item = lines[k].replace("    - ", "").strip()
                topics.append(Topic(topic_item, 2))
            else:
                raise ValueError("Bad topic line {}: {}".format(k, lines[k]))

        return topics

    @staticmethod
    def parse_type_of_exam_or_review(lines: List[str]) -> ExamOrReviewType:
        pass

    @staticmethod
    def parse_exam_number(lines: List[str]) -> int:
        pass

    @staticmethod
    def parse_sprint_number(lines: List[str]) -> int:
        pass
