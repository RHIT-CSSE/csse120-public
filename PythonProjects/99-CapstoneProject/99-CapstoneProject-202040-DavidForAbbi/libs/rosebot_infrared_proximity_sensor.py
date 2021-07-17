"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the InfraredProximitySensor class, for the robot's forward
facing sensor. The infrared sensor when it is in the mode in which it emits
infrared light and uses the reflected information to estimate distance to the
nearest object in its field of vision.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
###############################################################################
# STUDENTS: This module is ALREADY IMPLEMENTED.
#   READ its code so that you know how to use a InfraredProximity Sensor
#   if you wish to do so.  You may also AUGMENT this module if you choose.
###############################################################################
import libs.rosebot_ev3dev_api as ev3dev


###############################################################################
#    InfraredProximitySensor
###############################################################################
class InfraredProximitySensor(object):
    """
    Methods for the forward-facing   Infrared Proximity Sensor   on the robot,
    including:    get_distance_in_inches
    You may also (optionally) implement:  wait_until_distance_less_than
    """
    def __init__(self, port=4):
        """
        Constructs the underlying low-level InfraredProximitySensor.
          :type port: int
        """
        self.port = port
        self._low_level_proximity_sensor = \
            ev3dev.LowerLevelInfraredProximitySensor(port)
        # Note: The low-level LowerLevelInfraredProximitySensor object
        # is not actually constructed until it is enabled, which happens only
        # if one of the InfraredProximitySensor methods below are called.
        self.has_been_enabled = False

    def enable(self):
        """
        Enables the low-level LowerLevelInfraredProximitySensor object
        of the robot so that it can be used to get distances.
        """
        self._low_level_proximity_sensor.enable()
        self.has_been_enabled = True

    def get_distance_in_inches(self):
        """
        Returns the distance to the nearest object in its field of vision,
          in inches, where about 39.37 inches (which is 100 cm) means no object
          is within its field of vision.
        :return: The distance    in inches     to the nearest object.
        :rtype: float
        """
        if not self.has_been_enabled:
            self.enable()
        return self._low_level_proximity_sensor.get_distance_in_inches()

    def wait_until_distance_less_than(self, threshold_in_inches):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the IR proximity sensor to be less than some threshold.
        :param threshold_in_inches: The distance threshold in inches.
        :type threshold_in_inches: float
        """
        # ---------------------------------------------------------------------
        # OPTIONALLY, implement this method.
        # ---------------------------------------------------------------------

