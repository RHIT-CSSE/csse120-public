from Course import Course
from Course import Session
from Course import Module


class WhatToGrade:
    def __init__(self, course: Course, session: Session, module: Module):
        self.course = course
        self.session = session
        self.module = module


class StandardWhatToGrade(WhatToGrade):

    def __init__(self):
        super().__init__(self.get_course(), self.get_session(),
                         self.get_module())

    def get_course(self) -> Course:
        pass

    def get_session(self) -> Session:
        pass

    def get_module(self) -> Module:
        pass
