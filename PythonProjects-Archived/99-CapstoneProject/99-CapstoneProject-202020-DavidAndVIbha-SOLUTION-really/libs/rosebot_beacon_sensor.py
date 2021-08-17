"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the BeaconSensor class which is used to get readings from
 the beacon (i.e. the remote control). The beacon sensor uses the same hardware
 as the infrared proximity sensor and the remote control receiver.  The infrared
sensor not emit light when set to the beacon mode (that only happen for the
infrared proximity sensor), instead it only looks for the light coming
from the Remote Control.  The remote control must be running in beacon mode
(the top button) for this class to work.

Authors:  Your professors (for the framework).
Winter term, 2019-2020.
"""

###############################################################################
# STUDENTS: This module is ALREADY IMPLEMENTED.
#   READ its code so that you know how to use a Beacon Sensor if you wish
#   to do so.  You may also AUGMENT this module if you choose.
###############################################################################
import libs.rosebot_ev3dev_api as ev3dev


###############################################################################
#    BeaconSensor
###############################################################################
class BeaconSensor(object):
    """
    Methods for the forward-facing Infrared Sensor on the robot,
    when used in "
    including:
    """
    def __init__(self, port, channel):
        """
        Constructs the Beacon Sensor (initially NOT enabled)
          :type port: int
          :type channel: int
        """
        self.port = port
        self.channel = channel
        # To avoid conflicts, construct the underlying sensor only if enabled.
        self._low_level_beacon_sensor = None
        self.has_been_enabled = False

    def enable(self):
        """
        Enables the Infrared Sensor of the robot to be used with beacon sensor.
        """
        self._low_level_beacon_sensor = ev3dev.LowerLevelInfraredBeaconSensor(
            self.port, self.channel)
        self._low_level_beacon_sensor.enable()
        print("Enabled the Beacon Sensor.")
        self.has_been_enabled = True

    def get_heading(self):
        """
        Returns the heading to the beacon
         - The heading is in degrees in the range -25 to 25 with:
             - 0 means straight ahead
             - negative degrees mean the Beacon is to the left
             - positive degrees mean the Beacon is to the right
        :rtype: int
        :return: Heading to the beacon
        """
        if not self.has_been_enabled:
            self.enable()
        return self._low_level_beacon_sensor.get_heading_to_beacon()

    def get_distance(self):
        """
        Returns the distance to the beacon
         - Distance is from 0 to 100, where 100 is about 70 cm
         - -128 means the Beacon is not detected.
          :rtype: int
          :return: Distance to the beacon
        """
        if not self.has_been_enabled:
            self.enable()
        return self._low_level_beacon_sensor.get_distance_to_beacon()
