"""
Demonstrates using OBJECTS via Turtle Graphics.

Concepts include:
  -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
  -- Make an object   ** DO **   something by using a METHOD.
  -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.

Also:
  -- Making a NAME (aka VARIABLE) refer to an object, aka ASSIGNMENT,
     that is, ASSIGNING the NAME a VALUE that is a reference to the OBJECT,
     as in    x = math.sqrt(3.14)     and     p = Point(50, 22)

Authors: David Mutchler, Rachel Krohn, Dave Henthorn, Scott McClellan,
   Yiji Zhang, Mark Hays, Vibha Alangar, Matt Boutell, Dave Fisher,
   Sriram Mohan, Amanda Stouder, Mohammed Noureddine, Steve Chenoweth,
   Valerie Galluzzi, Curt Clifton, their colleagues and
         PUT_YOUR_NAME(S)_HERE.
"""
###############################################################################
# TODO: 1.
#   Yes, that means for YOU to DO something per the following instruction:
#      On Line 18 above, replace   PUT_YOUR_NAME(S)_HERE   with your OWN name.
#  _
#   BTW, the top block of text above forms a multiple-line string that is
#   called a DOC-STRING.  It documents what this module does, in a way that
#   other programs can make sense of.  It has no other effect on this program.
#  _
#   Once you have done the above, change this _TODO_ to DONE
#   and  ** continue to the next _TODO_ (below). **
###############################################################################

import rosegraphics as rg

###############################################################################
# TODO: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#  _
#     In the Project window (to the left), right click on the   src   folder,
#     then select   Mark Directory As  ~  Sources Root.
#  _
#   You will see that  rosegraphics  in the  import  statement above (line 33)
#   is no longer marked as an error.  You will do this "Mark Directory As" step
#   in all projects that use rosegraphics, so get used to it. :)
#  _
#   Once you have done the above, change this _TODO_ to DONE
#   and  ** continue to the next _TODO_ (below). **
###############################################################################

###############################################################################
# TODO: 3.
#   Run this module.  A window will pop up and Turtle objects will move around.
#   After the Turtles stop moving,
#      ** click anywhere in the window to close the window **.
#  _
#   Then look at the code below and determine which lines of code cause
#   what visual effects when the code runs.
#     ** ASK FOR HELP WHEN YOU HAVE QUESTIONS ABOUT WHAT THE CODE IS DOING, **
#     **      or if you just are curious about any of the code.             **
#  _
#   Once you believe you understand which code causes what visual effects
#   when the code runs, change this _TODO_ to DONE
#   and  ** continue to the next _TODO_ (below). **
###############################################################################

###############################################################################
# TODO: 4.
#   Review the code below one more time to be SURE
#   that you understand the notations for:
#  _
#     -- CONSTRUCTING an INSTANCE of a CLASS, e.g.
#           rg.SimpleTurtle()           [NOTE the PARENTHESES!]
#  _
#     -- Making a NAME (aka VARIABLE) refer to the resulting OBJECT
#        (that is, to the INSTANCE of the class), e.g.
#           natasha = rg.SimpleTurtle()
#        We call this ASSIGNMENT, and we sometimes say:
#           Assign the NAME a VALUE, where the VALUE is a REFERENCE
#           to an OBJECT.
#  _
#     -- Applying a METHOD to an object to make the object DO something, e.g.
#           natasha.forward(100)
#  _
#     -- Accessing an INSTANCE VARIABLE of an object, e.g.
#           natasha.speed = 10           [NOTE the ABSENCE of PARENTHESES!]
#           boris.speed = natasha.speed
#        to access/set DATA associated with the object.
#  _
#   After you are confident that you understand all the code below,
#   change this _TODO_ to DONE and  ** continue to the next _TODO_ (below). **
###############################################################################

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - CONSTRUCT (make and initialize) a   TurtleWindow   object for animation.
# The definition of a  TurtleWindow is in
# the   rg   (shorthand for rosegraphics) module that is IMPORTED above.
# -----------------------------------------------------------------------------
window = rg.TurtleWindow()
window.delay(20)  # Bigger numbers mean slower animation.

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - CONSTRUCT (make and initialize) a  SimpleTurtle  object
#     and make a NAME REFER to the object by using ASSIGNMENT.
# -----------------------------------------------------------------------------
boris = rg.SimpleTurtle()

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - Ask the SimpleTurtle object to do things by applying a METHOD to it.
# The numbers in the parentheses are called ARGUMENTS.
# -----------------------------------------------------------------------------
boris.forward(100)
boris.left(90)
boris.forward(200)

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - Construct a second SimpleTurtle
#       (using an optional argument that sets the shape displayed),
#   - set its  pen  and  speed  INSTANCE VARIABLES, and
#   - ask it to do things.
#
# TIP:  to see what other strings you can use for the shape, hover over
# the word   SimpleTurtle  in the first line of code below.  Doing so will
# pop up some quick documentation about whatever you hover upon -- try it!
# -----------------------------------------------------------------------------
natasha = rg.SimpleTurtle(shape="turtle")
natasha.pen = rg.Pen("red", 30)  # Second argument is the thickness of the Pen
natasha.speed = 5  # Bigger means faster, max is usually about 10

natasha.backward(50)
natasha.right(90)
natasha.forward(125)

natasha.speed = 1  # Now slower
natasha.pen.thickness = 8  # and thinner.
natasha.go_to(rg.Point(-100, 200))

###############################################################################
# TODO: 5.
#   Your instructor will explain (live, or in a Follow-Me video)
#   the so-called "dot-trick", which means to type an expression,
#   then a DOT (period), then PAUSE.  Try it out yourself by typing
#      natasha.
#   somewhere below and then pausing after typing the dot.
#   You will see options pop up for what natasha can do (methods, marked
#   with an M on the pop-up) and what natasha knows (instance variables,
#   aka fields, marked with a F on the pop-up).
#  _
#   Try out one of the methods!  Any is fine (but those with a visual
#   effect will be most interesting).  Experiment!
#      -- But stop looking when the "dot trick" list starts showing names
#           that begin begin with an UNDERSCORE (e.g. __init__),
#           since those are "system" things not meant to be used directly.
#           More on them later in the course.
#      -- Also notice that when you type the first few letters of a name
#           (here, natasha), PyCharm offers to "autofill" the rest of the name
#           for you -- just press the ENTER (RETURN) key to do so.  Try it out!
#  _
#      ** Be quick to ask for help as needed, as the so-called **
#      ** "dot-trick" is more easily shown than explained. **
#  _
#   As always, test by running the module.
###############################################################################

###############################################################################
# TODO: 6.
#   Add a few more lines of your own code to make one of the existing
#   SimpleTurtle objects move some more AND have different characteristics.
#  _
#      ** Nothing fancy is required. **
#      ** A SUBSEQUENT exercise will let you show your creativity. **
#  _
#   As always, test by running the module.
###############################################################################

###############################################################################
# TODO: 7.
#   The above code  CONSTRUCTS  two SimpleTurtle objects
#   and gives those objects NAMES:
#       boris    natasha
#  _
#   Add code of your own that constructs another SimpleTurtle object,
#   naming it whatever you want.  Names cannot have spaces or special
#   characters, but they can have digits and underscores, e.g.
#      this_1_has
#  _
#   STYLE RULES (obey these rules!!!):
#     1. Your names should always begin with a LOWER_CASE letter.
#          So   mary   is OK   but   Mary   is NOT OK.
#     2. Choose short-but-meaningful names.  Separate "words" in the name by
#          underscores, like this:   my_turtle1
#  _
#   Then add more code that:
#     -- Constructs a  Pen  object,
#     -- Assigns your SimpleTurtle's  pen  to the constructed Pen object, and
#     -- Makes your SimpleTurtle move around a bit.
#  _
#      ** Nothing fancy is required. **
#      ** A SUBSEQUENT exercise will let you show your creativity. **
#  _
#      ** Do not hesitate to ask for help as needed! **
#  _
#   As always, test by running the module.
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

# -----------------------------------------------------------------------------
# The next line keeps the window open until the user clicks in the window.
# Throughout this exercise, this  close_on_mouse_click   line
# should be the LAST line in the module.  DO NOT ADD CODE BELOW THIS LINE!
# -----------------------------------------------------------------------------
window.close_on_mouse_click()
