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
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    InfraredProximitySensor
###############################################################################
class InfraredProximitySensor(object):
    """
    Methods for the forward-facing InfraredProximitySensor on the robot, including:
      get_distance     wait_until_distance_less_than
    """

    def __init__(self, port):
        """
        Constructs the underlying low-level InfraredProximitySensor.
          :type port: int
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.sensor = rose_ev3.InfraredProximitySensor(port)

    def get_distance_in_inches(self):
        """
        Returns the distance to the nearest object in its field of vision,
          in inches, where about 39.37 inches (which is 100 cm) means no object
          is within its field of vision.
        :return: The distance    in inches     to the nearest object.
        :rtype: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        return self.sensor.get_distance_in_inches()

    def wait_until_distance_less_than(self, threshold_in_inches):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the IR proximity sensor to be less than some threshold.
        :param threshold_in_inches: The distance threshold in inches.
        :type threshold_in_inches: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        while True:
            time.sleep(0.05)
            if self.get_distance_in_inches() < threshold_in_inches:
                break
