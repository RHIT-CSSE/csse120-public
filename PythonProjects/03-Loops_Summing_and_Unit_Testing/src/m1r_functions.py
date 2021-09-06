"""
This module lets you practice   TRACING BY HAND   FUNCTION CALLS
for functions whose definition we supplied.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.
#   1. READ the code below.
#   2. TRACE (by hand) the execution of the code,
#        predicting what will get printed.
#   3. Run the code and compare your prediction to what actually was printed.
#   4. Decide whether you are 100% clear on the CONCEPTS and the NOTATIONS for:
#        -- DEFINING a function that has PARAMETERS
#        -- CALLING a function with actual ARGUMENTS.
#  _
#  ****************************************************************************
#      If you are NOT 100% clear on the above concepts,
#      ask your instructor or a student assistant about them during class.
#  ****************************************************************************
#  _
#  After you have completed the above, mark this _TODO_ as DONE.
###############################################################################


def main():
    hello("Grace Hopper")
    goodbye("Ada Lovelace")
    hello("Mataric")
    hello("Rus")
    hello_and_goodbye("One", "Two")
    hello_and_goodbye("Two", "One")


def hello(friend):
    print("Hello,", friend, "- how are things?")


def goodbye(friend):
    print("Goodbye,", friend, "- see you later!")


def hello_and_goodbye(person1, person2):
    hello(person2)
    goodbye(person1)


main()
