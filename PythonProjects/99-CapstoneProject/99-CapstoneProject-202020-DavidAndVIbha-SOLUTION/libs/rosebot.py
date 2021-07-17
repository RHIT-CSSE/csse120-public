"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This code defines the   RoseBot   class (the top-level class for a robot).
In the code that you write for making a robot do things,
you should construct a   RoseBot   object and then use it as in this example:

------------------------------------------------
import libs.rosebot as rb

def main():
   robot = rb.RoseBot()
   robot.drive_system.go(100, -40)
   robot.touch_sensor.wait_until_pressed()
   etc
------------------------------------------------

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of ALL the members of your team,
#  and make sure that ALL the members of your team READ this module!

# -----------------------------------------------------------------------------
# TODO: 2. Note below how to write an IMPORT statement
#  that imports a module that is in the  LIBS  sub-folder.
#  Change this _TODO_ to DONE after you have seen how to do it.
# -----------------------------------------------------------------------------
import libs.rosebot_drive_system as drive
import libs.rosebot_touch_sensor as touch
import libs.rosebot_arm_and_claw as arm


###############################################################################
#    RoseBot.
###############################################################################
class RoseBot(object):
    """ The top-level class for making a robot do things. """
    def __init__(self):
        """
        Constructs instances of each of the sub-systems of a Snatch3r robot
        and sets instance variables to them.
        """
        # ---------------------------------------------------------------------
        # TODO: 3. Once you understand the following code
        #  (ASK QUESTIONS AS NEEDED), change this _TODO_ to DONE.
        # ---------------------------------------------------------------------
        self.drive_system = drive.DriveSystem("B", "C")
        self.touch_sensor = touch.TouchSensor(1)
        self.arm_and_claw = arm.ArmAndClaw(self.touch_sensor)
