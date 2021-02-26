import re
from Question import Question
from Question import QuestionType

# types = ["multichoice", "truefalse", "shortanswer" , "matching",
# "cloze", "essay", "numerical", "description"]  # These are the possible
# question types in moodle (for reference)

QUESTION_DELIMETER = '^Q.'
ANSWER_DELIMETER = '^A.'
MATCHING_SYMBOL = '->'
CORRECT_ANSWER_SYMBOL = '~'

TRUE_FALSE = ('true', 'false', 't', 'f')
YES_NO = ('yes', 'no', 'y', 'n')

def questions_from_lines(lines):
    split_at_QUESTION_DELIMETERs = get_questions(lines)
    questions = make_questions(split_at_QUESTION_DELIMETERs)
    return questions

def get_questions(lines):
    return re.split(QUESTION_DELIMETER, lines, flags=re.MULTILINE)[1:]

def make_questions(list_of_questions_answers):
    questions = []
    for question_answer in list_of_questions_answers:
        split_at_ANSWER_DELIMETERs = re.split(ANSWER_DELIMETER,
                                              question_answer,
                                              flags=re.MULTILINE)
        # The test of the question_answer is the portion that preceeds
        # the first ANSWER_DELIMETER, with white space stripped:
        question_text = split_at_ANSWER_DELIMETERs[0].strip()

        # The rest of the question_answer is a list of answers.
        # Strip white space from the ends of each answer:
        answers = split_at_ANSWER_DELIMETERs[1:]
        for k in range(len(answers)):
            answers[k] = answers[k].strip()

        # Get the type of question, make a Question, and add to the list:
        question_type = get_question_type(answers)
        question = Question(question_type, question_text, answers)
        questions.append(question)

    return questions


def get_question_type(answers):
    # No answers means Description:
    if len(answers) == 0:
        return QuestionType.description

    # If there is just one answer:
    if len(answers) == 1:

        answer = answers[0].strip()

        # Just white space means Essay.
        if answer == '':
            return QuestionType.essay

        # Just True or False (possibly with a CORRECT_ANSWER_SYMBOL)
        # means True/False:
        if answer.replace(CORRECT_ANSWER_SYMBOL, '').lower() in TRUE_FALSE:
            return QuestionType.truefalse

        # Similarly for just Yes or No:
        if answer.replace(CORRECT_ANSWER_SYMBOL, '').lower() in YES_NO:
            return QuestionType.yesno

        # Otherwise Short Answer (with just one possible answer):
        # CONSIDER: This may conceal an "impossible" answer that is an error.
        return QuestionType.shortanswer

    # If there are multiple answers:

    # If there are just two answers and both are True/False or Yes/No,
    # and exactly one of the two choices has a CORRECT_ANSWER_SYMBOL,
    # that means True/False or Yes/No.
    if len(answers) == 2:
        for question_type in (TRUE_FALSE, YES_NO):
            result = True
            for answer in answers:
                reduced_answer = answer.replace(CORRECT_ANSWER_SYMBOL,
                                                '').lower().strip()
                if reduced_answer not in question_type:
                    result = False
                    break
            if result:
                if ((CORRECT_ANSWER_SYMBOL in answers[0]) !=
                    (CORRECT_ANSWER_SYMBOL in answers[1])):
                    if question_type == TRUE_FALSE:
                        return QuestionType.truefalse
                    else:
                        return QuestionType.yesno

    # MATCHING_SYMBOL in all the answers means Matching:
    matching = True
    for answer in answers:
        if MATCHING_SYMBOL not in answer:
            matching = False
            break
    if matching:
        return QuestionType.matching

    # CORRECT_ANSWER_SYMBOL in NONE of the answers means short answer:
    short_answer = True
    for answer in answers:
        if CORRECT_ANSWER_SYMBOL in answer:
            short_answer = False
            break
    if short_answer:
        return QuestionType.shortanswer

    # Otherwise:  MULTIPLE CHOICE.
    return QuestionType.multichoice

# def format1_to_format2(quiz_number, term=TERM):
#     lines = read_file(quiz_number, term)
#     lines = re.sub(r'^D\.', 'Q.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^[0-9]+\.', 'Q.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^[a-z]\.', 'A.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^ANS\.', 'A.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^M\.', 'A.', lines, flags=re.MULTILINE)
#     return lines

