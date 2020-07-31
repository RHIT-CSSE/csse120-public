"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the CameraTracker class which is used to track
the object detected by the camera (if any).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import libs.rosebot_camera_sensor as camera
import libs.rosebot_drive_system as drive


###############################################################################
# STUDENTS: OPTIONALLY, extend the code in this module to contain methods like:
#
#   def spin_until_object_seen(self, speed, heading_threshold):
#       """ Spin until robot is within  heading_threshold   of the object. """
#
#   def spin_to_track_object(self, speed, duration_s):
#       """ Spin, keeping robot pointed at the object, for given duration. """
#
#   def drive_to_object(self):
#       """ Spin until see object, then forward until robot is close to it. """
#
###############################################################################


###############################################################################
#    CameraTracker
###############################################################################
class CameraTracker(object):
    """ Methods using the camera to drive the robot. """

    def __init__(self, camera_sensor, drive_system):
        """
        Constructs CameraTracker to track beacon.
          :type camera_sensor: camera.CameraSensor
          :type drive_system:  drive.DriveSystem
        """
        self.camera_sensor = camera_sensor
        self.drive_system = drive_system
