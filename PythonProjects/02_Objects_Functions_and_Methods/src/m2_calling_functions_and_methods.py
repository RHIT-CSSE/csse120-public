"""
Permits exploration of CALLING FUNCTIONS and CALLING METHODS.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# TODO: 2.
#   Do this module while you watch the Session 2 Preparation video for
#       m2_calling_functions_and_methods
#   Do the exercises in this module when the video says to do so.
#  _
#   After you have read and understood the above instructions,
#   mark this _TODO_ as DONE and continue to the next _TODO_.
###############################################################################

###############################################################################
# Part 1: Calling FUNCTIONS.
###############################################################################

###############################################################################
# TODO: 3.  [Do this when the video says to do so.]
#   Recall that a FUNCTION gives a NAME to a block of code,
#   and can have (and usually does have) PARAMETERS that receive values
#   from actual ARGUMENTS when the method/function is CALLED.
#  _
#   Put a statement at the beginning of this module (near line 10)
#   that imports the   math   module.
#  _
#   Then, below this _TODO, put statements that call functions defined
#   in the math module to PRINT each of the following.
#   Run the program after typing each, to test your statements one by one:
#     -- the cosine of 2.5
#     -- the degrees that is the equivalent of -0.5 radians
#     -- The base-2 logarithm of the constant   e   where you use the math
#          module to access the value of the constant   e.
#     -- The result of applying the   factorial   function to the argument 100,
#          that is,   100!
#     -- The result of applying the   lgamma     function to the argument 3.1.
#   After you do the last of the above, hover over the function name  lgamma
#   to see its Quick Documentation.
###############################################################################

###############################################################################
# TODO: 4.  [Do this when the video says to do so.]
#   Type the statements needed to print a random integer between 100 and 1000,
#   using the   random.randint   function to do so.
#   Run the program to test your statements.
#  _
#   After doing so, bring up the Quick Documentation for random.randint.
###############################################################################

###############################################################################
# TODO: 5.  [Do this when the video says to do so.]
#   Below this _TODO, put statements that call functions defined
#   in the   builtins   module to do each of the following,
#   running the program after typing each, to test your statements one by one:
#     -- the absolute value of a random integer between -100 and 100
#     -- the smallest of 4 randomly-chosen integers between 1 and 20
#   The result will be different each time you run the program,
#   because of the randomness.
###############################################################################

###############################################################################
# TODO: 6.  [Do this when the video says to do so.]
#   The code below defines a function that returns the temperature
#   in Celsius of a given temperature in Fahrenheit.
#   BELOW that function definition, write code that prints:
#     -- the temperature in Celsius of 1000 degrees Fahrenheit
#     -- the temperature in Celsius of -80 degrees Fahrenheit
###############################################################################
def get_celsius(temperature_in_fahrenheit):
    """
    Returns the temperature in Celsius of the given Fahrenheit temperature.
    For example, this function returns   XXX   when given   YYY.

    Type hints:
      :type temperature_in_fahrenheit: float
    """
    return (temperature_in_fahrenheit - 32) * (5 / 9)

###############################################################################
# Part 2: Calling METHODS.
###############################################################################

###############################################################################
# TODO: 7.  [Do this when the video says to do so.]
#   METHODs are just like FUNCTIONs except that a METHOD is associated
#   with a CLASS.
#  _
#   Put a statement at the beginning of this module (near line 11)
#   that imports the   rosegraphics   module, using   rg   as shorthand for it.
#  _
#   Then, below this _TODO, put statements that:
#     -- constructs a   RoseWindow   object
#          (where RoseWindow is defined in the   rosegraphics   module),
#     -- applies the   close_on_mouse_click   method to that RoseWindow object.
#   Run the program to test your statements.
#  _
#   Then, BETWEEN the two statements that you just wrote,
#   write a statement that prints the position of the mouse
#   when the mouse is clicked inside the RoseWindow object.
#   Run the program to test your statement.
#  _
#   Then, repeat that same   print   statement 5 more times.
#     (Use a FOR loop if you happen to remember how to do so.)
#   Run the program to test your statements.
#  _
#   After you do the last of the above, hover over the
#   method name   get_next_mouse_click   to see its Quick Documentation.
###############################################################################
