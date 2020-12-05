"""
This module demonstrates   MUTATION   of a LIST in two ways:
  -- From an assignment in main.
  -- From within a function call.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, and their colleagues.
"""
# -----------------------------------------------------------------------------
# Students: Read and run this program in the debugger to watch
#           assignment and mutation in action.  This is a contrived
#           example that we are using only to show the elements
#           of mutation with simple code.
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
