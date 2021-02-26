class RoseBot(object):
    """
    Provides direct but high-level access to all of a RoseBot's features.
    Has a:
      Runner [wrong word?] that can connect, sleep and ...
      LeftWheel that can make the left wheel spin.
      RightWheel that can make the right wheel spin.
      Various Sensors (including Camera and maybe Button) that can return readings.
      CameraPanServo that can go to position ...
      CameraTiltServo
      Buzzer
      BuiltinLED (wrong name?)
      ???

      Also an ArduinoRoseBot that allows access to lower-level systems and methods.
      Also a ExtendedRosebot that allows access to higher-level systems and methods.
    """
    def __init__(self, extended=None):
        """
          :type extended: RoseBotExtended
        """
#         self.extended = extended or ExtendedRoseBot(self)

    def foobar(self):
        pass





class Runner(object):
    """
    wrong name?
    connect
    sleep
    ???
    has a Communicator
    """



def main():
    pass

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
