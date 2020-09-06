"""
Demonstrates using (calling) STRING methods,
and using the DOT trick to discover them.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """
    Tests the other functionns in this module, by running them.
    """
    strings_1("help me Edgar")
    print("The above should have printed:")
    print("hZlp mZ Zdgar")
    print()

    strings_1("Ello, here be eeees and ZEEZEE.")
    print("The above should have printed:")
    print("Zllo, hZrZ bZ ZZZZs and zZZzZZ.")

    strings_1("abcdef ABCDEF")
    print("The above should have printed:")
    print("abcdZf abcdZf")


def strings_1(string):
    """
    Prints the given string, but with:
      -- All characters converted to lower case, and then
      -- Each occurrence of   e   replaced by   Z.
    For example:
      strings_1("help me Edgar")   prints   hZlp mZ
      strings_1("Hello, here be eeees.")   prints   HZllo, hZrZ bZ ZZZZs.
    Type hints:
      :type string: str
    """
    ###########################################################################
    # TODO: 2. Implement and test this function, per its doc-string above.
    #   The testing code (in main) is already written for you.
    #  _
    #    NOTE: This function requires
    #      ** exactly 3 lines **
    #    If you think it needs more, ** ASK FOR HELP. **
    #    HINT: see   jump_and_move_turtle   above.
    ###########################################################################
    string.title()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

main()
