import sys
from string import Template
import re

# types = ["multichoice", "truefalse", "shortanswer" , "matching",
# "cloze", "essay", "numerical", "description"]  # These are the possible
# question types in moodle (for reference)

FORMAT_VERSION = 2
FORMAT_TYPE = 'markdown'

if FORMAT_VERSION == 2:
    import parse_format2
    questions_from_lines = parse_format2.questions_from_lines
else:
    import parse_format1
    questions_from_lines = parse_format1.questions_from_lines

from Question import Question
from Question import QuestionType

TERM = '201710'

QUIZ_QUESTION_FILENAME = Template('./quizzes-${TERM}/Quiz${QUIZ_NUMBER}.txt')
QUIZ_XML_FILENAME = Template('./quizzes-xml/Quiz${QUIZ_NUMBER}.xml')

XML_HEADER = Template("""<?xml version="1.0" ?>
<quiz>
  <question type="category" encoding="UTF-8"?>
    <category>
      <text>$$course/Quizzes-${TERM}/$$Quiz ${QUIZ_NUMBER}/</text>
    </category>
  </question>""")

XML_TRAILER = Template("""
</quiz>""")

XML_QUESTION = Template("""
  <question type="${QUESTION_TYPE}">
    <name>
      <text>$QUESTION_NUMBER_FOR_SORTING</text>
    </name>
    <questiontext format="${FORMAT_TYPE}">
      <text>
      <![CDATA[
      ${QUESTION_TEXT}
      ]]>
      </text>
    </questiontext>
  </question>""")

MATCHING_SUBQUESTION = Template("""
<subquestion format="${FORMAT_TYPE}">
      <text>${LEFT_HAND_SIDE_OF_MATCH}</text>
      <answer>
        <text>${RIGHT_HAND_SIDE_OF_MATCH}</text>
      </answer>
</subquestion>""")

def xml_from_txt(quiz_number, term=TERM):
    lines = read_questions(quiz_number, term)
    questions = questions_from_lines(lines)
    write_xml(quiz_number, questions, term)

    for question in questions:
        print(question)

def read_questions(quiz_number, term=TERM):
    filename = QUIZ_QUESTION_FILENAME.substitute(QUIZ_NUMBER=quiz_number,
                                                 TERM=term)
    with open(filename, 'r') as f:
        lines = f.read()

    return lines

def write_xml(quiz_number, questions, term=TERM):
    filename = QUIZ_XML_FILENAME.substitute(QUIZ_NUMBER=quiz_number)
    with open(filename, 'w') as xml_file:
        write_xml_header(xml_file, quiz_number, term)
        for k in range(len(questions)):
            write_xml_question(questions[k], k, xml_file)
            write_xml_answers(questions[k], xml_file)
        write_xml_trailer(xml_file)

def write_xml_header(xml_file, quiz_number, term):
    xml_file.write(XML_HEADER.substitute(QUIZ_NUMBER=quiz_number,
                                         TERM=term))

def write_xml_question(question, question_number, xml_file):
    """
      :type question: Question
    """
    # WARNING: More than 9,999 questions destroys the sorting.
    number_for_sorting = '{:0>4}'.format(question_number)
    question_type = question.question_type.name
    xml = XML_QUESTION.substitute(QUESTION_TYPE=question_type,
                                  QUESTION_NUMBER_FOR_SORTING=number_for_sorting,
                                  FORMAT_TYPE=FORMAT_TYPE,
                                  QUESTION_TEXT=question.question_text)

    xml_file.write(xml)

def write_xml_answers(question, xml_file):
    """
    :type question: Question
    """
    if question.question_type == QuestionType.description:
        return
    if question.question_type == QuestionType.essay:
        pass

def write_xml_trailer(xml_file):
    xml_file.write(XML_TRAILER.substitute())

# xml_from_txt(2)

def txt2xml(ifi, ofi, category):
    ifi = open(ifi)
    ofi = open(ofi, 'w')
    ofi.write("<?xml version=\"1.0\" ?>\n<quiz>\n")
    ofi.write("<question type=\"category\">\n<category>\n")
    ofi.write("<text> " + category + "</text>\n</category>\n</question>\n")
    ctr = 0
    question = {"text": "", "type": "", "answers": []}
    # Answers are a dictionary consisting of text and the amount of credit
    # given for this answer

    for li in ifi:
        print(li)
        li = li.strip()
        if li == "":
            continue
        mark = marktype(li.split(".")[0])
        li = ".".join(li.split(".")[1:])
        li = li.strip()
        if mark == 0:  # We don't know what this line is
            print(li, ctr)
            i = input(
                "We don't know what " + li + " is. Is this a problem (y/n)?:")
            if i == 'y':
                sys.exit(0)
            else:
                continue
        if mark == 1:  # We have a new question
            # print the old question
            ctr += 1
            ctr = xmlout(ofi, question, ctr)
            # Make a new question with the given question text
            question = {"text": li, "type": "", "answers": []}
        if mark == 2:  # We have a description
            # print the old question
            ctr += 1
            ctr = xmlout(ofi, question, ctr)
            # Make a new question with the given question text
            question = {"text": li, "type": "description", "answers": []}
        if mark == 3:  # We have a short answer answer
            # create the new answer
            # assign it 100% credit
            question["type"] = "shortanswer"
            question["answers"].append({"text": li, "credit": 100})
        if mark == 4:  # We have a t/f or multiple choice answer
            # create the new answer
            question["answers"].append({"text": li, "credit": 0})
            # if it is marked with ~, assign it 100% credit
            if "~" in li:
                question["answers"][-1]["credit"] = 100
                question[
                    "answers"][-1]["text"] = question["answers"][-1]["text"].replace("~", "")
        if mark == 6:  # matching question/answer pair
            matchpair = li.split("->")
            if len(matchpair) == 1:
                assert(" -> " in li)
                a = matchpair[0].strip()
            else:
                q = matchpair[0].strip()
                a = matchpair[1].strip()
            question["type"] = "matching"
            if not "pairs" in question:
                question["pairs"] = []
            question["pairs"].append({"question": q, "answer": a})

    # print the last question
    ctr += 1
    ctr = xmlout(ofi, question, ctr)
    ofi.write("</quiz>")
    ofi.close()
    ifi.close()


def gettype(q):
    if q["type"] != "":
        return
    if len(q["answers"]) == 0:
        q["type"] = "essay"
        q["answers"] = [{"text": "", "credit": 0}]
    # this is a true false question
    elif len([a for a in q["answers"] if a["text"] in ["True", "False", "true", "false"]]) == len(q["answers"]):
        for a in range(len(q["answers"])):
            q["answers"][a]["text"] = q["answers"][a]["text"].lower()
        q["type"] = "truefalse"
    else:
        q["type"] = "multichoice"


def marktype(s):
    if s == "":
        return 0
    if isint(s):
        return 1
    if s == "D":
        return 2
    if s == "ANS":
        return 3
    if s in "abcdefghijklmnopqrstuvwxyz":
        return 4
    if s == "FEED":
        return 5
    if s == "M":
        return 6
    return 0


def isint(a):
    try:
        int(a)
        return True
    except:
        return False


def matchingout(ofi, question, ctr):
    for pair in question["pairs"]:
        ofi.write("<subquestion>\n")
        ofi.write("<text><![CDATA[" + pair["question"] + "]]></text>\n")
        ofi.write("<answer>\n")
        ofi.write("<text><![CDATA[" + pair["answer"] + "]]></text>\n")
        ofi.write("</answer>\n")
        ofi.write("</subquestion>\n")


def xmlout(ofi, question, ctr):
    if question["text"] == "":
        return ctr - 1
    gettype(question)
    ofi.write("<question type=\"" + question["type"] + "\">\n")
    ofi.write(
        "<name><text><![CDATA[" + str(ctr).zfill(3) + " " + question["text"] + "]]></text></name>\n")
    ofi.write("<questiontext format=\"html\">\n")
    ofi.write(
        "<text><![CDATA[" + question["text"] + "]]></text>\n</questiontext>\n")
    if question["type"] == "matching":
        matchingout(ofi, question, ctr)
        ofi.write("<shuffleanswers>false</shuffleanswers>\n")
    else:
        # Generally want to shuffle the answers because most people write the correct answers first.
        # You can override later in the XML or online.
        ofi.write("<shuffleanswers>true</shuffleanswers>\n")
        # handle multichoice case when checkboxes are desired
        anscount = 0
        if question["type"] == "multichoice":
            for a in question["answers"]:
                if a["credit"] > 0:
                    anscount += 1
                if anscount > 1:  # need checkboxes
                    ofi.write('<single>false</single>')
                    break
        anscount = max(anscount, 1)
        for a in question["answers"]:
            ofi.write(
                "<answer fraction=\"" + str(a["credit"] / anscount) + "\">\n")
            ofi.write("<text><![CDATA[" + a["text"] + "]]></text>\n")
            ofi.write("</answer>\n")

    ofi.write("</question>\n")
    return ctr

#     if question_type == QuestionType.truefalse:
#         prefix = 'True or False: '
#     elif question_type == QuestionType.yesno:
#         prefix = 'Yes or No: '

#     for k in range(len(raw_answers)):
#         if not raw_answers[k].strip().startswith(prefix):
#             raw_answers[k] = prefix + '\n' + raw_answers[k]

def make_quiz(quiz_number, term='201630'):
    txt = './quizzes-' + term + '/Quiz' + str(quiz_number) + '.txt'
    xml = './quizzes-xml/Quiz' + str(quiz_number) + '.xml'
    category = ('$course/Quizzes-' + term + '/$Quiz ' +
                str(quiz_number) + '/')
    txt2xml(txt, xml, category)

def format1_to_format2(quiz_number, term=TERM):
    lines = read_questions(quiz_number, term)
    lines = re.sub(r'^D\.', 'Q.', lines, flags=re.MULTILINE)
    lines = re.sub(r'^[0-9]+\.', 'Q.', lines, flags=re.MULTILINE)
    lines = re.sub(r'^[a-z]\.', 'A.', lines, flags=re.MULTILINE)
    lines = re.sub(r'^ANS\.', 'A.', lines, flags=re.MULTILINE)
    lines = re.sub(r'^M\.', 'A.', lines, flags=re.MULTILINE)
    return lines

lines = format1_to_format2(1, '201710')
print(lines)
# make_quiz(1)
# for q in range(8, 9):
#     txt2xml("./quizzes txt/Quiz" + str(q) + ".txt",
#             "./quizzes xml/Quiz" + str(q) + ".xml", "$course/Quizzes-201630/$Quiz " + str(q) + "/")
