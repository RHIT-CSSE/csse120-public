from enum import Enum

# types = ["multichoice", "truefalse", "shortanswer" , "matching",
# "cloze", "essay", "numerical", "description"]  # These are the possible
# question types in moodle (for reference)

class Question(object):
    def __init__(self, question_type=None, question_text=None,
                 answers=None):
        self.question_text = question_text
        self.question_type = question_type
        self.answers = answers

    def __repr__(self):
        f_string = ('Question(question_type={}, ' +
                    'question_text={!r}, ' +
                    'answers={!r})')
        return f_string.format(self.question_type.name,
                               self.question_text,
                               self.answers)

class QuestionType(Enum):
    description = 1
    multichoice = 2
    truefalse = 3
    shortanswer = 4
    matching = 5
    essay = 6
    yesno = 7  # Not a real type, treated as a multichoice

class Answer(object):
    def __init__(self, text=None, credit=None, match=None):
        self.text = text
        self.credit = credit  # For all EXCEPT Matching questions
        self.match = match  # For MATCHING questions

    def __repr__(self):
        f_string = 'Answer(text={!r}, '
        if self.credit is not None:
            f_string += 'credit={!r})'
            return f_string.format(self.text, self.credit)
        else:
            f_string += 'match={!r})'
            return f_string.format(self.text, self.match)
