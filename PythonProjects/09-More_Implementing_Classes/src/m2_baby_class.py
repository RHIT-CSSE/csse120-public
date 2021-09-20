"""
A   Baby   class and functions that use/test it.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random


def main():
    """ Runs the tests of the   Baby   class. """
    print("UN-comment the following TESTS, one by one, when you are ready.")
    # UN-comment the following, one by one, when you are ready to TEST.
    # run_test_1()
    # run_test_2()


###############################################################################
# TODO: 2.  In this module you will implement and test a   Baby  class.
#           Here is an OVERVIEW of the steps you will take to do so.
#  _
#    Step 2 (this step): Read this overview of this module.
#    Step 3: Read and understand the SPECIFICATION for the  Baby  class.
#    Step 4: Read and understand the TESTS for the  Baby  class.
#              We supplied those tests.
#    Step 5: IMPLEMENT and TEST the Baby class.
#  _
#  Once you understand this OVERVIEW, mark this _TODO_ as DONE.
###############################################################################

###############################################################################
# TODO: 3. SPECIFICATION (read the following):
#   Here (below) are the methods that you must implement in your Baby class:
#  ----------------------------------------------------------------------------
#  _
#   Constructor method (that is, the   __init__  method):
#      What comes in:
#         -- self
#         -- a string for the name of the Baby
#      What goes out:  Nothing (i.e., None).
#      Side effects:
#         -- Prints "Hello baby <your baby's name>!"
#         -- Sets instance variables as needed
#              [YOU FIGURE OUT WHAT IS NEEDED AS YOU IMPLEMENT THE METHODS!]
#      Example:
#          b = Baby("McKinley")
#      causes the following to be printed on the Console:
#          Hello baby McKinley!
#  _
#   feed_baby:
#      What comes in:
#         -- self
#      What goes out:  Nothing (i.e., None).
#      Side effects:
#         -- Prints "Thank you for feeding baby <your baby's name>."
#         -- Modifies instance variables as needed.
#      Example:
#          b = Baby("Joshua")
#          b.feed_baby()
#      causes the following to be printed on the Console:
#          Hello baby Joshua!
#          Thank you for feeding baby Joshua.
#  _
#   hour_passes
#      What comes in:
#         -- self
#      What goes out:  Nothing (i.e., None).
#      Side effects:
#       -- If this is the FIRST time this method has been called
#          since this Baby was created or last fed, then this method prints:
# 	         "Baby <your baby's name> is sleeping."
#  _
#       -- If this is the SECOND time this method has been called
#          since baby was created or last fed, then this method prints:
# 	         "Baby <your baby's name> is awake.  Time for food."
#  _
#       -- If this is the THIRD (OR MORE) time this method has been called
#          since baby was created or last fed, then this method prints:
#            "Baby <your baby's name> is CRYING uncontrollably!  Feed the Baby!"
#  _
#       -- Modifies instance variables as needed.
#  _
#      Examples:  See the two TEST functions below.
#  _
#  You may find it helpful to read the two TEST functions (below) at this time.
#  If reading the TEST functions below does not make this specification clear,
#     ASK QUESTIONS AS NEEDED to clarify this specification.
#  _
#  Once you understand this SPECIFICATION, mark this _TODO_ as DONE.
###############################################################################

###############################################################################
# TODO: 4. TESTS (read the following):
#  The two functions that follow this comment TEST the Baby class.
#  For each of those two functions:
#    1. READ the CODE in the function.
#         As you do so, PREDICT what the code will cause to be printed.
#    2. READ the doc-string for the function.
#         It shows the CORRECT output when the function runs.
#    3. CONFIRM that you understand WHY the function's CODE produces
#         the OUTPUT that the doc-string says that it will.
#  _
#     If you do not understand why the CODE produces the OUTPUT as written
#     in the function's doc-string, STOP HERE and ASK QUESTIONS AS NEEDED.
#     Do  ** NOT **  attempt to write the  Baby  class
#     without fully understanding both of its test functions.
#  _
#  Once you fully understand the TESTS below, mark this _TODO_ as DONE.
###############################################################################
def run_test_1():
    """
    Running this test should cause EXACTLY the following
    to be displayed (i.e. printed) on the Console:

            ------------ Running test #1: ------------
            Hello baby Joshua!
            Baby Joshua is sleeping.
            Baby Joshua is awake.  Time for food.
            Baby Joshua is CRYING uncontrollably!  Feed the Baby!
            Baby Joshua is CRYING uncontrollably!  Feed the Baby!

            Thank you for feeding baby Joshua.
            Baby Joshua is sleeping.
            Baby Joshua is awake.  Time for food.

            Thank you for feeding baby Joshua.
            Baby Joshua is sleeping.

            Thank you for feeding baby Joshua.
            Baby Joshua is sleeping.
            Baby Joshua is awake.  Time for food.
            Baby Joshua is CRYING uncontrollably!  Feed the Baby!

    Examine the code in this test to be sure that you understand
    WHY it causes the above to be printed.
    """
    print()
    print('------------ Running test #1: ------------ ')
    b = Baby("Joshua")
    b.hour_passes()
    b.hour_passes()
    b.hour_passes()
    b.hour_passes()

    print()  # Just to make the output easier to read.
    b.feed_baby()
    b.hour_passes()
    b.hour_passes()

    print()  # Just to make the output easier to read.
    b.feed_baby()
    b.hour_passes()

    print()  # Just to make the output easier to read.
    b.feed_baby()
    b.hour_passes()
    b.hour_passes()
    b.hour_passes()


def run_test_2():
    """
    Running this test should cause EXACTLY the following
    to be displayed (i.e. printed) on the Console:

            ------------ Running test #2: ------------
            Hello baby McKinley!
            Hello baby Keegan!

            --- Iteration #1 ---
            Baby Keegan is sleeping.
            Thank you for feeding baby McKinley.
            Baby McKinley is sleeping.
            Baby McKinley is awake.  Time for food.
            Baby McKinley is CRYING uncontrollably!  Feed the Baby!
            Baby McKinley is CRYING uncontrollably!  Feed the Baby!
            Thank you for feeding baby McKinley.
            Baby McKinley is sleeping.
            Baby McKinley is awake.  Time for food.

            --- Iteration #2 ---
            Baby Keegan is awake.  Time for food.
            Thank you for feeding baby McKinley.
            Baby McKinley is sleeping.
            Baby McKinley is awake.  Time for food.
            Baby McKinley is CRYING uncontrollably!  Feed the Baby!
            Baby McKinley is CRYING uncontrollably!  Feed the Baby!
            Thank you for feeding baby McKinley.
            Baby McKinley is sleeping.
            Baby McKinley is awake.  Time for food.

            --- Iteration #3 ---
            Baby Keegan is CRYING uncontrollably!  Feed the Baby!
            Thank you for feeding baby McKinley.
            Baby McKinley is sleeping.
            Baby McKinley is awake.  Time for food.
            Baby McKinley is CRYING uncontrollably!  Feed the Baby!
            Baby McKinley is CRYING uncontrollably!  Feed the Baby!
            Thank you for feeding baby McKinley.
            Baby McKinley is sleeping.
            Baby McKinley is awake.  Time for food.

    Examine the code in this test to be sure that you understand
    WHY it causes the above to be printed.
    """
    print()
    print('------------ Running test #2: ------------ ')

    mckinley = Baby("McKinley")
    keegan = Baby("Keegan")

    for k in range(3):
        print()  # Just to make the output easier to read.
        print("--- Iteration #{} ---".format(k + 1))

        keegan.hour_passes()
        mckinley.feed_baby()

        for j in range(4):
            mckinley.hour_passes()

        mckinley.feed_baby()
        mckinley.hour_passes()
        mckinley.hour_passes()


###############################################################################
# TODO: 5.
#   Implement the entire   Baby  class
#     (including its 3 methods: __init__, feed_baby, and hour_passes)
#     below this comment.
#  _
#   Here is a reminder for the syntax (notation) to define a new class:
#      class NameOfClass(object):
#          """ Brief description of what an object of the class 'is'. """
#  _
#   AFTER you have implemented the ENTIRE   Baby   class,
#   un-comment (one-by-one) the calls in   main   to the two tests
#   and confirm that the tests produce the output that the doc-strings
#   for the tests show as the CORRECT output.
#  _
#      Fix errors as needed!  Do not hesitate to ASK QUESTIONS AS NEEDED.
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
