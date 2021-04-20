"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         many others before them, and now PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  Read and run this program, examining the code and the output.
#           Then answer the questions below, writing answers in this comment.
#  __
#   1. Briefly describe how the output from  example_1
#      differs from the output from  example_2.
#  __
#   2. Do you understand what the optional   end   parameter for PRINT does?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#   3. Do you believe that you can you READ and TRACE BY HAND
#      simple nested loops like the examples in this module?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#  After you have completed the above, change the above _TODO_ to DONE.
#  As always,  *** GET HELP AS NEEDED.  ***
###############################################################################


def main():
    """ Calls the other functions to demonstrate them. """
    example_1(4, 7)
    example_2(6)
    example_3(5, 9)


def example_1(n, m):
    """ Prints the loop variables of a loop within a loop. """
    # -------------------------------------------------------------------------
    # Classic nested-loops, type 1:
    #    The number of inner-loop iterations does NOT depend
    #    on the current value of the outer-loop variable.
    # -------------------------------------------------------------------------
    print()
    print("-----------------------------")
    print("Classic example 1:")
    print("-----------------------------")

    for k in range(n):
        for j in range(m):
            print(k, j)
        print("Completed the inner loop {} times".format(k + 1))


def example_2(n):
    """ Prints the loop variables of a loop within a loop. """
    # -------------------------------------------------------------------------
    # Classic nested-loops, type 2:
    #    The number of inner-loop iterations DOES depend
    #    on the current value of the outer-loop variable.
    # -------------------------------------------------------------------------
    print()
    print("-----------------------------")
    print("Classic example 2:")
    print("-----------------------------")

    for k in range(n):  # The ONLY difference from the previous
        for j in range(k + 1):  # example is   k+1   on this line.
            print(k, j)
        print("Completed the inner loop {} times".format(k + 1))


def example_3(n, m):
    """ Prints the loop variables of a loop within a loop. """
    # -------------------------------------------------------------------------
    # Same as classic example 1, but shows how to have successive PRINT
    # statements cause output on the SAME line, and then go to the NEXT line.
    # -------------------------------------------------------------------------
    print()
    print("-----------------------------")
    print("Classic example 3:")
    print("-----------------------------")

    for k in range(n):
        print(k, end=":  ")  # Note the   end=":  "  which replaces newline.
        for j in range(m):
            print(" ", j, end="")  # Note   end=""   which causes no newline.
        print("Completed the inner loop {} times".format(k + 1))


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
