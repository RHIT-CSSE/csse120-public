"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the BeaconSensor class which is used to track the beacon
(i.e. the remote control). The beacon sensor uses the same hardware as the
infrared proximity sensor and the remote control receiver.  The infrared
sensor not emit light when set to the beacon mode (that only happen for the
infrared proximity sensor), instead it only looks for the light coming
from the Remote Control.  The remote control must be running in beacon mode
(the top button) for this class to work.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import time
import rosebot_camera_sensor
import rosebot_drive_system


###############################################################################
#    CameraTracker
###############################################################################
class CameraTracker(object):
    """
    Methods using the camera to drive the robot.
    """

    def __init__(self, camera_sensor, drive_system):
        """
        Constructs CameraTracker to track beacon.
          :type camera_sensor: rosebot_beacon_sensor.BeaconSensor
          :type drive_system: rosebot_drive_system.DriveSystem
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.camera_sensor = camera_sensor
        self.drive_system = drive_system

    def spin_until_color_seen(self, speed, blob_area_threshold):
        """
        Spins the robot CW (left @ speed, right @ -speed) until the active camera color
        is seen with a size greater than or equal to the given blob_area_threshold.
        Once the blob size is bigger than threshold the drive system should stop.
        :param speed: Motor speed to use 1 to 100
        :type speed: int
        :param blob_area_threshold: Required threshold for the blob size (pixels squared)
        :type blob_area_threshold: float
        """
        self.drive_system.go(speed, -speed)
        while True:
            time.sleep(0.05)
            # ---------------------------------------------------------------------
            # TODO: Implement this method.
            # ---------------------------------------------------------------------

            # Solution to be removed
            blob = self.camera_sensor.get_biggest_blob()
            if blob.get_area() >= blob_area_threshold:
                break
        self.drive_system.stop()

    def spin_to_track_color(self, speed, duration_s):
        """
        This method should make the robot spin to follow the color.  The robot
        will not move forward it will only spin in place to continuously follow
        the active camera color left and right.  If the color is not seen the
        robot can either sit still or spin, you decide!
        After duration_s seconds have passed this method will stop both motors.
        :param speed: Motor speed to use 1 to 100
        :type speed: int
        :param duration_s: How long to continue this action (in seconds)
        :type duration_s: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method by making the robot turn left or right
        # as needed.  If the color is near the middle (you decide the threshold
        # then don't move left or right, just sit).
        # Hint towards implementing the duration_s requirement...
        # start_time_s = time.time()
        # while True:
        #     time.sleep(0.05)
        #     if time.time() > start_time_s + duration_s:
        #         break
        # ---------------------------------------------------------------------

        # Solution to be removed
        start_time_s = time.time()
        while True:
            time.sleep(0.05)
            if time.time() > start_time_s + duration_s:
                break
            blob = self.camera_sensor.get_biggest_blob()
            heading = blob.center.x - (blob.SCREEN_WIDTH / 2)
            print("Heading = {}".format(heading))
            if abs(heading) < 20:
                self.drive_system.stop()
            elif heading < 0:
                self.drive_system.go(-speed, speed)
            else:
                self.drive_system.go(speed, -speed)
        self.drive_system.stop()