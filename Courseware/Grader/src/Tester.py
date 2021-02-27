from WhoToGrade import WhoToGrade
from WhatToGrade import WhatToGrade
from TestResults import TestResults


class Tester:
    def __init__(self, what_to_grade: WhatToGrade, who_to_grade: WhoToGrade):
        self.what_to_grade = what_to_grade
        self.who_to_grade = who_to_grade

    def test(self) -> TestResults:
        pass


class StandardTester(Tester):
    def __init__(self, what_to_grade: WhatToGrade, who_to_grade: WhoToGrade):
        super().__init__(what_to_grade, who_to_grade)
