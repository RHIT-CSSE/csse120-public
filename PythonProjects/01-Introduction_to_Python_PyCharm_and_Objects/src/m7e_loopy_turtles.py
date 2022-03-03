"""
Demonstrates:
  -- LOOPS (doing something repeatedly) and
  -- using OBJECTS
via Turtle Graphics.

Concepts include:
  -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
  -- Make an object   ** DO **   something by using a METHOD.
  -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.

 * LOOPS:
   -- Using a FOR expression like this:
         for k in range(41):
             blah
             blah
             blah

     The above repeats the body of the FOR expression 41 times.
     The name  k  is:
            0 the first time the body runs,
       then 1 the next time the body runs,
       then 2 the next time the body runs,
         etc
       then 40 the last time the body runs.
     Note how the BODY of the loop (the code that is repeated 41 times)
     is INDENTED 4 spaces.

 * ASSIGNMENT and NAMES
  -- ASSIGNING a VALUE to a NAME (aka VARIABLE), as in these examples:
        jack = 45
        jill = "ran down the hill"
        size = size - 12
        sponge_bob = rg.SimpleTurtle()

 * The DOT trick: If you type an expression and then PAUSE after typing
     the DOT (period, full stop), then the window that pops up gives
     lots of clues for what you can do!  For example:
        rg.
        rg.SimpleTurtle().
        rg.Pen().
        rg.PaintBucket().

Authors: David Mutchler, Rachel Krohn, Dave Henthorn, Scott McClellan,
   Yiji Zhang, Mark Hays, Vibha Alangar, Matt Boutell, Dave Fisher,
   Sriram Mohan, Amanda Stouder, Mohammed Noureddine, Steve Chenoweth,
   Valerie Galluzzi, Curt Clifton, their colleagues and
         PUT_YOUR_NAME(S)_HERE.
"""
import rosegraphics as rg

###############################################################################
# TODO: 1.  This is an EXAMPLE module (m1e_..., note the e).
#  For ALL example modules, throughout the course:
#    a. RUN the example.
#    b. READ the code (and accompanying comments), ASKING QUESTIONS
#         about anything that is not clear to you.  In particular, be sure that
#         you understand why the code produces the output/drawing that it does.
#  _
#  From here on, we will not put a _TODO_ in EXAMPLE modules,
#  but we nonetheless expect you to DO them, per the above.
#  _
#  If you have not already done so, READ the doc-string that forms the
#  first 49 lines of this module, noting the examples and discussion therein.
#  _
#  After you RUN this example, READ its code, and ASK QUESTIONS about anything
#  that is not clear to you, change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# One window, for two examples.
###############################################################################
window = rg.TurtleWindow()

###############################################################################
# Example 1.
###############################################################################
blue_turtle = rg.SimpleTurtle("turtle")
blue_turtle.pen = rg.Pen("midnight blue", 3)
blue_turtle.speed = 20  # Fast

# The first square will be 300 x 300 pixels, per the next line and line 88:
size = 300

# Do the indented code 6 times.  Each time draws a square.
for k in range(6):
    # Draw a square of the given size:
    blue_turtle.draw_square(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    size = size - 12

###############################################################################
# Example 2.  It shows how to speed up the animation.
#   Run the example as it is, then in   window.tracer(10)   below,
#   change the 10 to 100, run again, and observe the effect.
###############################################################################
window.tracer(10)  # Bigger numbers make the animation run faster

another_turtle = rg.SimpleTurtle("triangle")
another_turtle.pen = rg.Pen("magenta", 1)
another_turtle.backward(50)

# The name k takes on the values 0, 1, 2, ... 499 as the loop runs 500 times.
for k in range(500):
    another_turtle.left(91)
    another_turtle.forward(k)

# -----------------------------------------------------------------------------
# The next line keeps the window open until the user clicks in the window.
# Whenever you are doing TurtleGraphics code, this  close_on_mouse_click   line
# should be the LAST line in the module.  DO NOT ADD CODE BELOW THIS LINE!
# -----------------------------------------------------------------------------
window.close_on_mouse_click()
