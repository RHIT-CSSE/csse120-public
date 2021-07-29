"""
A very simple class to make running tests a bit simpler.
There are much stronger frameworks possible; this is a KISS framework.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.  October 2015.
"""

import testing_helper


class SimpleTestCase(object):
    """
    A SimpleTestCase is a test to run.  It has:
      -- The function to test,
      -- its argument(s), and
      -- its correct returned value.
    """

    def __init__(self, function, arguments, correct_returned_value):
        """
        The arguments are:
          -- The function to test
          -- The arguments to use in the test, as a sequence
          -- The correct returned value.

        For example, if the intended test is:
           foo(blah1, blah2, blah3)
        with correct returned value True,
        then its SimpleTestCase would be construced by:
          SimpleTestCase(foo, [blah1, blah2, blah3], True)

        Note that the arguments must be a SEQUENCE even if there is
        only a single argument and an EMPTY sequence if there are no
        arguments.  For example:
          foo(blah)   with correct returned value 88
        would be constructed by:
          SimpleTestCase(foo, [blah], 88)
        """
        self.function_to_test = function
        self.arguments_to_use = arguments
        self.correct_returned_value = correct_returned_value

    def run_test(self):
        """
        Runs this test, printing appropriate messages.
        Returns True if your code passed the test, else False.
        Does not attempt to catch Exceptions.
        """
        your_answer = self.function_to_test(*(self.arguments_to_use))

        print()

        if your_answer == self.correct_returned_value:
            result = 'PASSED'
            testing_helper.print_colored(
                'Your code {:6} this test'.format(result), color='blue')
        else:
            result = 'FAILED'
            testing_helper.print_colored(
                'Your code {:6} this test'.format(result), color='red')

        if len(self.arguments_to_use) == 0:
            format_string = '  ( )'
        else:
            f_beginning = '  {}( {} '
            f_args = ', {}' * (len(self.arguments_to_use) - 1)
            format_string = f_beginning + f_args + ' )'
        print(format_string.format(self.function_to_test.__name__,
                                   *(self.arguments_to_use)))

        print('  The correct returned value is:',
              self.correct_returned_value)
        print('  Your code returned ..........:', your_answer)

        return (your_answer == self.correct_returned_value)

    @staticmethod
    def run_tests(function_name, tests):
        print()
        print('--------------------------------------------------')
        print('Testing the   {}   function:'.format(function_name))
        print('--------------------------------------------------')

        failures = 0
        for k in range(len(tests)):
            result = tests[k].run_test()
            if result is False:
                failures = failures + 1

        if failures > 0:
            print()
            testing_helper.print_colored(
                '************************************', color='red')
            testing_helper.print_colored(
                '*** YOUR CODE FAILED SOME TESTS. ***', color='red')
            testing_helper.print_colored(
                '************************************', color='red')
