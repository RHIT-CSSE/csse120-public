import re
from Question import Question
from Question import QuestionType
from Question import Answer

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
    # The QUESTION_DELIMITER symbol separates questions,
    # where each question has 0 or more answers associated with it:
    raw_questions = get_questions_with_answers(lines)

    # For each question (with associated answer(s))
    # parse it into a Question (with Answers).
    questions = []
    for question in raw_questions:
        questions.append(make_Question(question))

    return questions

def get_questions_with_answers(lines):
    return re.split(QUESTION_DELIMETER, lines, flags=re.MULTILINE)[1:]

def make_Question(raw_question):
    split_at_ANSWER_DELIMETERs = re.split(ANSWER_DELIMETER,
                                          raw_question,
                                          flags=re.MULTILINE)

    # The text of the question is the portion that preceeds
    # the first ANSWER_DELIMETER, with white space stripped:
    question_text = split_at_ANSWER_DELIMETERs[0].strip()

    # The rest of the raw_question is a list of answers.
    raw_answers = split_at_ANSWER_DELIMETERs[1:]

    # Get the type of question along with the list of Answers
    # from the raw_answers.
    question_type, answers = get_question_type_and_answers(raw_answers)

    return Question(question_type, question_text, answers)


def get_question_type_and_answers(raw_answers):
    # No answers means type is Description, answers is None
    if len(raw_answers) == 0:
        answers = None
        return QuestionType.description, answers

    # If there is just one answer:
    if len(raw_answers) == 1:

        answer = raw_answers[0]

        # Just white space means type is Essay, answers is []
        if answer.strip() == '':
            answers = []
            return QuestionType.essay, answers

        # Just True or False (possibly with a CORRECT_ANSWER_SYMBOL
        # at the end) means True/False, with indicated Answer.
        reduced_answer = answer.strip()
        if reduced_answer[-1] == CORRECT_ANSWER_SYMBOL:
            reduced_answer = reduced_answer[:-1]

        if reduced_answer.lower() in TRUE_FALSE:
            return QuestionType.truefalse, [Answer(reduced_answer, 100)]

        # Similarly for just Yes or No:
        if reduced_answer.lower() in YES_NO:
            return QuestionType.yesno, [Answer(reduced_answer, 100)]

        # Otherwise Short Answer (with just one possible answer):
        # CONSIDER: This may conceal an "impossible" answer that is an error.
        return QuestionType.shortanswer, [Answer(answer, 100)]

    # If there are multiple raw_answers:

    # If there are just two raw_answers and both are True/False or Yes/No,
    # and exactly one of the two choices has a CORRECT_ANSWER_SYMBOL,
    # that means True/False or Yes/No.
    if len(raw_answers) == 2:

        a1 = raw_answers[0].strip()
        a2 = raw_answers[1].strip()
        if (a1.endswith(CORRECT_ANSWER_SYMBOL) !=
            a2.endswith(CORRECT_ANSWER_SYMBOL)):

            # Exactly one correct answer.
            # Are the answers True/False or Yes/No or something else?
            a1 = a1.replace(CORRECT_ANSWER_SYMBOL, '')
            a2 = a2.replace(CORRECT_ANSWER_SYMBOL, '')

            if a1 in TRUE_FALSE and a2 in TRUE_FALSE and a1 != a2:
                answers = make_answers_for_multiple_choice(raw_answers,
                                                           QuestionType.truefalse)
                return QuestionType.truefalse, answers

            elif a1 in YES_NO and a2 in YES_NO and a1 != a2:
                answers = make_answers_for_multiple_choice(raw_answers,
                                                           QuestionType.truefalse)
                return QuestionType.yesno, answers

    # MATCHING_SYMBOL in all the raw_answers means Matching:
    matching = True
    for answer in raw_answers:
        if MATCHING_SYMBOL not in answer:
            matching = False
            break
    if matching:
        answers = make_answers_for_matching(raw_answers)
        return QuestionType.matching, answers

    # CORRECT_ANSWER_SYMBOL in NONE of the raw_answers means short answer:
    short_answer = True
    for answer in raw_answers:
        if CORRECT_ANSWER_SYMBOL in answer:
            short_answer = False
            break
    if short_answer:
        answers = make_answers_for_short_answer(raw_answers)
        return QuestionType.shortanswer, answers

    # Otherwise:  MULTIPLE CHOICE.
    # CONSIDER: This may conceal an "impossible" answer that is an error.
    answers = make_answers_for_multiple_choice(raw_answers)
    return QuestionType.multichoice, answers

def make_answers_for_multiple_choice(raw_answers):
    answers = []
    corrects = 0
    for answer in raw_answers:
        if answer.strip().endswith(CORRECT_ANSWER_SYMBOL):
            corrects = corrects + 1
            answers.append(Answer(answer, '100', None))
        else:
            answers.append(Answer(answer, '0', None))

    if corrects == 0:
        print('ERROR: Multiple choice with NO correct answer!')
        exit()

    if corrects > 1:
        for answer in answers:
            if answer.credit == '100':
                answer.credit = str(100 / corrects)

    return answers

def make_answers_for_matching(raw_answers):
    answers = []
    corrects = 0
    for answer in raw_answers:
        halves = answer.split('->')
        if halves[0].strip() == '':
            answers.append(Answer('', '0', halves[1]))
        else:
            corrects = corrects + 1
            answers.append(Answer(halves[0], '100', halves[1]))

    if corrects == 0:
        print('ERROR: Matching with NO correct answer!')
        exit()

    if corrects > 1:
        for answer in answers:
            if answer.credit == '100':
                answer.credit = str(100 / corrects)

    return answers

def make_answers_for_short_answer(raw_answers):
    answers = []
    for answer in raw_answers:
        answers.append(Answer(answer, 100, None))

    return answers

# def format1_to_format2(quiz_number, term=TERM):
#     lines = read_file(quiz_number, term)
#     lines = re.sub(r'^D\.', 'Q.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^[0-9]+\.', 'Q.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^[a-z]\.', 'A.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^ANS\.', 'A.', lines, flags=re.MULTILINE)
#     lines = re.sub(r'^M\.', 'A.', lines, flags=re.MULTILINE)
#     return lines

