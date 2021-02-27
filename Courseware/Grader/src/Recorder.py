from WhatToGrade import WhatToGrade
from WhoToGrade import WhoToGrade
from TestResults import TestResults


class Recorder:
    def __init__(self, what_to_grade: WhatToGrade, who_to_grade: WhoToGrade):
        self.what_to_grade = what_to_grade
        self.who_to_grade = who_to_grade

    def record(self, results: TestResults) -> bool:
        return True  # Stub


class StandardRecorder(Recorder):
    def __init__(self, what_to_grade: WhatToGrade, who_to_grade: WhoToGrade):
        super().__init__(what_to_grade, who_to_grade)
