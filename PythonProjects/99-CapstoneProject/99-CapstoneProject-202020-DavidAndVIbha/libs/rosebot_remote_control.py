"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the RemoteControl class, for the robot's remote
control that detects when the arm and claw are in the fully-up position.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
###############################################################################
# STUDENTS: This module is (mostly) ALREADY IMPLEMENTED.
#   READ its code so that you know how to use a RemoteControl if you wish
#   to do so.  You may also AUGMENT this module if you choose
#   (e.g. by implementing   wait_until_pressed   as specified below).
###############################################################################
import libs.rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    RemoteControl
###############################################################################
class RemoteControl(object):
    """
    Methods for the RemoteControl on the robot, including:
       is_pressed    (optionally) wait_until_pressed
    """
    def __init__(self):
        """
        Constructs the underlying low-level versions of this RemoteControl.
        Creates a single instance variables named:
           remote_controls
        which is a list, in order, of the four possible remote control objects.
        """
        remote_control_1 = rose_ev3.RemoteControlChannel(1)
        remote_control_2 = rose_ev3.RemoteControlChannel(2)
        remote_control_3 = rose_ev3.RemoteControlChannel(3)
        remote_control_4 = rose_ev3.RemoteControlChannel(4)
        self.remote_controls = [remote_control_1, remote_control_2,
                                remote_control_3, remote_control_4]

    def is_pressed(self, channel, button_name):
        """
        Returns True if the requested button is pressed.
        Valid button_names:
          "red_up", "red_down", "blue_up", "blue_down"
          :rtype: bool
        """
        remote_control = self.remote_controls[channel - 1]
        if button_name == "red_up":
            return remote_control.red_up()
        elif button_name == "red_down":
            return remote_control.red_down()
        elif button_name == "blue_up":
            return remote_control.blue_up()
        elif button_name == "blue_down":
            return remote_control.blue_down()
        else:
            print("INVALID REMOTE CONTROL BUTTON NAME")
            return False

    def wait_until_pressed(self, channel, button):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the requested button to be pressed
        """
        # ---------------------------------------------------------------------
        # OPTIONALLY, implement this method.
        # ---------------------------------------------------------------------
