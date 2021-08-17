"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the RoseBot class (the top-level class for a robot).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Fall term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_touch_sensor
import rosebot_color_sensor
import rosebot_drive_system
import rosebot_arm_and_claw

###############################################################################
#    RoseBot class.
#
# NOTE TO STUDENTS:
#   You should construct a  RoseBot  object for the Snatch3r robot.
#   Do ** NOT ** construct any instances of any other classes in this module,
#   since a RoseBot constructs instances of all the sub-systems that provide
#   ALL of the functionality available to a Snatch3r robot.
#
#   Use those sub-systems (and their instance variables)
#   to make the RoseBot (and its associated Snatch3r robot) do things.
###############################################################################
class RoseBot(object):
    def __init__(self):
        # TODO: Implement this class with your instructor.
        self.touch_sensor = rosebot_touch_sensor.TouchSensor(1)
        self.color_sensor = rosebot_color_sensor.ColorSensor(3)
        self.drive_system = rosebot_drive_system.DriveSystem('A', 'B')
        self.arm_and_claw = rosebot_arm_and_claw.ArmAndClaw('C',
                                                            self.touch_sensor)
