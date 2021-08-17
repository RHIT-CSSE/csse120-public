"""
This module demonstrates simple loops of the form:
   for k in range(blah):
      ... k ...

Authors: Many, many people over many, many years.
         David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Amanda Stouder, Derek Whitley, and their colleagues wrote this version.
"""
# -----------------------------------------------------------------------------
# Students: Read and run this program.
#           Make sure that you understand all 3 examples.
# -----------------------------------------------------------------------------


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    example1()
    example2()
    example3()


def example1():
    """ Prints a message, then   0  1  2  3  ... 7. """
    print()
    print("--------------------------------------------------")
    print("Running example1:")
    print("--------------------------------------------------")
    for k in range(8):
        print(k)


def example2():
    """ Prints a message, then  0  5  10  15  20 ... 50. """
    print()
    print("--------------------------------------------------")
    print("Running example2:")
    print("--------------------------------------------------")
    for k in range(11):
        print(5 * k)


def example3():
    """ Prints a message, then  1  4  7  10  13  16. """
    print()
    print("--------------------------------------------------")
    print("Running example3:")
    print("--------------------------------------------------")
    for k in range(6):
        print(1 + (3 * k))


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
