"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the CameraSensor.

Authors:  Your professors (for the framework).
Winter term, 2019-2020.
"""
###############################################################################
# STUDENTS: This module is ALREADY IMPLEMENTED.
#   READ its code so that you know how to use a CameraSensor if you wish
#   to do so.  You may also AUGMENT this module if you choose.
###############################################################################
import libs.rosebot_ev3dev_api as ev3dev


###############################################################################
#    CameraSensor
###############################################################################
class CameraSensor(object):
    """ A class for using the Pixy Camera on a Snatch3r robot. """
    def __init__(self, port=2):
        """
        Constructs the underlying low-level Camera.
          :type port: int
        """
        self.port = port
        self._low_level_camera = ev3dev.LowerLevelCamera(self.port)

        # Note: The low-level Camera object is not actually constructed
        # until it is enabled, which happens only if one of the CameraSystem
        # methods is actually called.
        self.has_been_enabled = False

    def enable(self):
        """
        Enables the Camera of the robot so that it can be used to get a blob.
        """
        self._low_level_camera.enable()
        self.has_been_enabled = True

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
        return self._low_level_camera.get_biggest_blob()

    def set_color_signature(self, signature_number=1):
        """
        Sets the color signature that will be used for calls
        to the   get_biggest_blob   method.
          :param signature_number: Index of the color signature to find (1 to 8)
          :type signature_number: int
        """
        if not self.has_been_enabled:
            self.enable()
        self._low_level_camera.set_signature(signature_number)

    def get_color_signature(self):
        """
        Returns the color signature that is currently used for calls
        to the   get_biggest_blob   method, as an integer (1 to 8).
        """
        if not self.has_been_enabled:
            self.enable()
        return self._low_level_camera.get_signature()
