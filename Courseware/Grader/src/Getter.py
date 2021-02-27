from WhatToGrade import WhatToGrade
from WhoToGrade import WhoToGrade


class Getter:
    def __init__(self, what_to_grade: WhatToGrade, who_to_grade: WhoToGrade):
        self.what_to_grade = what_to_grade
        self.who_to_grade = who_to_grade

    def get(self):
        pass


class StandardGetter(Getter):
    def __init__(self, what_to_grade: WhatToGrade, who_to_grade: WhoToGrade):
        super().__init__(what_to_grade, who_to_grade)
