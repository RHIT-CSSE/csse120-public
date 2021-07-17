"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the RoseBot class (the top-level class for a robot).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO 0: Put the name of EACH team member who contributes
#   to this module in the above.


import rosebot_touch_sensor     # Lab 1
import rosebot_drive_system     # Lab 2
import rosebot_arm_and_claw     # Lab 2
import rosebot_leds             # Lab 3
import rosebot_brick_buttons    # Lab 3
import rosebot_remote_control   # Lab 3
import rosebot_sound            # Lab 4
import rosebot_infrared_proximity_sensor     # Lab 4
import rosebot_beacon_sensor    # Lab 4
import rosebot_beacon_seeker    # Lab 4
import rosebot_color_sensor     # Lab 5
import rosebot_line_follower    # Lab 5
import rosebot_camera_sensor    # Lab 6
import rosebot_camera_tracker   # Lab 6


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
    """
    Top level of the EV3 robot stack.
    """

    def __init__(self):
        # Lab 1
        # ---------------------------------------------------------------------
        # TODO 1: With your instructor, add subsystems needed for Lab 1.
        # ---------------------------------------------------------------------
        self.drive_system = rosebot_drive_system.DriveSystem('B', 'C')

        # Lab 2
        # ---------------------------------------------------------------------
        # TODO 2: With your instructor, add subsystems needed for Lab 2.
        # ---------------------------------------------------------------------
        self.touch_sensor = rosebot_touch_sensor.TouchSensor(1)
        self.arm_and_claw = rosebot_arm_and_claw.ArmAndClaw('A', self.touch_sensor)

        # Lab 3
        # ---------------------------------------------------------------------
        # TODO 3: With your instructor, add subsystems needed for Lab 3.
        # ---------------------------------------------------------------------
        self.leds = rosebot_leds.Leds()
        self.brick_buttons = rosebot_brick_buttons.BrickButtons()
        self.remote_control = rosebot_remote_control.RemoteControl()

        # Lab 4
        # ---------------------------------------------------------------------
        # TODO 4: With your instructor, add subsystems needed for Lab 4.
        # ---------------------------------------------------------------------
        self.sound = rosebot_sound.Sound()
        self.infrared_proximity_sensor = rosebot_infrared_proximity_sensor.InfraredProximitySensor(4)
        self.beacon_sensor = rosebot_beacon_sensor.BeaconSensor(4, 1)
        self.beacon_seeker = rosebot_beacon_seeker.BeaconSeeker(self.beacon_sensor, self.drive_system)

        # Lab 5
        # ---------------------------------------------------------------------
        # TODO 5: With your instructor, add subsystems needed for Lab 5.
        # ---------------------------------------------------------------------
        self.color_sensor = rosebot_color_sensor.ColorSensor(3)
        self.line_follower = rosebot_line_follower.LineFollower(self.color_sensor, self.drive_system)

        # Lab 6
        # ---------------------------------------------------------------------
        # TODO 6: With your instructor, add subsystems needed for Lab 5.
        # ---------------------------------------------------------------------
        self.camera = rosebot_camera_sensor.CameraSensor(2)
        self.camera_tracker = rosebot_camera_tracker.CameraTracker(self.camera, self.drive_system)

        # Lab 7
        self.should_shutdown = False

    def shutdown(self):
        print("Called shutdown")
        self.should_shutdown = True
