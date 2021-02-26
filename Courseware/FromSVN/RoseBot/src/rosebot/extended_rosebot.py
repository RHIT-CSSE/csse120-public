"""
<describe what this module has/does>

Created on Sep 29, 2016.
Written by: david.
"""

class ExtendedRoseBot(object):
    """
    Adds systems and methods that are not so direct as those of
    a RoseBot, including:
      MotorSystem: forward, backward, left, right, curve (?), ...
        Also can return distances the wheels have spun.
        Also can do PID forward, backward, left, right.
      CameraSystem:  can pan, tilt and return information.
        Also can pan/tilt to track something.
      DistanceSensorSystem:  distances on left, center, right
      ReflectanceSensorSystem: reflectance left, center, right
      Follower:  uses subsystems to follow an object.
      Singer:
      Talker:  morse code with LED or buzzer


    Also a Rosebot to allow access to RoseBot things,
    and an ArduinoRoseBot to allow access to Arduino things.

    Also a Communicator that can connect and sleep?? and ??
    """
    def __init__(self, rosebot=None):
        """
          :type rosebot: RoseBot
          """
#         self.rosebot = rosebot or RoseBot(self)

    def foo(self):
        pass

def main():
    """ Calls the   TEST   functions in this module. """
    pass


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
