"""
The goal of this module is to again use the  rose_ev3  library,
but with a sensor and to make sounds.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosebot_ev3dev_api as rose_ev3
import time


def main():
    # -------------------------------------------------------------------------
    # TODO: 2. Read the code below and run it.
    #  Then right-click on   ColorSensor   in the code below and select
    #    Go To -> Implementation(s)
    #  so that you can understand what a ColorSensor can do.
    #  ASK QUESTIONS AS DESIRED.
    #  Change the above _TODO_ to DONE when you know how to:
    #    -- Construct a ColorSensor plugged into port 3.
    #    -- Read the name of the color that the ColorSensor currently senses.
    #  (The code below may help you understand these.)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 3. Add Motor objects (per the previous module) and make the Motor
    #   objects do interesting things depending on the color sensed.
    #   For example, when the robot sees "black", have the robot move forward
    #   for a while, then back for a while, and when the robot sees "white",
    #   have the robot spin in place for a while.
    # -------------------------------------------------------------------------
    color_sensor = rose_ev3.ColorSensor(3)

    k = 0
    while True:
        k = k + 1  # Include counter to help see new readings (when same color)
        counter = str(k) + "."

        color = color_sensor.get_color_as_name()

        print(counter, color)
        time.sleep(1)  # So that we are not overwhelmed by the output.

    # -------------------------------------------------------------------------
    # TODO: 4. Construct a  ToneMaker  object BEFORE the above loop.
    #   Look at its implementation (right-click on ToneMaker, Go To -> Impl...)
    #   to see what a ToneMaker can do.  (Warning: the code is in beta state.)
    #  _
    #   Make your ToneMaker play a tone (try 500) for a while (try 250 for 1/4
    #   of a second), using the   play_tone  method.
    #  _
    #   Once you have played one tone, consider making a loop
    #   that causes a sequence of tones to play.  Be sure to put a time.sleep
    #   that is greater than the duration of the tone after each play_tone
    #   function call.  (There are better approaches, more on those later.)
    #   The documentation shows how to play a fun song, if you are so inclined.
    # -------------------------------------------------------------------------

main()
