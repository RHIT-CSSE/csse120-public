from Course import Course
from Course import Session
from Course import Module
import Constants


class WhatToGrade:
    def __init__(self, course: Course = Constants.CSSE120,
                 session: Session = Constants.SESSION,
                 module: Module = Constants.MODULE):
        self.course = course
        self.session = session
        self.module = module
