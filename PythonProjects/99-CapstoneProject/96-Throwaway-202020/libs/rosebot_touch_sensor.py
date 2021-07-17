"""
THROW-AWAY Capstone Project. If you mess up this THROW-AWAY project,
  ** no worries. **
It lets you practice skills & concepts needed for the REAL Capstone Project.

This module contains a   TouchSensor   class that contains methods
relevant to a physical Touch Sensor plugged into a port.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# -----------------------------------------------------------------------------
# NOTE to students: Start this exercise WITH YOUR INSTRUCTOR.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 1.  If you have not already done so, with your instructor,
#  READ and UNDERSTAND the  HowToShareModules.pdf  document in this project.
#    -- If you understand it, change this _TODO_ to DONE.
#    -- Otherwise, ** do NOT modify this module **
#         and get help before continuing.
#  _
#  Throughout this module, ** use the process in HowToShareModules.pdf. **
#  _
#  In particular, *** only ONE team member should modify this file ***
#    (but often pair-programming using the same computer).
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 2. Change the   PUT_YOUR_NAMES_HERE   above to the names of
#  EACH team member who contributes (in any way) to this module.
#  _
#  REMINDER: Use ONLY ** ONE ** team member's computer to make changes herein.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 3. With your instructor, import the modules needed herein:
#    from . import rosebot_ev3dev_api as rose_ev3
#    import time
#  Make sure you understand WHY those imports are needed.
# -----------------------------------------------------------------------------


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
        ---
        :param port:  The port (1, 2, 3, or 4) into which a Touch Sensor is
                      plugged, or None to attempt to autodetect such a port.
        :type port: int | None
        """
        # ---------------------------------------------------------------------
        # TODO: 4. With your instructor, implement this method.
        # ---------------------------------------------------------------------

    def get_reading(self):
        """
        Returns the current reading (1 for pressed, 0 for not-pressed)
        of the physical Touch Sensor associated with this TouchSensor.
        ---
        :rtype: int
        """
        # ---------------------------------------------------------------------
        # TODO: 5. With your instructor, implement this method.
        # ---------------------------------------------------------------------

    def is_pressed(self):
        """
        Returns True if the physical Touch Sensor associated with this
        TouchSensor is pressed, else returns False.
        ---
        :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: 6. With your instructor, implement this method.
        # ---------------------------------------------------------------------

    def wait_until_pressed(self):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the physical Touch Sensor to be pressed.
        """
        # ---------------------------------------------------------------------
        # TODO: 7. Implement this method
        #          (with help from your instructor as needed).
        # ---------------------------------------------------------------------

    def wait_until_released(self):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the physical Touch Sensor to be released.
        """
        # ---------------------------------------------------------------------
        # TODO: 8. Implement this method
        #          (with help from your instructor as needed).
        # ---------------------------------------------------------------------

