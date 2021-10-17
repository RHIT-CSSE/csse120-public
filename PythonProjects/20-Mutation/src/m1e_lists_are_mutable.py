"""
This module demonstrates   MUTATION   of a LIST in two ways:
  -- From an assignment in main.
  -- From within a function call.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, and their colleagues.
"""


# -----------------------------------------------------------------------------
# Students: You might like to run this program in the debugger as you read it,
# stepping from line to line to watch assignment and mutation in action.
#
# This is a contrived example whose purpose is only to show
# the concepts behind assignment and mutation, using simple code.
# This module mutates LISTS; the next module mutates OBJECTS.
# -----------------------------------------------------------------------------


def main():
    # -------------------------------------------------------------------------
    # 1. Constructs a list, assigning it a value.
    # 2. Assigns an ELEMENT in the list a new value,
    #    thus MUTATING the LIST (because an ELEMENT in it was ASSIGNED).
    # -------------------------------------------------------------------------
    numbers = [45, 100, 8]
    numbers[2] = 99
    print(numbers)  # To see that the INSIDES of   numbers   has changed

    # -------------------------------------------------------------------------
    # 3. Mutates the list again, this time from within a function call.
    # -------------------------------------------------------------------------
    mutate_numbers(numbers)
    print(numbers)  # To see that the INSIDES of   numbers   has changed

    # -------------------------------------------------------------------------
    # 4. Assigns another variable to refer to the same list
    #       to which the    numbers   variable refers.
    # 5. Re-assigns the   numbers   variable to refer to another list.
    # This is ASSIGNMENT and NOT mutation.
    # -------------------------------------------------------------------------
    numbers2 = numbers
    numbers = [4, 4, 4, 4, 4]

    print(numbers, numbers2)  # Prints the two DIFFERENT lists

    # -------------------------------------------------------------------------
    # Shows the difference between the   is   operator
    #    (two things refer to the same place in memory)
    # and the   ==   operator (two things contain the same data).
    # -------------------------------------------------------------------------
    numbers3 = [1, 2, 3]
    numbers4 = [1, 2, 3]
    numbers5 = numbers3

    print(numbers3 is numbers4)  # False
    print(numbers3 == numbers4)  # True

    print(numbers3 is numbers5)  # True
    print(numbers3 == numbers4)  # True


def mutate_numbers(numbers):
    numbers[2] = -1


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
