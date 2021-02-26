import sys
# types = ["multichoice", "truefalse", "shortanswer" , "matching",
# "cloze", "essay", "numerical", "description"]  # These are the possible
# question types in moodle (for reference)


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


def make_quiz(quiz_number, term='201740'):
    txt = './quizzes-' + term + '/Quiz' + str(quiz_number) + '.txt'
    xml = './quizzes-xml/Quiz' + str(quiz_number) + '.xml'
    category = ('$course/Quizzes-' + term + '/$Quiz ' +
                str(quiz_number) + '/')
    txt2xml(txt, xml, category)

# for j in range(4):
#     for k in range(1, j + 2):
#         print(j + k, end="")
#     print()
#
# for j in range(3):
#     for k in range(1, 6):
#         print(j + k, end="")
#     print()


make_quiz(1)
# for q in range(8, 9):
#     txt2xml("./quizzes txt/Quiz" + str(q) + ".txt",
#             "./quizzes xml/Quiz" + str(q) + ".xml", "$course/Quizzes-201630/$Quiz " + str(q) + "/")


# def foo1(seq):
#     total = 0
#     for k in range(len(seq) // 2):
#         total = total + seq[1 + (2 * k)]
#     return total
#
#
# def foo2(seq):
#     total = 0
#     for k in range(1, len(seq), 2):
#         total = total + seq[k]
#     return total
#
#
# def foo3(seq):
#     total = 0
#     m = 1
#     for _ in range(len(seq) // 2):
#         total = total + seq[m]
#         m = m + 2
#     return total
#
# print(foo1([3]))
# print(foo1([3, 6]))
# print(foo1([3, 6, 1, 4, 9, 5]))
#
# print(foo2([3]))
# print(foo2([3, 6]))
# print(foo2([3, 6, 1, 4, 9, 5]))
#
# print(foo3([3]))
# print(foo3([3, 6]))
# print(foo3([3, 6, 1, 4, 9, 5]))
