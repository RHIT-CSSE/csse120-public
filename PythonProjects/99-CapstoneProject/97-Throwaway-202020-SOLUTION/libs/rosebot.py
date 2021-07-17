"""
THROW-AWAY Capstone Project. If you mess up this THROW-AWAY project,
  ** no worries. **
It lets you practice skills & concepts needed for the REAL Capstone Project.

This module contains a   RoseBot   class that is the same as the full RoseBot
class that you will implement later, but restricted to the objects that
are relevant to this THROW-AWAY project.

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
#    but TEAM-PROGRAMMING (with your ENTIRE TEAM) using the same computer.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 2. Change the   PUT_YOUR_NAMES_HERE   above to the names of
#  EACH team member who contributes (in any way) to this module.
#  _
#  REMINDER: Use ONLY ** ONE ** team member's computer to make changes herein.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 3. With your instructor, import the modules needed herein:
#     from . import rosebot_drive_system as drive_system
#     from . import rosebot_touch_sensor as touch_sensor
#     from . import rosebot_arm_and_claw as arm_and_claw.
#  Make sure you understand WHY those imports are needed.
#  Make sure you understand that constructing a   RoseBot   object provides
#    access to ALL the sub-systems of a Snatch3r robot needed
#    in this THROW-AWAY project.
# -----------------------------------------------------------------------------
# SOLUTION CODE: Delete later.
import libs.rosebot_drive_system as drive_system
import libs.rosebot_touch_sensor as touch_sensor


###############################################################################
#    RoseBot.
###############################################################################
class RoseBot(object):
    """ The top-level class for making a robot do things. """
    def __init__(self):
        """
        Constructs instances of each of the sub-systems of a Snatch3r robot
        relevant to this THROW-AWAY project and sets instance variables to them:
          self.drive_system   using ports "B" and "C"
          self.touch_sensor   using port 1
        """
        # ---------------------------------------------------------------------
        # TODO: 4. With your instructor, implement this method.
        # ---------------------------------------------------------------------
        # SOLUTION, delete for final version:
        self.drive_system = drive_system.DriveSystem("B", "C")
        self.touch_sensor = touch_sensor.TouchSensor(1)
