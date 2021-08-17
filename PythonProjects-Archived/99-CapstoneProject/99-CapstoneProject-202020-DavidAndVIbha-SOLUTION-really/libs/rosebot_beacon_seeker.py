"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the BeaconSeeker class which is used to track the beacon
(i.e. the remote control).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import time
import libs.rosebot_beacon_sensor as beacon
import libs.rosebot_drive_system as drive

###############################################################################
# STUDENTS: OPTIONALLY, extend the code in this module to contain methods like:
#
#   def spin_until_beacon_seen(self, speed, heading_threshold):
#       """ Spin until robot is within  heading_threshold   of the Beacon. """
#
#   def spin_to_track_beacon(self, speed, duration_s):
#       """ Spin, keeping robot pointed at Beacon, for the given duration. """
#
#   def drive_to_beacon(self):
#       """ Spin until see Beacon, then forward until robot is close to it. """
#
###############################################################################


###############################################################################
#    BeaconSeeker
###############################################################################
class BeaconSeeker(object):
    """
    Methods using the beacon sensor to drive the robot.
    """
    def __init__(self, beacon_sensor, drive_system):
        """
        Constructs BeaconSeeker to track beacon.
          :type beacon_sensor: beacon.BeaconSensor
          :type drive_system:  drive.DriveSystem
        """
        self.beacon_sensor = beacon_sensor
        self.drive_system = drive_system
