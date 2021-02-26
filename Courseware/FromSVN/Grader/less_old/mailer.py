"""
<describe what this module has/does>

Created on Apr 3, 2016.
Written by: mutchler.
"""

import string

FIRST_USERNAME_COLUMN = 3


class Problem(object):

    def __init__(self, problem_name):
        self.problem_name = problem_name
        self.points_available = None
        self.lines_for_deductions = []
        self.lines_for_comments = []
        self.line_with_score = None

    def __str__(self):
        template = "$Problem (points available: $Points)"
        t = string.Template(template)
        return t.substitute(Problem=self.problem_name,
                            Points=self.points_available)


class ProblemResult(object):

    def __init__(self,
                 problem=None,
                 deductions=None,
                 comments=None,
                 score=None):
        self.problem = problem
        self.deductions = deductions
        self.comments = comments
        self.score = score

    def __str__(self):
        if 'See me re:' in self.comments:
            self.comments.remove('See me re:')
        template = """
Score and comments on problem: $Problem
Your score on this problem: $Score
"""
        if self.deductions:
            template += "Points were deducted for the following reasons:\n"
            for deduction in self.deductions:
                template += str(deduction) + '\n'

        if self.comments:
            template += """Please note the following additional comments,
discussing them with me in class (or after class) as needed:\n"""
            for comment in self.comments:
                template += comment + '\n'

        t = string.Template(template)
        return t.substitute(Problem=self.problem,
                            Score=str(self.score))


class StudentResult(object):

    MSG1 = """$Student
Hi!  Here is your score on $Test, along with comments on your work.

IMPORTANT: Look at the points that you missed.
  If there is anything that you are not sure that you understand,
  find me in my office today (Wednesday) between 3 and 6 p.m.
  That will help you be ready for tonight's Test 3.

In addition:
Please examine the places below (if any) where there is either
  -- a line that has an indication of points deducted (and why)
  -- a line that begins with 'See me ...'
The 'See me ...' lines are comments that are important for you to
understand, even though no points were deducted for them on THIS test.

I work very hard to grade accurately, but of course it is always
possible that I made I mistake.  If you are unclear about any
of your scores, simply ask me about them in class.

The following lines are brief, hence somewhat cryptic.  Simply
   ** BRING YOUR QUESTIONS TO CLASS. **

  ... david m.
"""

    MSG2 = """$Student
Hi!  Here is your score on $Test, along with comments on your work.

IMPORTANT: Please examine the places below (if any) where there is either
  -- a line that has an indication of points deducted (and why)
  -- a line that begins with 'See me ...'
The 'See me ...' lines are comments that are important for you to
understand, even though no points were deducted for them on THIS test.

For the in-class portion of $Test, your score on each problem is
on Moodle.  For problems where you missed points, re-try the problem.
Then, in class show me your reworked result and I will tell you
whether or not it is correct.  That way, you can learn from your mistakes!

The following lines are brief, hence somewhat cryptic.  Simply
   ** BRING YOUR QUESTIONS TO CLASS. **

  ... david m.
"""

    def __init__(self, student):
        self.student = student
        self.problem_results = []
        self.totals = []

    def __str__(self):
        template = StudentResult.MSG2
        for result in self.problem_results:
            template += result.__str__()

        t = string.Template(template)
        t = t.substitute(Student=self.student,
                         Test='Test 1')

        t += '\nYour total score on Test 1 is:\n'
        for total in self.totals:
            t += '  ' + total + '\n'

        return t


class Deduction(object):

    def __init__(self, points_for_deduction, rubric, points_deducted):
        self.points_for_deduction = points_for_deduction
        self.rubric = rubric
        self.points_deducted = points_deducted

    def __str__(self):
        return self.rubric + ' - Points deducted: ' + str(self.points_deducted)


def main():
    """ Calls the   TEST   functions in this module. """
    make_emails_from_spreadsheet('Grades.txt')


def make_emails_from_spreadsheet(spreadsheet_file, separator='\t'):
    results = get_results_from_spreadsheet(spreadsheet_file, separator)
    emails = make_emails_from_results(results)
#     send_emails(emails)


def get_results_from_spreadsheet(spreadsheet_file, separator='\t'):
    """
    Opens the given TAB-separated file: Each line is a row with
    N columns (same N for all rows), with TABs separating the columns.
    Assumes that the file format is XXX.
    Returns a dictionary whose keys are student usernames and whose
    values are a list of comments for the student.
    """
    table = read_spreadsheet(spreadsheet_file, separator)
    students = get_students(table)
    problems = get_problems(table)
    totals = get_totals(table)

    results = []
    for student in students:
        print(student)  # To watch the program running.
        student_result = StudentResult(student)
        results.append(student_result)

        student_column = table[0].index(student)
        for problem in problems:
            problem_result = ProblemResult(problem)
            problem_result.score = get_score(problem,
                                             student_column,
                                             table)

            problem_result.deductions = get_deductions(problem,
                                                       student_column,
                                                       table)
            problem_result.comments = get_comments(problem,
                                                   student_column,
                                                   table)
            student_result.problem_results.append(problem_result)

        for line in totals:
            student_result.totals.append(
                get_total(student_column, line, table))
#             print(student_result)  # To watch the program running.

    return results


def read_spreadsheet(spreadsheet_file, separator='\t'):
    """
    Given a tab (or other) separated text file,
    returns the table of data.
    Throws an Exception if not all rows have the same number of columns.
    """
#     with open(spreadsheet_file, 'r', encoding='utf16') as f:
    with open(spreadsheet_file, 'r') as f:
        data = f.read()

    table = []
    number_of_columns = None
    for line in data.split('\n'):
        if line.strip() == '':
            continue  # Skip empty lines
        line = remove_extra_quotes(line)
        data = line.split(separator)
        if not number_of_columns:
            number_of_columns = len(data)
        else:
            if len(data) != number_of_columns:
                message = 'Bad file: Not all rows have the same number'
                message += 'of columns'
                raise Exception(message)
        table.append(data)

    return table


def get_students(table):
    """ Returns a list of student usernames in the given table. """
    # CONSIDER: Make the implementation more general than this.
    usernames = table[0][FIRST_USERNAME_COLUMN:]
    while '' in usernames:
        usernames.remove('')

    return usernames


def get_problems(table):
    """ Returns a list of Problems in the given table. """
    problems = []
    for k in range(1, len(table)):
        row = table[k]
        problem_name = row[0].strip()
        scoring = row[1].strip()
        rubric = row[2].strip()
        # This row ...
        if problem_name.startswith('Statistics'):
            # ... ends the problems
            break
        elif problem_name and not scoring:
            # ... begins a new Problem.
            problem = Problem(problem_name)
            problems.append(problem)
        elif problem_name and scoring:
            # ... indicates the points possible for the Problem.
            problem.points_available = scoring
        elif scoring == '' and rubric.startswith('Points earned'):
            # ... indicates the points earned on the Problem.
            problem.line_with_score = k
        elif scoring == '' and rubric.startswith('Total'):
            # ... indicates a Total line, skip it for now.
            pass
        elif scoring == '0':
            # ... is a row for a comment (no score deduction)
            problem.lines_for_comments.append(k)
        else:
            # ... is a row for a deduction of points
            problem.lines_for_deductions.append(k)

    return problems


def get_totals(table):
    """
    Returns a list of line numbers for lines
    that contain Totals in the given table.
    """
    totals = []
    for k in range(1, len(table)):
        row = table[k]
        scoring = row[1].strip()
        rubric = row[2].strip()
        # This row ...
        if scoring == '' and rubric.startswith('Total'):
            # ... indicates a Total line.
            totals.append(k)

    print(totals)
    return totals


def get_score(problem, column, table):
    row = problem.line_with_score
    return table[row][column]


def get_deductions(problem, column, table):
    deductions = []
    for line_number in problem.lines_for_deductions:
        entry = table[line_number][column].strip()
        if entry != '':
            deductions.append(Deduction(table[line_number][1],
                                        table[line_number][2],
                                        entry))

    return deductions


def get_comments(problem, column, table):
    comments = []
    for line_number in problem.lines_for_comments:
        entry = table[line_number][column].strip()
        comment = table[line_number][2].strip()
        if entry != '':
            comments.append(comment)

    return comments


def get_total(student_column, row, table):
    note = table[row][2]
    score = table[row][student_column]
    return note + ': ' + str(score)


# def add_comments_for_row(row, comments, students):
#     """
#     For each student in the comments dictionary, add this row's comment
#     to that students comments if it applies to that student.
#     """
#     for k in range(len(students)):
#         student_column = k + FIRST_USERNAME_COLUMN
#         student = students[k]
    # CONSIDER: Make the IF rule more general than this:
#         if row[0] and not row[1]:
#             comments[student].append(
#         elif row[student_column]:
#             if (row[2].strip().startswith('Sum of errors') and
#                     row[student_column].strip() == '0'):
#                 continue
#             else:
#                 data = row[:FIRST_USERNAME_COLUMN] + [row[student_column]]
#                 comments[student].append(data)


def remove_extra_quotes(line):
    temp = 'TEMPORARY_QUOTE_QUOTE_MARKER'
    while '""' in line:
        line = line.replace('""', temp)
    while '"' in line:
        line = line.replace('"', '')
    while temp in line:
        line = line.replace(temp, '"')

    return line


def make_emails_from_results(results):
    with open('results-to-email.txt', 'w', encoding='utf8') as f:
        for result in results:
            f.write(result.__str__())
            f.write('\n')


import smtplib

from email.message import EmailMessage
from email.headerregistry import Address


def send_emails():
    return
    msg = EmailMessage()
    msg['Subject'] = "Testing from david m."
    msg['From'] = Address("David Mutchler", "mutchler@rose-hulman.edu")
    msg['To'] = (Address("David Mutchler", "mutchler@rose-hulman.edu"),)
    msg.set_content("""\
Testing to see if this works.
""")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('David.Mutchler@gmail.com', 'sandynathan')
    server.send_message(msg)


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
