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

Authors:  Your professors (for the framework).
Winter term, 2019-2020.
"""

###############################################################################
# STUDENTS:  *** READ this file. Understanding it is CRITICAL. ***
#            *** But do NOT change ANYTHING in this module. ***
###############################################################################

# -----------------------------------------------------------------------------
# Note below how to write an IMPORT statement
#  that imports a module that is in the  LIBS  sub-folder.
# -----------------------------------------------------------------------------
import libs.rosebot_drive_system as drive
import libs.rosebot_touch_sensor as touch
import libs.rosebot_arm_and_claw as arm
import libs.rosebot_leds as leds
import libs.rosebot_brick_buttons as bb
import libs.rosebot_remote_control as rc
import libs.rosebot_color_sensor as color
import libs.rosebot_infrared_proximity_sensor as proximity
import libs.rosebot_camera_sensor as camera
import libs.rosebot_sound as sound
import libs.rosebot_beacon_sensor as b_sensor

# -----------------------------------------------------------------------------
# The following import OPTIONAL modules, which you will implement or not
#   as you choose.  They contain "stubs" so they will not break any code as is.
# -----------------------------------------------------------------------------
import libs.rosebot_beacon_seeker as b_seeker
import libs.rosebot_line_follower as follower
import libs.rosebot_camera_tracker as tracker


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
        self.drive_system = drive.DriveSystem("B", "C")
        self.touch_sensor = touch.TouchSensor(1)
        self.arm_and_claw = arm.ArmAndClaw(self.touch_sensor)
        self.leds = leds.Leds()
        self.brick_buttons = bb.BrickButtons()
        self.remote_control = rc.RemoteControl()
        self.color_sensor = color.ColorSensor(3)
        self.infrared_proximity_sensor = proximity.InfraredProximitySensor(4)
        self.camera = camera.CameraSensor(2)
        self.sound = sound.Sound()
        self.beacon_sensor = b_sensor.BeaconSensor(4, 1)

        # ---------------------------------------------------------------------
        # The following are OPTIONAL sub-systems, which you will implement
        #   or not as you choose.  If you do not implement them,
        #   then of course these sub-systems will not work.
        # ---------------------------------------------------------------------
        self.beacon_seeker = b_seeker.BeaconSeeker(self.beacon_sensor,
                                                   self.drive_system)
        self.line_follower = follower.LineFollower(self.color_sensor,
                                                   self.drive_system)
        self.camera_tracker = tracker.CameraTracker(self.camera,
                                                    self.drive_system)
