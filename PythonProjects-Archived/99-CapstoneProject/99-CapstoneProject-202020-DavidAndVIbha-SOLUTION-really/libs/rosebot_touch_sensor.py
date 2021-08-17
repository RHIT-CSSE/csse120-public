"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This code defines the   TouchSensor   class  that is used
for the physical Touch Sensor that is plugged into the robot.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note below how to write an IMPORT statement
#  that imports a module that is in the  LIBS  sub-folder.
#  This module uses code that is in the "low-level" api in rosebot_ev3dev_api.
#  Change this _TODO_ to DONE after you have seen how to do it.
# -----------------------------------------------------------------------------
import libs.rosebot_ev3dev_api as ev3dev
import time


###############################################################################
#    TouchSensor
###############################################################################
class TouchSensor(object):
    """
    Associated with a physical Touch Sensor that is plugged into a port
    (1, 2, 3, or 4).  Its methods include:
       get_reading    is_pressed    wait_until_pressed   wait_until_released
    """
    def __init__(self, port=None):
        """
        Constructs the underlying low-level version of this sensor.
        Doing so enforces the requirement:
          The  port  must be 1, 2, 3, 4, or None, where  None  means to attempt
          to autodetect a port into which a physical Touch Sensor is plugged.

        :type port: int | None
        """
        # ---------------------------------------------------------------------
        # TODO: 3. Read the following, ASKING QUESTIONS AS NEEDED.
        #  Once you understand the code, change this _TODO_ to DONE.
        # ---------------------------------------------------------------------
        self._low_level_touch_sensor = ev3dev.LowLevelTouchSensor(port)

    def get_reading(self):
        """
        Returns the current reading (1 for pressed, 0 for not-pressed)
        of the physical Touch Sensor associated with this TouchSensor.
        ---
        :rtype: int
        """
        # ---------------------------------------------------------------------
        # TODO: 4. Implement this method, using code like this:
        #      self._low_level_touch_sensor.YOU_FIGURE_OUT_WHAT_GOES_HERE
        #  The "dot trick" should make it clear what to put in the YOU_FIGURE...
        # ---------------------------------------------------------------------
        return self._low_level_touch_sensor.get_reading()

    def is_pressed(self):
        """
        Returns True if the physical Touch Sensor associated with this
        TouchSensor is pressed, else returns False.
        ---
        :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: 5. Implement this method, using code that includes a call
        #   to this TouchSensor object's   get_reading   method (see above).
        # ---------------------------------------------------------------------
        return self.get_reading() == 1

    def wait_until_pressed(self):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop
        (in order to avoid "flooding" the actual Touch Sensor's hardware),
        waiting for the physical Touch Sensor to be pressed.
        """
        # ---------------------------------------------------------------------
        # TODO: 6. Implement this method, using code that includes a call
        #   to this TouchSensor object's   is_pressed   method (see above).
        # ---------------------------------------------------------------------
        while True:
            if self.is_pressed():
                break
            time.sleep(0.05)

    def wait_until_released(self):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop
        (in order to avoid "flooding" the actual Touch Sensor's hardware),
        waiting for the physical Touch Sensor to be released.
        """
        # ---------------------------------------------------------------------
        # TODO: 7. Implement this method, using code that includes a call
        #   to this TouchSensor object's   is_pressed   method (see above).
        # ---------------------------------------------------------------------
        while True:
            if not self.is_pressed():
                break
            time.sleep(0.05)