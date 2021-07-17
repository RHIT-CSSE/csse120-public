"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code contains lower-level code that interacts with the EV3 robot library.
The goal is a provide a wrapper layer between your code and the ev3dev api.

The ev3dev2 api is a good one, but it is a bit different from code you've seen
before, so we added these wrapper classes to try to make your life easier.

Just so you are aware the ev3dev2 api can be found here:
https://python-ev3dev.readthedocs.io/en/stable/

but the goal of this module is to wrap all the functionality that we'd like for
you to use.  Some things we've hidden on purpose, other things we've made
easy to use. :)  Look at the doc strings of the Classes and methods below to
learn what API call you are allowed to use.

STUDENTS:  *** Do NOT change ANYTHING in this module. ***

Winter term, 2019-2020.
"""

import ev3dev.ev3 as ev3

###############################################################################
# STUDENTS:  *** Do NOT change ANYTHING in this module. ***
###############################################################################


###############################################################################
#    Motor
###############################################################################
class Motor(object):
    """
    Controls a single EV3 Motor.  Our robot has 2 "large" motors for the wheels
    and a "medium" motor to control the arm/claw.
    """

    def __init__(self, port, motor_type='large'):
        """
        Constructs a Motor based on the input parameters.  Valid ports:
          'A', 'B', 'C', or 'D'
          Our "large" motors are in ports "B" and "C"
          Our "medium" motor is in port "A"
        Valid motor_types: "medium" or "large"
        ---
        :param port: Letter on EV3 brick where motor connects
        :type port: str
        :param motor_type: Motor types are either "medium" or "large"
        :type motor_type: str
        """
        if motor_type == 'large':
            self._motor = ev3.LargeMotor('out' + port)
        else:
            self._motor = ev3.MediumMotor('out' + port)

        # Check that the motor is actually connected (crash now if not connected)
        assert self._motor.connected

    def turn_on(self, speed):
        """
        Turns on the motor at the requested speed. Valid speeds:
          -100 up to 100
        For example:
          -100 full speed in reverse
          -50 slow reverse
          0 coast to a stop
          30 slow forwards
          60 pretty fast forwards
          100 max speed forwards
        ---
        :param speed: Duty cycle percentage for motor
        :type speed: int
        """
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self, stop_action="brake"):
        """
        Stops the motor.
        Note: turn_off is similar to turn_on(0), but turn_off
              tries to stop the motion a bit faster using the  brake  option.
        """
        self._motor.stop(stop_action=stop_action)

    def get_position(self):
        """
        Returns the position of the motor since the last reset.
        Units are in degrees
        :return: Position of the motor in degrees
        :rtype: int
        """
        return self._motor.position

    def reset_position(self):
        """
        Sets the motors current position as 0.
        """
        self._motor.position = 0


###############################################################################
#    TouchSensor
###############################################################################
class TouchSensor(object):
    def __init__(self, port=None):  # port must be 1, 2, 3, 4, or None (for autodetect)
        """
        Creates a TouchSensor.
        :type port: int | None
        """
        if port is not None:
            self._touch_sensor = ev3.TouchSensor('in' + str(port))
        else:
            self._touch_sensor = ev3.TouchSensor()  # automatically determine the port

        # Check that all the sensor is actually connected (crash now if not connected)
        assert self._touch_sensor

    def is_pressed(self):

        """
        Returns True if this TouchSensor is pressed, else returns False
        :return: Returns True if the touch sensor is being pressed.
        :rtype bool
        """
        return self._touch_sensor.is_pressed == 1


###############################################################################
#    LEDs
###############################################################################
class Led(object):
    """
    Represents a single LED object on the EV3 Brick.
    Note: there are 2 LEDs and each LED has a red and a green component.
    """

    def __init__(self, left_or_right):
        """
          Constructs a single LED object. Valid left_or_right values:
            "left" or "right"
          :param left_or_right: Determines the LED side ("left" or "right")
          :type left_or_right: str
        """
        if left_or_right == "left":
            self.led_location = ev3.Leds.LEFT
        elif left_or_right == "right":
            self.led_location = ev3.Leds.RIGHT
        else:
            print("INVALID Led LOCATION!")

    def turn_off(self):
        """ Turns this Led off. """
        self.set_color("off")

    def set_color(self, color_name):
        """
        Sets this Led to the given color. Valid colors include:
          "red", "green", "amber", "off"
          :param color_name: Target color for the LED.
          :type color_name: str
        """
        if color_name == "red":
            ev3.Leds.set_color(self.led_location, ev3.Leds.RED)
        elif color_name == "green":
            ev3.Leds.set_color(self.led_location, ev3.Leds.GREEN)
        elif color_name == "amber":
            ev3.Leds.set_color(self.led_location, ev3.Leds.AMBER)
        elif color_name == "off":
            ev3.Leds.set_color(self.led_location, ev3.Leds.BLACK)
        else:
            print("INVALID LED COLOR STRING")


###############################################################################
#    Remote Control
###############################################################################
class RemoteControlChannel(object):
    """
     Represents all of the buttons on the remote control.  This is used
     to know if a button is being pressed on the remote control.
     """

    def __init__(self, channel):
        """
        Creates an object that can be used to check if a button is being
        pressed on the remote control.  You might need as many as four of
        these classes if you use all the channels of the remote.
        Valid channels: 1, 2, 3, or 4
        :param channel: Determines which channel of the remote control to use.
        :type channel: int
        """
        self._remote_control = ev3.RemoteControl(channel=channel)

        # Note: The IR sensor can be used in 3 different modes!
        #   Proximity mode, Beacon seek mode, and remote control mode.
        # The lower library tries to change it as needed automatically, so
        #   here we just don't mess with it with the mode at all.

    def red_up(self):
        """
        Returns True if the remote control red up button is pressed
        :return: True if red_up is pressed for this channel, otherwise False.
        :rtype bool
        """
        return self._remote_control.red_up

    def red_down(self):
        """
        Returns True if the remote control red down button is pressed
        :return: True if red_down is pressed for this channel, otherwise False.
        :rtype bool
        """
        return self._remote_control.red_down

    def blue_up(self):
        """
        Returns True if the remote control blue up button is pressed
        :return: True if blue_up is pressed for this channel, otherwise False.
        :rtype bool
        """
        return self._remote_control.blue_up

    def blue_down(self):
        """
        Returns True if the remote control blue down button is pressed
        :return: True if blue_down is pressed for this channel, otherwise False.
        :rtype bool
        """
        return self._remote_control.blue_down


###############################################################################
#    EV3 Brick Buttons
###############################################################################
class BrickButtons(object):
    def __init__(self):
        """
        Creates the one and only brick button object.
        """
        self._buttons = ev3.Button()

    def up(self):
        """
        Returns True if the EV3 brick up button is pressed
        :return: True if up button is pressed on the EV3 brick, otherwise False.
        :rtype bool
        """
        return self._buttons.up

    def down(self):
        """
        Returns True if the EV3 brick down button is pressed
        :return: True if down button is pressed on the EV3 brick, otherwise False.
        :rtype bool
        """
        return self._buttons.down

    def left(self):
        """
        Returns True if the EV3 brick left button is pressed
        :return: True if left button is pressed on the EV3 brick, otherwise False.
        :rtype bool
        """
        return self._buttons.left

    def right(self):
        """
        Returns True if the EV3 brick right button is pressed
        :return: True if right button is pressed on the EV3 brick, otherwise False.
        :rtype bool
        """
        return self._buttons.right

    def backspace(self):
        """
        Returns True if the EV3 brick backspace button is pressed
        :return: True if backspace button is pressed on the EV3 brick, otherwise False.
        :rtype bool
        """
        return self._buttons.backspace


###############################################################################
#    Infrared (IR) Proximity (Distance) Sensor
###############################################################################
class InfraredProximitySensor(object):
    """
    The infrared sensor on the front of the robot emits infrared light
    and uses the reflected information to estimate distance to the nearest
    object in its field of vision.
    """

    def __init__(self, port=None):  # port must be 1, 2, 3, 4, or None (for autodetect)
        """
        Creates a InfraredSensor.
        :type port: int | None
        """
        if port is not None:
            self._ir_sensor = ev3.InfraredSensor('in' + str(port))
        else:
            self._ir_sensor = ev3.InfraredSensor()  # automatically determine the port

        # Note: The IR sensor can be used in 3 different modes!
        # self._ir_sensor.mode = "IR-PROX"
        # self._ir_sensor.mode = "IR-SEEK"
        # self._ir_sensor.mode = "IR-REMOTE"

        # The ev3dev library will switch the mode for you, so no code added here.

        # Check that the ir_sensor is actually connected (crash now if not connected)
        assert self._ir_sensor

    def get_distance_raw(self):
        """
        Returns the distance to the nearest object in its field of vision,
        as a integer between 0 and 100, where a value N indicates that the
        distance to the nearest object is 70 * (N / 100) cm.  For example:
           - numbers < 10 indicate that the object is less than 7 cm away
           - 20 means 1/5 of 70, i.e., 14 cm
           - 40 means 2/5 of 70, i.e., 28 cm
           - 50 means 1/2 of 70, i.e., 35 cm
           - greater than 70 is too far away to be useful
               (more precisely, greater than 49 cm away)
           - 100 is the maximum distance for the sensor, namely, 100 cm.
        :return: Distance to the nearest object 0 (close) to 100 (far away)
        :rtype: int
        """
        self._ir_sensor.mode = "IR-PROX"
        return self._ir_sensor.proximity

    def get_distance_in_inches(self):
        """
        Returns the distance to the nearest object in its field of vision,
        in inches, where about 39.37 inches (which is 100 cm) means no object
        is within its field of vision.
        :return: Distance to the nearest object in inches (in)
        :rtype: float
        """
        cm_per_inch = 2.54
        distance = 70 / cm_per_inch * self.get_distance_raw() / 100
        return distance


###############################################################################
#    ColorSensor
###############################################################################
class ColorSensor(object):
    """ Represents the downward facing light sensor of the robot. """

    def __init__(self, port=None):  # port must be 1, 2, 3, 4, or None (for autodetect)
        """
        Creates a ColorSensor.
        :type port: int | None
        """
        self.COLORS = (
            'No Color',
            'Black',
            'Blue',
            'Green',
            'Yellow',
            'Red',
            'White',
            'Brown',
        )

        if port is not None:
            self._sensor = ev3.ColorSensor('in' + str(port))
        else:
            self._sensor = ev3.ColorSensor()  # automatically determine the port

        # Check that the ir_sensor is actually connected (crash now if not connected)
        assert self._sensor

    def get_color_as_number(self):
        return self._sensor.color

    def get_color_as_name(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is a string:
          - 0: No Color
                  (that is, cannot classify the color as one of the following)
          - 1: Black
          - 2: Blue
          - 3: Green
          - 4: Yellow
          - 5: Red
          - 6: White
          - 7: Brown
        :return: String representing the current color
        :rtype: str
        """
        return self.COLORS[self.get_color_as_number()]

    def get_reflected_light_intensity(self):
        """
        Shines red light and returns the intensity of the reflected light.
        The returned value is from 0 to 100,
        but in practice more like 3 to 90+ in our classroom lighting with our
        downward-facing sensor that is about 0.25 inches from the ground.
        :return: Amount of light reflected 0 (no light reflected) to 100 (super bright)
        :rtype: int
        """
        return self._sensor.reflected_light_intensity

    def get_ambient_light_intensity(self):
        """
        Shines dimly lit blue light and returns the intensity
        of the ambient light.  The returned value is from 0 to 100.
        :return: Amount of light present 0 (in a cave) to 100 (on the sun)
        :rtype: int
        """
        return self._sensor.ambient_light_intensity


###############################################################################
#    IR Beacon Sensor
###############################################################################
class InfraredBeaconSensor(object):
    """
    The infrared sensor which it measures the heading and distance to the Beacon.
    Note: the remote control can be put into Beacon mode (signal continuously)
    on one of its 4 channels (1 to 4).
    """

    def __init__(self, port=None, channel=1):  # port must be 1, 2, 3, 4, or None (for autodetect)
        """
        Creates an InfraredBeaconSensor and puts it into a disabled state.
        Note: it starts disabled to avoid conflicts with other uses of this sensor.
        :type port: int | None
        :type channel: int
        """
        self.port = port
        self.channel = channel
        self._ir_sensor = None  # Not initialized at first to avoid conflicts with the IR sensor.
        self.has_been_enabled = False

    def enable(self):
        """
            Enables the InfraredBeaconSensor.  By default the sensor is disabled, since the
            same sensor serves multiple roles.  To avoid conflicts the InfraredBeaconSensor
            is disabled by default.  This method enables the sensor as an IR Beacon Sensor.
        """
        if self.port is not None:
            self._ir_sensor = ev3.InfraredSensor('in' + str(self.port))
        else:
            self._ir_sensor = ev3.InfraredSensor()  # automatically determine the port

        # Note: The IR sensor can be used in 3 different modes!
        # self._ir_sensor.mode = "IR-PROX"
        # self._ir_sensor.mode = "IR-SEEK"
        # self._ir_sensor.mode = "IR-REMOTE"

        # Check that the ir_sensor is actually connected (crash now if not connected)
        assert self._ir_sensor.connected

        # The ev3dev library will try to switch it for you, but here it's done explicitly.
        self._ir_sensor.mode = "IR-SEEK"
        print("InfraredSensor mode set to IR-SEEK")
        self.has_been_enabled = True

    def get_heading_to_beacon(self):
        """
        Returns heading (-25, 25) to the beacon on the given channel.
        - The heading is in degrees in the range -25 to 25 with:
             - 0 means straight ahead
             - negative degrees mean the Beacon is to the left
             - positive degrees mean the Beacon is to the right
        """
        if not self.has_been_enabled:
            self.enable()
        return self._ir_sensor.value((self.channel - 1) * 2)

    def get_distance_to_beacon(self):
        """
        Returns distance (0, 100) to the beacon on the given channel.
        - Distance is from 0 to 100, where 100 is about 70 cm
         - -128 means the Beacon is not detected.
        """
        if not self.has_been_enabled:
            self.enable()
        return self._ir_sensor.value((self.channel - 1) * 2 + 1)


###############################################################################
# Camera
###############################################################################
class Camera(object):
    """
    A class for a Pixy camera.
    Use the   PixyMon    program to initialize the camera's firmware.
    Download the program from the    Windows   link at:
        http://www.cmucam.org/projects/cmucam5/wiki/Latest_release
    Learn how to use the Pixy camera's "color signatures" to recognize objects
        at: http://www.cmucam.org/projects/cmucam5/wiki/Teach_Pixy_an_object.
    """

    def __init__(self, port=2):
        input_port = "in" + str(port)
        try:
            self._pixy_camera_sensor = ev3.Sensor(input_port, driver_name="pixy-lego")
        except AssertionError:
            print("Is the camera plugged into port 2?")
            print("If that is not the problem, then check whether the camera")
            print("has gotten into 'Arduino mode', as follows:")
            print("  In PixyMon, select the gear (Configure) icon,")
            print("  then look for a tab that has 'Arduino' on its page.")
            print("  Make sure it says 'Lego' and not 'Arduino'.")
            print("Note: Only some of the cameras have this option;")
            print("the others are automatically OK in this regard.")
        self.set_color_signature()  # Default to color signature 1.

    def set_color_signature(self, signature_number=1):
        """
        Sets the color signature that will be returned by calls to get_biggest_blob
        :param signature_number: Index of the color signature to find (1 to 8)
        :type signature_number: int
        """
        if signature_number == 1:
            self._pixy_camera_sensor.mode = "SIG1"
        elif signature_number == 2:
            self._pixy_camera_sensor.mode = "SIG2"
        elif signature_number == 3:
            self._pixy_camera_sensor.mode = "SIG3"
        elif signature_number == 4:
            self._pixy_camera_sensor.mode = "SIG4"
        elif signature_number == 5:
            self._pixy_camera_sensor.mode = "SIG5"
        elif signature_number == 6:
            self._pixy_camera_sensor.mode = "SIG6"
        elif signature_number == 7:
            self._pixy_camera_sensor.mode = "SIG7"
        else:
            print("Invalid signature value")

    def get_biggest_blob(self):
        """
        A "blob" is a collection of connected pixels that are all in the color
        range specified by a color "signature".  A Blob object stores the Point
        that is the center (actually, centroid) of the blob along with the
        width and height of the blob.  For a Pixy camera, the x-coordinate is
        between 0 and 319 (0 left, 319 right) and the y-coordinate is between
        0 and 199 (0 TOP, 199 BOTTOM).  See the Blob class below.
        A Camera returns the largest Blob whose pixels fall within the Camera's
        current color signature.  A Blob whose width and height are zero
        indicates that no large enough object within the current color signature
        was visible.
        The Camera's color signature defaults to "SIG1", which is the color
        signature set by selecting the RED light when training the Pixy camera.
        :return: A Blob object for the biggest matching color blob.
        :rtype: Blob
        """
        return Blob(Point(self._pixy_camera_sensor.value(1),
                          self._pixy_camera_sensor.value(2)),
                    self._pixy_camera_sensor.value(3),
                    self._pixy_camera_sensor.value(4))


###############################################################################
# Point (for the Camera class, as well as for general purposes.
###############################################################################
class Point(object):
    """
    Represents a point in the camera space.
    For a Pixy camera,
      the x-coordinate is between 0 and 319 (0 left, 319 right)
      the y-coordinate is between 0 and 199 (0 TOP, 199 BOTTOM).
    """
    def __init__(self, x, y):
        """
        Constructs the Point (centroid of the Blob).
        :type x: int
        :type y: int
        """
        self.x = x
        self.y = y

###############################################################################
# Blob (for the Camera class).
###############################################################################
class Blob(object):
    """
    Represents a rectangle in the form that a Pixy camera uses:
      upper-left corner along with width and height.
    """

    def __init__(self, center, width, height):
        """
        Constructs the Blob (which is always a rectangle)
        :param center: Centroid of the blob
        :type center: Point
        :param width: Width of this blob in pixels (1 to 320)
        :param width: int
        :param height: Height of this blob in pixels (1 to 200)
        :param height: int
        """
        self.center = center
        self.width = width
        self.height = height
        self.SCREEN_WIDTH = 320
        self.SCREEN_HEIGHT = 240

    def __repr__(self):
        return "center: ({:3d}, {:3d})  width, height: {:3d} {:3d}.".format(
            self.center.x, self.center.y, self.width, self.height)

    def get_area(self):
        return self.width * self.height

    def is_left_of_center(self):
        return self.center.x < self.SCREEN_WIDTH / 2

    def is_right_of_center(self):
        return self.center.x > self.SCREEN_WIDTH / 2

    def is_against_left_edge(self):
        return self.center.x - (self.width + 1) / 2 <= 0

    def is_against_right_edge(self):
        return self.center.x + (self.width / 2 + 1) / 2 >= self.SCREEN_WIDTH

    def is_against_top_edge(self):
        return self.center.y - (self.height + 1) / 2 <= 0

    def is_against_bottom_edge(self):
        return self.center.y + (self.height + 1) / 2 >= self.SCREEN_HEIGHT

    def is_against_an_edge(self):
        return (self.is_against_left_edge()
                or self.is_against_right_edge()
                or self.is_against_top_edge()
                or self.is_against_bottom_edge())


###############################################################################
#    Beeper
###############################################################################
class Beeper(object):
    # Future enhancements: Add volume to all the SoundSystem classes.
    def __init__(self):
        self._beeper = ev3.Sound

    def beep(self):
        """
        Starts playing a BEEP sound.
        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. Returns a subprocess.Popen,
        so if you want the sound-playing to block until the sound is completed
        (e.g. if the next statement will immediately make another sound),
        then use   beep  like this:
             beeper = Beeper()
             beeper.beep().wait()
        :rtype subprocess.Popen
        """
        return self._beeper.beep()


###############################################################################
#    SpeechMaker
###############################################################################
class SpeechMaker(object):
    """
    Creates an object that has a speak method to have the robot talk.
    Note: this class could really be a static class, but we wanted to follow
    the same pattern as other classes to keep it simple.
    """
    def __init__(self):
        self._speech_maker = ev3.Sound

    def speak(self, phrase):
        """
        Speaks the given phrase aloud.
        The phrase must be short.
        This method is blocking, meaning the next line of your code will not
        run until the SpeechMaker is done (usually this IS what you want).
        :param phrase: The string that you would like the robot to say.
        :type  phrase:  str
        """
        self._speech_maker.speak(phrase).wait()

    def speak_nonblocking(self, phrase):
        """
        Speaks the given phrase aloud. The phrase must be short.
        This method does NOT block, that is, continues immediately to the next
        statement while the sound is being played.
        IMPORTANT:  speak()  does not appear to work correctly in all circumstances.
        Use this method with a   time.sleep()  after a   speak_nonblocking  as needed.
        :param phrase: The string that you would like the robot to say.
        :type  phrase:  str
        """
        self._speech_maker.speak(phrase)


###############################################################################
#    ToneMaker
###############################################################################
class ToneMaker(object):
    """
    Creates an object that has a play_tone and play_tone_sequence methods to
    have the robot play music using notes.
    Note: this class could really be a static class, but we wanted to follow
    the same pattern as other classes to keep it simple.
    """
    def __init__(self):
        self._tone_maker = ev3.Sound

    def play_tone(self, frequency, duration):
        """
        Starts playing a tone at the given frequency (in Hz) for the given
        duration (in milliseconds).
        This method is blocking, meaning the next line of your code will not
        run until the ToneMaker is done playing (usually this IS what you want).
        :param frequency: Frequency (Hertz) to play
        :type frequency: float
        :param duration: Length of time to play the tone in milliseconds (ms)
        :type duration: float
        """
        self._tone_maker.tone(frequency, duration).wait()

    def play_tone_sequence(self, tones):
        """
        Starts playing a sequence of tones, where each tone is a 3-tuple:
          (frequency, duration ms, delay_until_next_tone_in_sequence ms)
        This method is blocking, meaning the next line of your code will not
        run until the ToneMaker is done playing (usually this IS what you want).
        Here is a cheerful example, from the ev3 documentation::
            tone_player = ToneMaker()
            tone_player.play_tone_sequence([
        (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
        (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
        (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
        (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100),
        (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
        (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
        (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
        (554.36, 350, 100),
        (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100),
        (440, 25, 100),
        (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
        (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100),
        (392, 250, 100),
        (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100),
        (392, 250, 100),
        (392, 25, 100), (784, 350, 100), (739.98, 250, 100),
        (698.46, 25, 100),
        (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
        (415.3, 25, 200),
        (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
        (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400),
        (311.13, 25, 200),
        (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
        (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
        ])
        :param tones: List of 3-tuple tones (frequency, duration_ms, delay_ms)
        :type tones: list of tuple
        """
        self._tone_maker.tone(tones).wait()

    def play_tone_nonblocking(self, frequency, duration):
        """
        Same as the play_tone method, but...
        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played.
        :param frequency: Frequency (Hertz) to play
        :type frequency: float
        :param duration: Length of time to play the tone in milliseconds (ms)
        :type duration: float
        """
        self._tone_maker.tone(frequency, duration)

    def play_tone_sequence_nonblocking(self, tones):
        """
        Same as the play_tone_sequence method, but...
        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played.
        :param tones: List of 3-tuple tones (frequency, duration_ms, delay_ms)
        :type tones: list of tuple
        """
        self._tone_maker.tone(tones)


###############################################################################
#    WavFilePlayer
###############################################################################
class WavFilePlayer(object):
    """
    Creates an object that has a play methods to play a .wav file.
    Note: this class could really be a static class, but we wanted to follow
    the same pattern as other classes to keep it simple.
    """
    def __init__(self):
        self._wav_player = ev3.Sound

    def play(self, file_location):
        """
        Plays properly formatted .wav files.
        Based on the documentation the file must be a PCM signed 16-bit
        little-endian .wav file.  You can try to convert normal audio files
        using tools like: http://audio.online-convert.com/convert-to-wav
        Warning: audio files get big.  The game is trial and error to find
        one that works.  Your instructors are CERTAINLY not experts on what
        actaully plays.
        """
        self._wav_player.play(file_location).wait()


# Some notes and examples for when we move to ev3dev2...
# From: https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/index.html
# import ev3dev2
# ts = ev3dev2.sensor.lego.TouchSensor()
# leds = ev3dev2.led.Leds()
# while True:
#     if ts.is_pressed:
#         leds.set_color("LEFT", "GREEN")
#         leds.set_color("RIGHT", "GREEN")
#     else:
#         leds.set_color("LEFT", "RED")
#         leds.set_color("RIGHT", "RED")
# m = ev3dev2.motor.LargeMotor(ev3dev2.motor.OUTPUT_A)
# m.on_for_rotations(ev3dev2.motor.SpeedPercent(75), 5)
# ev3dev2.sensor.INPUT_1
# ev3dev2.sensor.lego.TouchSensor
# pixy = ev3dev2.sensor.Sensor(ev3dev2.sensor.INPUT_2, driver_name="pixy-lego")
