answer = 2 ** 5
print(answer * 100)

###############################################################################
# TODO: 1.
#      [Note: You saw this same _TODO_ in the Follow-Me m3f exercise.]
#   Read the 2 lines of code ABOVE this _TODO_.
#   When the Python INTERPRETER runs, that is, when this program runs,
#   it does the following with that code:
#  _
#     1. It runs line 1, that is, it:
#          a. Evaluates (runs, computes) 2 raised to the 5th power,
#             yielding the object that is the integer 32.
#          b. Makes the name   answer   refer to that object.
#  _
#        We say that "the name  answer  is ASSIGNED the value 32."
#        Names used in assignment statements are commonly called VARIABLES
#        (because their value can "vary" as the program runs).
#  _
#        Note that the RIGHT-hand-side of an assignment statement
#        is evaluated BEFORE the NAME on the LEFT-hand-side
#        gets ASSIGNED the result.
#  _
#     2. It runs line 2, that is, it:
#          a. Looks up the object to which the name   answer  refers
#               (i.e., the object 32).
#          b. Multiplies that object (32) by 100
#               (hence computing the object that is the integer 3,200).
#          c. Prints (that is, displays on the Run window)
#             the newly-computed object.  (It prints WITHOUT the comma.)
#  _
#   Make sure that you understand that those two lines accomplish the above,
#     ** ASKING QUESTIONS AS NEEDED. **
#   Once you completely understand the above, run this module,
#   confirming that it prints 3200.  Then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 2.
#      [Note: You saw this same _TODO_ in the Follow-Me m3f exercise.]
#   Some things, like addition (+) and subtraction (-), are built into
#   Python.  Others are defined in modules (aka libraries) that must be
#   IMPORTED into your program for you to use them.  The trigonometric functions
#   (e.g. cos, sin) are defined in the MATH module, so to use them, you must
#   IMPORT the math module by putting the following statement into your code:
#      import math
#   Such statements are traditionally put at the TOP of a module.
#   Go ahead and put an   import math   statement at the top of this module.
#  _
#   To access things defined in an imported module, we use the DOT notation,
#   like this:
#       math.sin
#   to refer to the sine function defined in the imported  math  module.
#  _
#   After putting your  import math  statement at the beginning of this module,
#   and keeping in mind how we use the DOT notation to refer to things defined
#   inside an imported module:
#      Immediately below this _TODO_, write code that:
#        a. Computes 77 plus the cosine of 2.75.
#               When you type   math.co   pause after typing the  "o"
#               and notice what pops up.  It will show you that
#               the name of the cosine function is NOT "cosine"; rather,
#               it is "cos".  Hence, you will type   math.cos(2.75)
#        b. Stores that computed value using a name of your own choosing.
#        c. Prints the square root of that computed value.
#               You will have to guess what function in the  math  module
#               is used for square roots.  Try typing:
#                   math.s
#               and pause after typing the "s" to see what pops up.
#               Do you see what function to use for square roots?
#               (If not, ask for help.)
#   The result printed should be about 8.7221.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 3.
#   Immediately below this _TODO_, write code that:
#     -- 1. Computes and stores in a variable the cosine of (0.12345).
#     -- 2. Multiplies that cosine by 1.0802 and stores it in a variable.
#     -- 3. Raises that result to the 3.03165 power and stores it in a variable.
#             Hint: use the   **   operator for raising to a power.
#     -- 4. Prints that result (it should be about 1.234567).
#     -- 5. Rounds that result to 6 decimal places and stores it in a variable.
#            -- Hint: Here is an example of using the ROUND function
#               to round math.pi to 5 decimal places:   round(math.pi, 5)
#     -- 6. Prints that result (it should be exactly 1.2343567).
#  _
#   Use as few or as many intermediate names as you feel appropriate.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 4.
#   Immediately below this _TODO_, write code that repeats the previous _TODO_
#   (ending up with the result 1.234567) but USING ONLY *ONE* VARIABLE
#   in your entire solution.  Hint. RE-use that single variable multiple times!
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 5.
#   Immediately below this _TODO_, write code that makes the variable defined
#   in the preceding _TODO_ increase by 1 (so printing that variable should
#   then yield 2.34567).
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 6.
#   Immediately below this _TODO_, write code that computes and prints:
#     1. the base-10 logarithm of 1,000,000    (which is 6, as you know)
#     2. the base-2 logarithm of 1,000,000     (which is a bit less than 20)
#     3. the base-3 logarithm of 1,000,000     (which is between 6 and 20)
#   For all three, use the relevant function in the  math  module,
#   and discover the name of that function by typing:
#      math.l   (pausing after the "l" and noting what pops up)
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

#############################################################################
# TODO: 7.
#   Immediately below this _TODO_, write code that computes and prints:
#     1. The cosine of 90.
#     2. The cosine of math.pi / 2.
#   Run your code (fix errors as needed).
#   Then decide, from what gets printed, whether the trigonometric functions
#   in the   math  module use degrees or radians.
#     ** As always, ASK QUESTIONS AS NEEDED! **
#   Then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 8.
#   Ensure that no blue bars remain on the scrollbar-thing to the right.
#   Run one more time to be sure that all is still OK.
#  _
#   Then COMMIT-and-PUSH your work as before:
#     1. Select    Git     from the menu bar (above).
#     2. Choose   Commit...   from the pull-down menu that appears.
#     3. In the   "Commit to master"   window that pops up,
#        press the   "Commit and Push..."   button.
#            Note: If it asks you to "Specify commit message", do so
#                  using   Done   or something like that for the message.
#  _
#   You can COMMIT-and-PUSH as often as you like.
#   DO IT FREQUENTLY - AT LEAST once per module.
###############################################################################
