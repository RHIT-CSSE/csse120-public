"""
This module demonstrates that  TUPLES  and  STRINGS  are IMMUTABLE:
  -- Attempts to mutate them cause run-time errors.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, and their colleagues.
"""


# -----------------------------------------------------------------------------
# Students: You might like to run this program in the debugger as you read it,
# stepping from line to line to watch assignment and mutation in action.
#
# It attempts to mutate a STRING, which THROWS AN EXCEPTION (crashes).
# Later, it attempts to mutate a TUPLE, which THROWS AN EXCEPTION (crashes).
#
# This is a contrived example whose purpose is only to show
# the concepts behind assignment and mutation, using simple code.
# -----------------------------------------------------------------------------


def main():
    # -------------------------------------------------------------------------
    # 1. Constructs a string, assigning it a value.
    # 2. Constructs a tuple, assigning it a value.
    # -------------------------------------------------------------------------
    s = "Hello"
    numbers = (45, 100, 8)

    print(s, numbers)

    # -------------------------------------------------------------------------
    # 3. Assigns the string a new value -- NO PROBLEM!
    # 4. Assigns the tuple a new value -- NO PROBLEM!
    # -------------------------------------------------------------------------

    s = "Goodbye"
    numbers = (55, 20)

    print(s, numbers)

    # -------------------------------------------------------------------------
    # 5. Attempts to re-assign the INSIDES of the string,
    #       that is, attempts to MUTATE the string.
    # 6. Attempts to re-assign the INSIDES of the tuple,
    #       that is, attempts to MUTATE the tuple.
    # These cause RUN-TIME errors.
    # -------------------------------------------------------------------------
    s[0] = 'X'  # After seeing the effect of this line, comment it out.
    numbers[2] = 77


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
