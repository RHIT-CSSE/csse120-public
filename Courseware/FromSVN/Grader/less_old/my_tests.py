'''
Created on Dec 25, 2016

@author: david
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        print('hello')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
