"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the CameraSensor.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_ev3dev_api as rose_ev3


###############################################################################
#    CameraSensor
###############################################################################
class CameraSensor(object):
    """
    """

    def __init__(self, port=2):
        """
        Constructs the underlying low-level InfraredBeaconSensor.
          :type port: int
          :type channel: int
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement (uncomment)  this method.
        # ---------------------------------------------------------------------
        # self.port = port
        # self.camera = None  # Only enable the camera if it is actually used.
        # self.has_been_enabled = False

    def enable(self):
        """
        Enables the Camera of the robot so that it can be used to get a blob.
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement (uncomment)  this method.
        # ---------------------------------------------------------------------
        # self.camera = rose_ev3.Camera(self.port)
        # self.has_been_enabled = True

    def get_biggest_blob(self):
        """
        Returns the biggest Blob object in the field of view of the camera.
        A "blob" is a collection of connected pixels that are all in the color
        range specified by a color "signature".  A Blob object stores the Point
        that is the center (actually, centroid) of the blob along with the
        width and height of the blob.  For a Pixy camera, the x-coordinate is
        between 0 and 319 (0 left, 319 right) and the y-coordinate is between
        0 and 199 (0 TOP, 199 BOTTOM).  See the rose_ev3.Blob class for details.
        A Camera returns the largest Blob whose pixels fall within the Camera's
        current color signature.  A Blob whose width and height are zero
        indicates that no large enough object within the current color signature
        was visible.
        The Camera's color signature defaults to "SIG1", which is the color
        signature set by selecting the RED light when training the Pixy camera.
        :return: A Blob object for the biggest matching color blob.
        :rtype: rose_ev3.Blob
        """
        if not self.has_been_enabled:
            self.enable()
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------



    def set_color_signature(self, signature_number):
        """
        Sets the color signature that will be returned by calls to get_biggest_blob
        :param signature_number: Index of the color signature to find (1 to 8)
        :type signature_number: int
        """
        if not self.has_been_enabled:
            self.enable()
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

