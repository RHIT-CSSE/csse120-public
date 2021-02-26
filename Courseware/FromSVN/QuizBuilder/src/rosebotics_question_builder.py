import sys
from string import Template
import re
import parse_format1

from Question import Question
from Question import QuestionType

TERM = '201810'
QUIZ_QUESTION_FILENAME = Template('./quizzes-${TERM}/Quiz${QUIZ_NUMBER}.txt')

def main():
    print_from_txt(15)

def print_from_txt(quiz_number, term=TERM):
    filename = QUIZ_QUESTION_FILENAME.substitute(QUIZ_NUMBER=quiz_number, TERM=term)
    f = open(filename, 'r')
    for line in f:
        parts = line.split(". ", 2)
        line = line.rstrip()
        if parts[0] == "ANS":
            print("""

    {
      questionType : "freetext",
      correctAnswerRegex : /^""" + parts[1].rstrip() + """$/i,
      correctAnswerOutput : "Correct!",
      incorrectAnswerOutput : "Please try again."
    },

    """)
        elif parts[0].isdigit():
            print("""    ]
  },""")
            print('"<br><br><b>X.</b> ', line, '<br>",',)
            print("""{
    questionType: "multiple choice",
    choices: [""")
        elif len(parts[0]) == 1 and parts[0].isalpha():
            if parts[0] == "D":
                print('"<br><br>' + line + '",')
            elif parts[0] == "M":
                print("M question")
            else:
                if not line.endswith("~"):
                    print('    ["' + line[3:] + '", false, "Please try again."],')
                else:
                    print('    ["' + line[3:-1] + '", true, "Correct!"],')

main()