"""
Code for all types of Session objects, along with SessionMaker.
Author: David Mutchler and his colleagues.
"""

from typing import List
from Constants import *  # All constants, and only constants, are in ALL_CAPS.
from Parser import Parser
from Topic import Topic


class Session:
    def __init__(self, session_number: int, session_title: str,
                 topics: List[Topic]):
        self.session_number = session_number
        self.session_title = session_title
        self.topics = topics

    def __repr__(self) -> str:
        return "{} {}".format(self.session_number, self.topics)


class RegularClassSession(Session):
    def __init__(self, session_number: int, session_title: str,
                 topics: List[Topic]):
        super().__init__(session_number, session_title, topics)


class ReviewSession(Session):
    def __init__(self, session_number: int, session_title: str,
                 topics: List[Topic],
                 exam_number: int, review_type: ExamOrReviewType):
        super().__init__(session_number, session_title, topics)
        self.exam_number = exam_number
        self.review_type = review_type

    def __repr__(self) -> str:
        return "{} {} {}".format(super().__repr__(),
                                 self.exam_number, self.review_type)


class ExamSession(Session):
    def __init__(self, session_number: int, session_title: str,
                 topics: List[Topic],
                 exam_number: int, exam_type: ExamOrReviewType):
        super().__init__(session_number, session_title, topics)
        self.exam_number = exam_number
        self.exam_type = exam_type


class EveningExamSession(ExamSession):
    def __init__(self, session_number: int, session_title: str,
                 topics: List[Topic],
                 exam_number: int, exam_type: ExamOrReviewType):
        super().__init__(session_number, session_title, topics,
                         exam_number, exam_type)

    def __repr__(self) -> str:
        return "{} {} {} {}".format(super().__repr__(), "evening exam",
                                    self.exam_number, self.exam_type)


class InClassExamSession(ExamSession):
    def __init__(self, session_number: int, session_title,
                 topics: List[Topic],
                 exam_number: int, exam_type: ExamOrReviewType):
        super().__init__(session_number, session_title, topics,
                         exam_number, exam_type)

    def __repr__(self) -> str:
        return "{} {} {} {}".format(super().__repr__(), "in-class exam",
                                    self.exam_number, self.exam_type)


class CapstoneProjectSession(Session):
    def __init__(self, session_number: int, session_title: str,
                 topics: List[Topic],
                 sprint_number: int):
        super().__init__(session_number, session_title, topics)
        self.sprint_number = sprint_number

    def __repr__(self) -> str:
        return "{} {}".format(super().__repr__(), self.sprint_number)


class SessionMaker:
    def __init__(self, filename: str):
        # TODO: Eventually set more than just the session titles
        #   and Session objects based on the titles.
        with open(filename, "r") as file_handle:
            self.text = file_handle.read()

        sessions_raw_data = self.text.split("\n\n")
        # Check for bad data:
        assert len(sessions_raw_data) == NUMBER_OF_SESSIONS

        for k in range(len(sessions_raw_data)):
            sessions_raw_data[k] = sessions_raw_data[k].strip("\n")
        self.sessions_raw_data = sessions_raw_data

        # Make the Session objects.
        # TODO: Eventually, the Session objects will include more information
        #   with data obtained not just from the session titles.
        self.sessions = []
        for k in range(NUMBER_OF_SESSIONS):
            session = self.make_session(k + 1, self.sessions_raw_data[k])
            self.sessions.append(session)

    @staticmethod
    def make_session(session_number: int, session_raw_data: str) -> Session:
        # FIXME: Make less brittle:
        lines = session_raw_data.split("\n")

        session_number_listed = Parser.parse_session_number(lines)
        assert session_number_listed == session_number  # Check for bad data

        session_title = Parser.parse_session_title(lines)

        topics = Parser.parse_topics(lines)
        session_type = Parser.parse_session_type(lines)

        exam_number = exam_or_review_type = sprint_number = None
        if session_type in (SessionType.REVIEW, SessionType.EVENING_EXAM,
                            SessionType.IN_CLASS_EXAM):
            exam_number = Parser.parse_exam_number(lines)
            exam_or_review_type = Parser.parse_type_of_exam_or_review(lines)
        elif session_type is CapstoneProjectSession:
            sprint_number = Parser.parse_sprint_number(lines)

        if session_type is SessionType.REGULAR:
            return RegularClassSession(session_number, session_title, topics)

        elif session_type is SessionType.REVIEW:
            return ReviewSession(session_number, session_title, topics,
                                 exam_number, exam_or_review_type)

        elif session_type is SessionType.EVENING_EXAM:
            return EveningExamSession(session_number, session_title, topics,
                                      exam_number, exam_or_review_type)

        elif session_type is SessionType.IN_CLASS_EXAM:
            return InClassExamSession(session_number, session_title, topics,
                                      exam_number, exam_or_review_type)

        elif session_type is SessionType.CAPSTONE_PROJECT:
            return CapstoneProjectSession(session_number, session_title,
                                          topics, sprint_number)

        else:
            raise ValueError("Unknown session type:\n" + str(session_type))
