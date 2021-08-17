"""
This module tests   m3_calling_functions_returning_values.
You do NOT need to understand all of the code in this module,
but you should be able to pass all of its tests.

Authors: Mark Hays and others.
"""
###############################################################################
# Do not change this file.
# Tt is intended only as a way to check your code.
###############################################################################

import m4_calling_functions_returning_values as m4
import sys
from io import StringIO


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_of_digits()
    run_test_digits_in_cube()
    run_test_digits_in_power()
    run_test_fancy_sums_of_digits()


###############################################################################
# Do not worry about understanding the code below this line.
# It is used to test your code cleanly, but you are not expected to
# understand how it works at this point.
###############################################################################

def run_test_sum_of_digits():
    """ Tests the  sum_of_digits  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_of_digits   function:')
    print('--------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([826], 16, "", [826])
    testCases.addTestCase([83135], 20, "", [83135])
    testCases.addTestCase([1000000], 1, "", [1000000])
    runTestOnMethod(m4.sum_of_digits, testCases, "sum_of_digits")


def run_test_digits_in_cube():
    """ Tests the   digits_in_cube   function. """
    print()
    print('-----------------------------------------------------')
    print('Testing the   digits_in_cube   function:')
    print('-----------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([5], 8, "", [5])
    testCases.addTestCase([12], 18, "", [12])
    testCases.addTestCase([255], 36, "", [255])
    testCases.addTestCase([10000], 1, "", [10000])
    runTestOnMethod(m4.digits_in_cube, testCases, "digits_in_cube")


def run_test_digits_in_power():
    """ Tests the   digits_in_power   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   digits_in_power   function:')
    print('--------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([12, 3], 18, "", [12, 3])
    testCases.addTestCase([255, 3], 36, "", [255, 3])
    testCases.addTestCase([2, 10], 7, "", [2, 10])
    testCases.addTestCase([1, 10000], 1, "", [1, 10000])
    runTestOnMethod(m4.digits_in_power, testCases, "digits_in_power")


def run_test_fancy_sums_of_digits():
    """ Tests the  fancy_sums_of_digits  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   fancy_sums_of_digits   function:')
    print('--------------------------------------------------')
    testCases = TestCaseCollection()
    testCases.addTestCase([10], 1, "", [10])
    testCases.addTestCase([2], 19084, "", [2])
    testCases.addTestCase([35], 124309, "", [35])
    runTestOnMethod(m4.fancy_sums_of_digits, testCases,
                    "fancy_sums_of_digits")


def runTestOnMethod(function, testCases, function_name):
    numTests = len(testCases.expectedPrints)
    total = numTests * 2 + (len(testCases.args[0]) * numTests)
    resultsToPrint = ""
    correct = 0
    old_stdout = sys.stdout
    try:
        for k in range(numTests):
            sys.stdout = mystdout = StringIO()
            ep = testCases.expectedPrints[k]
            er = testCases.expectedReturns[k]
            ea = testCases.expectedArgumentsAfter[k]
            argList = testCases.args[k]
            actualReturn = None
            if (len(argList) == 0):
                actualReturn = function()
            elif (len(argList) == 1):
                actualReturn = function(argList[0])
            elif (len(argList) == 2):
                actualReturn = function(argList[0], argList[1])

            actualPrint = mystdout.getvalue()

            if (actualReturn == er):
                correct += 1
            else:
                fstring = 'Failure with arguments: {}\n'
                fstring += '  Returned value: {}\n'
                fstring += '  did not match\n'
                fstring += '  expected value: {}\n'
                resultsToPrint += fstring.format(testCases.args[k],
                                                 actualReturn,
                                                 er)

            if (actualPrint == ep):
                correct += 1
            else:
                fstring = 'Failure with arguments {}\n'
                fstring += '  Printed value:  {}\n'
                fstring += '  did not match\n'
                fstring += '  expected value: {}\n'
                resultsToPrint += fstring.format(testCases.args[k],
                                                 actualPrint,
                                                 ep)

            for i in range(len(testCases.args[k])):
                if (testCases.args[k][i] == ea[i]):
                    correct += 1
                else:
                    fstring = 'Failure with arguments: {}\n'
                    fstring += '  Argument value: {}\n'
                    fstring += '  after the function call did not match\n'
                    fstring += '  expected value: {}\n'
                    resultsToPrint += fstring.format(testCases.args[k],
                                                     testCases.args[k][i],
                                                     ea[i])

        sys.stdout = old_stdout
        # print(functionName, "Total:", str(correct) + "/" + str(total))

        print(resultsToPrint)
    except Exception as e:
        sys.stdout = old_stdout
        print("Exception occurred while executing test: ", e)
    finally:
        sys.stdout = old_stdout

    if correct == total:
        print(function_name, "COMPLETED SUCCESSFULLY!")
        return True
    else:
        print(function_name, "FAILED! See messages above.")
        return False


class TestCaseCollection():

    def __init__(self):
        self.expectedReturns = []
        self.expectedPrints = []
        self.expectedArgumentsAfter = []
        self.args = []

    def addTestCase(self, arguments, expectedReturn, expectedPrint,
                    expectedArgsAfter):
        self.args.append(arguments)
        self.expectedReturns.append(expectedReturn)
        self.expectedPrints.append(expectedPrint)
        self.expectedArgumentsAfter.append(expectedArgsAfter)

# -----------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
