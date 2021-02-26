'''
Created on Mar 3, 2014

@author: mutchler
'''
import unittest
import lines_of_code

import os.path

TEST_FOLDER = 'testData'

class Test(unittest.TestCase):

    def run_file_test(self, method_to_test,
                      file_with_test_string, file_with_answer_string):
        # Read file
        test_file = TEST_FOLDER + '/' + file_with_test_string
        f = open(test_file, 'r')
        before = f.read()
        f.close()

        # Run test on the test string.
        after = method_to_test(before)

        # If the file with the (correct) answer string exist,
        # get that answer string.
        answer_file = TEST_FOLDER + '/' + file_with_answer_string
        if os.path.isfile(answer_file):
            f = open(answer_file, 'r')
            correct = f.read()
            f.close()
        # Otherwise, write the result of the test to that answer file.
        else:
            f = open(answer_file, 'w')
            f.write(after)
            f.close()
            correct = after
            print(after)

        # Check whether the test passes.
        self.assertEqual(after, correct)


    def test_remove_whitespace_lines(self):
        self.run_file_test(lines_of_code.remove_whitespace_lines,
                           'data1.py', 'answer_whitespace1.py')
        self.run_file_test(lines_of_code.remove_whitespace_lines,
                           'data2.txt', 'answer_whitespace2.txt')

    def test_remove_docstrings(self):
        self.run_file_test(lines_of_code.remove_docstrings,
                           'data1.py', 'answer_docstring1.py')
        self.run_file_test(lines_of_code.remove_docstrings,
                           'data2.txt', 'answer_docstring2.txt')

    def test_remove_docstrings_and_whitespace(self):
        rem_doc = lines_of_code.remove_docstrings
        rem_ws = lines_of_code.remove_whitespace_lines
        rem_doc_ws = lambda s: rem_ws(rem_doc(s))
        self.run_file_test(rem_doc_ws,
                           'data1.py', 'answer_doc_ws1.py')
        self.run_file_test(rem_doc_ws,
                           'data2.txt', 'answer_doc_ws2.txt')

    def test_remove_comments(self):
        self.run_file_test(lines_of_code.remove_comments,
                           'data1.py', 'answer_comments1.py')
        self.run_file_test(lines_of_code.remove_comments,
                           'data2.txt', 'answer_comments2.txt')

    def test_remove_docstrings_comments_and_whitespace(self):
        rem_doc = lines_of_code.remove_docstrings
        rem_ws = lines_of_code.remove_whitespace_lines
        rem_comments = lines_of_code.remove_comments
        rem_doc_ws = lambda s: rem_ws(rem_comments(rem_doc(s)))
        self.run_file_test(rem_doc_ws,
                           'data1.py', 'answer_doc_comments_ws1.py')
        self.run_file_test(rem_doc_ws,
                           'data2.txt', 'answer_doc_comments_ws2.txt')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
