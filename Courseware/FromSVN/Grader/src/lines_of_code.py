# FIXME: This file needs to be reworked!!!!!!!!!

"""
"""
# TODO: Put a comment above.

# Remove lines with only whitespace in them.

# Remove triply-quoted strings (single or double quotes, but matched)

# Remove comments (# sign to end of line)

# Count functions: def that begins in column 1.
# Count classes: class that begins in column 1.
# Also count lines that begin in column 1 but are NOT def/class: should
#   be 1 for if .. main, but no more (others are probably global vars).
# [TODO: classes and methods.  IGNORE nested defs.]

# For each def, count lines until next item in column 1.
# Store total such.

# Do the above for the initial version of the file (from instructor).
# Ditto for student version.  Report difference in loc.


class ModuleEvaluator:

    def __init__(self, student_contents, original_contents):
        self.student_contents = student_contents
        self.original_contents = original_contents

    def evaluate(self):
        if self.is_unchanged():
            return self

        return self

    def is_unchanged(self):
        if self.student_contents == self.original_contents:
            self.is_unchanged = True
        else:
            self.is_unchanged = False
        return self.is_unchanged


#         self.loc_all_lines = 0
#         self.loc_wo_whitespace = 0
#         self.loc_wo_whitespace_docstrings = 0
#         self.loc_wo_whitespace_docstrings_comments = 0
#         self.loc_gui = 0

#     def __repr__(self):
#         s = ''
#         for item in [self.student, self.module,
#                      self.loc_all_lines, self.loc_wo_whitespace]:
#             s = s + str(item) + ', '
#         return s


class WordCount():

    def __init__(self, text, lines=0, words=0, characters=0):
        """
        Computes and stores the number of lines, words and characters
        in the given text if text is not None, else stores
        the given values for lines, words and characters.
        :type lines: int
        :type words: int
        :type characters: int
        """
        self.text = text

        if text:
            self.lines = len(text.splitlines())
            self.words = len(text.split())
            self.characters = len(text)
        else:
            self.lines = lines
            self.words = words
            self.characters = characters

    def __repr__(self):
        return 'WordCount(None, {}, {}, {})'.format(self.lines,
                                                    self.words,
                                                    self.characters)

    def __str__(self):
        return '{:3} {:4} {:5}'.format(self.lines,
                                       self.words,
                                       self.characters)

    def minus(self, other):
        """
        Returns a WordCount that is this one minus the given other one.
        :type other: WordCount
        """
        return WordCount(None,
                         self.lines - other.lines,
                         self.words - other.words,
                         self.characters - other.characters)


class StatisticsForModule(object):

    def __init__(self,
                 original,
                 after_blank_lines_removed,
                 after_docstrings_removed,
                 after_comments_removed):
        """
        :type original: WordCount
        :type after_blank_lines_removed: WordCount
        :type after_docstrings_removed: WordCount
        :type after_comments_removed: WordCount
        """
        self.nothing_removed = original
        self.wo_blank_lines = after_blank_lines_removed
        self.wo_docstrings = after_docstrings_removed
        self.wo_comments = after_comments_removed

    def __repr__(self):
        format_string = 'StatisticsForModule({!r}, {!r}, {!r})'
        return format_string.format(self.nothing_removed,
                                    self.wo_blank_lines,
                                    self.wo_docstrings,
                                    self.wo_comments)

    def __str__(self):
        format_string = 'WordCount for file as given:  {}\n'
        format_string += 'After blank lines removed:    {}\n'
        format_string += 'After docstrings removed too: {}\n'
        format_string += 'After comments removed too:   {}\n'

        return format_string.format(str(self.nothing_removed),
                                    str(self.wo_blank_lines),
                                    str(self.wo_docstrings),
                                    str(self.wo_comments))

    def minus(self, other):
        """
        Returns a ModuleStatistics that is this ModuleStatistics
        minus the given other ModuleStatistics.
        :type other: ModuleStatistics
        """
        orig = self.nothing_removed.minus(other.nothing_removed)
        blanks = self.wo_blank_lines.minus(other.wo_blank_lines)
        docs = self.wo_docstrings.minus(other.wo_docstrings)
        comments = self.wo_comments.minus(other.wo_comments)

        return StatisticsForModule(orig, blanks, docs, comments)


def evaluate_module(module_name):
    contents = read_module(module_name)
    contents_wo_blank_lines = remove_whitespace_lines(contents)
    contents_wo_docstrings = remove_docstrings(contents_wo_blank_lines)
    contents_wo_comments = remove_comments(contents_wo_docstrings)
    stats = StatisticsForModule(WordCount(contents),
                                WordCount(contents_wo_blank_lines),
                                WordCount(contents_wo_docstrings),
                                WordCount(contents_wo_comments))

    return stats


def read_module(module_name):
    """ Returns the contents of the given filename. """
    with open(module_name, 'r') as file:
        return file.read()


def remove_whitespace_lines(s):
    """
    Returns a copy of the string s, but with all lines that contain
    only whitespace removed.
    """
    lines = s.split('\n')
    new_lines = []
    for line in lines:
        if len(line) > 0 and not line.isspace():
            new_lines.append(line)

    return '\n'.join(new_lines)


def remove_docstrings(s):
    """
    Returns a copy of the string s, but with all docstrings removed.
    It does NOT parse the file correctly for Python; instead,
    it simply removes all characters between matched pairs of
    triple-quotes (either single or double quotes).
    """
    IN_SINGLE_DOCSTRING = 0
    IN_DOUBLE_DOCSTRING = 1
    NOT_IN_DOCSTRING = 2

    state = NOT_IN_DOCSTRING
    result = ''
    index = 0
    while True:
        if state == NOT_IN_DOCSTRING:
            new_index1 = s.find('"""', index)
            new_index2 = s.find("'''", index)
            if new_index1 == -1 and new_index2 == -1:
                result = result + s[index:]
                break
            elif new_index2 == -1 or (new_index1 != -1 and new_index1 < new_index2):
                state = IN_DOUBLE_DOCSTRING
                new_index = new_index1
            else:
                state = IN_SINGLE_DOCSTRING
                new_index = new_index2
            result = result + s[index:new_index]
        elif state == IN_SINGLE_DOCSTRING:
            new_index = s.find("'''", index)
            if new_index == -1:
                break
            state = NOT_IN_DOCSTRING
        else:
            new_index = s.find('"""', index)
            if new_index == -1:
                break
            state = NOT_IN_DOCSTRING
        index = new_index + 3

    return result


def remove_comments(s):
    """
    Returns a copy of string s, but with all comments removed.
    It does NOT parse the file correctly for Python; instead,
    it simply removes all characters from a  #  sign to the end
    of the line with the  #  sign.
    """
    result = ''
    index = 0
    while True:
        comment_begin = s.find('#', index)
        if comment_begin == -1:
            result = result + s[index:]
            break
        result = result + s[index:comment_begin]
        end_of_line = s.find('\n', comment_begin)
        if end_of_line == -1:
            break
        index = end_of_line

    return result

# def main():
#     test_evaluate_module()
#
#
# def test_evaluate_module():
#     for m in ('xxx.txt', 'lines_of_code.py'):
#         stats = evaluate_module(m, 'david')
#         print(stats)
