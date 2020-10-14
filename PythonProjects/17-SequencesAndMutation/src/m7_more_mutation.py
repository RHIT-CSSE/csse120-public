"""
This module lets you practice   MUTATION   of objects
by changing the values of instance variables.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    run_test_RETURN_circle()
    run_test_MUTATE_circle()


def run_test_RETURN_circle():
    """ Tests the   RETURN_circle   function. """
    print()
    print('-----------------------------------------')
    print('Testing RETURN_circle:')
    print('-----------------------------------------')

    print()
    print('See the graphics window for this test.')
    print('If an error msg appears at any point,')
    print('then you have FAILED this test.')

    # -------------------------------------------------------------------------
    # Tests 1 and 2 (on one window):
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(500, 400, 'Testing RETURN_circle')
    text = rg.Text(rg.Point(250, 125), '')
    text.attach_to(window)

    circle = rg.Circle(rg.Point(200, 300), 50)
    circle.fill_color = 'blue'

    circle.attach_to(window)

    msg = 'Note: If you see an error message at ANY point,\n'
    msg = msg + 'then you have failed this test.\n\n'
    msg = msg + 'I have drawn the original, blue circle.\n\n'
    msg = msg + 'So you should see a BLUE circle below\n'
    msg = msg + '(and nothing else).\n\n'
    msg = msg + 'Click the mouse to continue this test.\n'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    new_circle = RETURN_circle(circle, 'red')

    if new_circle:
        new_circle.attach_to(window)

    msg = 'I have now called your   RETURN_circle   function\n'
    msg = msg + 'and drawn the CLONED, RED circle that your\n'
    msg = msg + 'RETURN_circle   function should have returned.\n\n'
    msg = msg + 'So you should see a RED circle below\n'
    msg = msg + '(and nothing else, since the blue circle\n'
    msg = msg + 'is beneath the red circle).\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    if new_circle:
        new_circle.detach_from(window)

    msg = 'I have now UN-drawn the CLONED, RED circle.\n\n'
    msg = msg + 'So you should see the original, BLUE circle below\n'
    msg = msg + '(and nothing else).\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    circle.detach_from(window)

    msg = 'I have now UN-drawn the ORIGINAL, blue circle.\n\n'
    msg = msg + 'So you should see NO circles below.\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    if new_circle:
        new_circle.attach_to(window)

    msg = 'Now I have RE-drawn the CLONED, RED circle\n'
    msg = msg + 'that your   RETURN_circle   function\n'
    msg = msg + 'should have returned.\n\n'
    msg = msg + 'So you should see a RED circle below\n'
    msg = msg + '(and nothing else).\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    # -------------------------------------------------------------------------
    # Note: The following statements make the variable  new_circle
    #       refer to a new, green circle.  So we can no longer refer
    #       to the RED circle (to which the variable  new_circle  once
    #       referred).  But the red circle still exists!
    # -------------------------------------------------------------------------

    new_circle = RETURN_circle(circle, 'green')

    if new_circle:
        new_circle.attach_to(window)

    msg = 'Now I have ALSO drawn the CLONED, GREEN circle\n'
    msg = msg + 'that your   RETURN_circle   function\n'
    msg = msg + 'should have returned.\n\n'
    msg = msg + 'So you should see a GREEN circle below\n'
    msg = msg + '(and nothing else, since the red circle\n'
    msg = msg + 'is beneath the green circle).\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    if new_circle:
        new_circle.detach_from(window)

    msg = 'I have now UN-drawn the CLONED, GREEN circle.\n\n'
    msg = msg + 'So you should see the cloned, RED circle below\n'
    msg = msg + '(and nothing else).\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    new_circle2 = RETURN_circle(rg.Circle(rg.Point(250, 350), 25),
                                'white')

    if new_circle:
        new_circle.attach_to(window)
    if new_circle2:
        new_circle2.attach_to(window)

    msg = 'I have now RE-drawn the CLONED, GREEN circle.\n'
    msg = msg + 'Additionally, I called your   RETURN_circle   function\n'
    msg = msg + 'again, asking it to return a smaller WHITE circle\n'
    msg = msg + 'that is below and to the right of the other circles.\n\n'
    msg = msg + 'So you should see a GREEN circle below\n'
    msg = msg + 'and a smaller WHITE circle below and to its right\n'
    msg = msg + '(but NOT the red circle, since it\n'
    msg = msg + 'is beneath the green circle).\n\n'
    msg = msg + 'Click the mouse to conclude this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    window.close()


def RETURN_circle(circle, color):
    """
    Returns a NEW rg.Circle that is a CLONE (copy) of the given circle,
    but with its color set to the given color.

    This function must NOT mutate the given circle or color.

    Preconditions:
      :type circle:  rg.Circle
      :type color: str | rg.Color
    where the color is either a string that Rosegraphics understands
    or a rg.Color object.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. First, READ THE ABOVE TEST CODE.
    #          Make sure that you understand it.
    #          Then, IMPLEMENT and test THIS FUNCTION
    #          (using the above code for testing).
    #  HINT: Use the   clone   method to make the copy.
    # -------------------------------------------------------------------------


def run_test_MUTATE_circle():
    """ Tests the   MUTATE_circle   function. """
    print()
    print('-----------------------------------------')
    print('Testing MUTATE_circle:')
    print('-----------------------------------------')

    print()
    print('See the graphics window for this test.')
    print('If an error msg appears at any point,')
    print('you have failed this test.')

    # Tests 1 and 2 (on one window):
    window = rg.RoseWindow(500, 450, 'Testing MUTATE_circle')
    text = rg.Text(rg.Point(250, 125), '')
    text.attach_to(window.initial_canvas)

    circle = rg.Circle(rg.Point(250, 300), 50)
    circle.fill_color = 'yellow'

    circle.attach_to(window.initial_canvas)

    msg = 'Note: If you see an error message at ANY point,\n'
    msg = msg + 'then you have failed this test.\n\n'
    msg = msg + 'I have drawn the original, yellow circle.\n\n'
    msg = msg + 'So you should see a YELLOW circle below\n'
    msg = msg + '(and nothing else).\n\n'
    msg = msg + 'Click the mouse to continue this test.\n'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    result = MUTATE_circle(circle, 'pink', 200)

    msg = 'I have called your   MUTATE_circle   function.\n'
    msg = msg + 'It should have MUTATED the (sole) circle to be pink\n'
    msg = msg + 'and 200 units to the right of where it was.\n\n'
    msg = msg + 'So you should see (only) a PINK circle below,\n'
    msg = msg + 'almost touching the right side of the window.\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    if result is not None:
        msg = msg + '\n\nERROR: You returned a value! Wrong!!!'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    circle.detach_from(window.initial_canvas)

    msg = 'I have now UN-drawn the (sole) circle.\n\n'
    msg = msg + 'So you should see NO circles below.\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    circle.attach_to(window.initial_canvas)

    msg = 'Now I have RE-drawn the (now pink) circle.\n\n'
    msg = msg + 'So you should see (only) a PINK circle below,\n'
    msg = msg + 'just touching the right side of the window.\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    result = MUTATE_circle(circle, 'black', -400)

    msg = 'I have called your   MUTATE_circle   function again.\n'
    msg = msg + 'It should have MUTATED the (sole) circle to be black\n'
    msg = msg + 'and 400 units to the left of where it was.\n\n'
    msg = msg + 'So you should see (only) a BLACK circle below,\n'
    msg = msg + 'just touching the left side of the window.\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    if result is not None:
        msg = msg + '\n\nERROR: You returned a value! Wrong!!!'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    another_circle = rg.Circle(circle.center, 25)
    another_circle.fill_color = 'red'
    another_circle.attach_to(window.initial_canvas)

    msg = 'I have constructed and drawn another circle.\n'
    msg = msg + 'It is red and smaller than the black circle,\n'
    msg = msg + 'and currently centered on the black circle.\n\n'
    msg = msg + 'So you should now see a BLACK circle below,\n'
    msg = msg + 'just touching the left side of the window,\n'
    msg = msg + 'with a smaller red circle on top of the black circle.\n\n'
    msg = msg + 'Click the mouse to continue this test.'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    result = MUTATE_circle(another_circle, 'white', 65)

    msg = 'I have called your   MUTATE_circle   function again.\n'
    msg = msg + 'It should have MUTATED the small, red circle to be white\n'
    msg = msg + 'and 65 units to the left of where it was.\n\n'
    msg = msg + 'So you should see a BLACK circle below,\n'
    msg = msg + 'just touching the left side of the window,\n'
    msg = msg + 'with a WHITE circle slightly overlapping the black one.\n\n'
    msg = msg + 'Click the mouse to conclude this test.'
    if result is not None:
        msg = msg + '\n\nERROR: You returned a value! Wrong!!!'
    text.text = msg
    window.render(0.5)
    window.get_next_mouse_click()

    window.close()


def MUTATE_circle(circle, color, n):
    """
    MUTATES the given circle, so that:
      1. its fill color becomes the given color, and
      2. it is centered   n   pixels to the right of where it was centered.

    This function must NOT construct any new circles.
    This function must NOT return anything (other than the default None).

    Precondition: The first argument is a rg.Circle and the second
                  argument is a color appropriate for RoseGraphics.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. First, READ THE ABOVE TEST CODE.
    #          Make sure that you understand it.
    #          Then, IMPLEMENT and test THIS FUNCTION
    #          (using the above code for testing).
    #   HINT: This function can be implemented with just TWO lines of code.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
