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

    def turn_off(self):
        """
        Stops the motor.
        Note: turn_off is similar to turn_on(0), but turn_off
              tries to stop the motion a bit faster using the
              brake option.
        """
        self._motor.stop(stop_action="brake")

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

        :return:
        """
        self._motor.position = 0


###############################################################################
#    TouchSensor
###############################################################################
class TouchSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3, 4, or None (for autodetect)
        """
        Creates a TouchSensor.
        :type port: int
        """
        if port is not None:
            self._touch_sensor = ev3.TouchSensor('in' + str(port))
        else:
            self._touch_sensor = ev3.TouchSensor()  # automatically determine the port

    def is_pressed(self):
        """
        Returns True if this TouchSensor is pressed, else returns False
        ":rtype bool"""
        return self._touch_sensor.is_pressed == 1


###############################################################################
#    ColorSensor
###############################################################################
class ColorSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._color_sensor = ev3.ColorSensor('in' + str(port))
        self.color_names = (
            'NoColor',
            'Black',
            'Blue',
            'Green',
            'Yellow',
            'Red',
            'White',
            'Brown',
        )

    def get_color(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is an integer between
        0 and 7, where the meanings of the integers are:
          - 0: No color
                  (that is, cannot classify the color as one of the following)
          - 1: Black
          - 2: Blue
          - 3: Green
          - 4: Yellow
          - 5: Red
          - 6: White
          - 7: Brown
        """
        return self._color_sensor.color

    def get_reflected_light_intensity(self):
        """
        Shines red light and returns the intensity of the reflected light.
        The returned value is from 0 to 100,
        but in practice more like 3 to 90+ in our classroom lighting with our
        downward-facing sensor that is about 0.25 inches from the ground.
        """
        return self._color_sensor.reflected_light_intensity

    def get_ambient_light_intensity(self):
        """
        Shines dimly lit blue light and returns the intensity
        of the ambient light.  The returned value is from 0 to 100.
        """
        return self._color_sensor.ambient_light_intensity

    def get_color_as_name(self):
        """
        Same as  get_color  but returns the color as a STRING, in particular,
        as one of the strings listed in the doc-string for get_color.
        """
        return self.color_names[self.get_color()]

    def get_color_number_from_color_name(self, color_name):
        """
        Returns the color NUMBER associated with the given color NAME.
        The color_name must be one of the 7 strings
        listed in the doc-string for get_color.
        """
        return self.COLOR_NUMBERS[color_name]

    def get_raw_color(self):
        """
        Shines red, then green, then blue light down.  Returns the reflected
        intensities of each, with each in the range 0-1020.
        Example usage:
            red, green, blue = color_sensor.get_raw_color
        """
        # Not yet implemented


###############################################################################
#    IR Distance Sensor
###############################################################################
class InfraredProximitySensor(object):
    """
    The infrared sensor when it is in the mode in which it emits infrared light
    and uses the reflected information to estimate distance to the nearest
    object in its field of vision.
    """

    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._ir_sensor = ev3.InfraredSensor('in' + str(port))

    def get_distance(self):
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
        """
        return self._ir_sensor.proximity

    def get_distance_in_inches(self):
        """
        Returns the distance to the nearest object in its field of vision,
        in inches, where about 39.37 inches (which is 100 cm) means no object
        is within its field of vision.
        """
        cm_per_inch = 2.54
        distance = 70 / cm_per_inch * self.get_distance() / 100
        return distance


###############################################################################
#    IR Beacon Sensor
###############################################################################
class InfraredBeaconSensor(object):
    """
    The infrared sensor when it is in the mode in which it measures the
    heading and distance to the Beacon when the Beacon is emitting
    its signal continuously ("beacon mode") on one of its 4 channels (1 to 4).
    """

    def __init__(self, port, channel=1):  # port must be 1, 2, 3 or 4
        self.port = port
        self.channel = channel
        self._ir_sensor = ev3.BeaconSeeker('in' + str(self.port),
                                           channel=channel)

    def set_channel(self, channel):
        """
        Makes this sensor look for signals on the given channel. The physical
        Beacon has a switch that can set the channel to 1, 2, 3 or 4.
        """
        self.channel = channel
        self._ir_sensor = ev3.BeaconSeeker('in' + str(self.port),
                                           channel=channel)

    def get_channel(self):
        return self.channel

    def get_heading_and_distance_to_beacon(self):
        """
        Returns a 2-tuple containing the heading and distance to the Beacon.
        Looks for signals at the frequency of the given channel,
        or at the InfraredAsBeaconSensor's channel if channel is None.
         - The heading is in degrees in the range -25 to 25 with:
             - 0 means straight ahead
             - negative degrees mean the Beacon is to the left
             - positive degrees mean the Beacon is to the right
         - Distance is from 0 to 100, where 100 is about 70 cm
         - -128 means the Beacon is not detected.
        """
        return self._ir_sensor.heading_and_distance

    def get_heading_to_beacon(self):
        """
        Returns the heading to the Beacon.
        Units are per the   get_heading_and_distance_to_beacon   method.
        """
        return self._ir_sensor.heading

    def get_distance_to_beacon(self):
        """
        Returns the heading to the Beacon.
        Units are per the   get_heading_and_distance_to_beacon   method.
        """
        return self._ir_sensor.distance


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

    def __init__(self, port=ev3.INPUT_2):
        try:
            self.low_level_camera = ev3.Sensor(port, driver_name="pixy-lego")
        except AssertionError:
            print("Is the camera plugged into port 2?")
            print("If that is not the problem, then check whether the camera")
            print("has gotten into 'Arduino mode', as follows:")
            print("  In PixyMon, select the gear (Configure) icon,")
            print("  then look for a tab that has 'Arduino' on its page.")
            print("  Make sure it says 'Lego' and not 'Arduino'.")
            print("Note: Only some of the cameras have this option;")
            print("the others are automatically OK in this regard.")
        self.set_signature("SIG1")

    def set_signature(self, signature_name):
        self.low_level_camera.mode = signature_name

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
        """
        return Blob(Point(self.low_level_camera.value(1),
                          self.low_level_camera.value(2)),
                    self.low_level_camera.value(3),
                    self.low_level_camera.value(4))


###############################################################################
# Point (for the Camera class, as well as for general purposes.
###############################################################################
class Point(object):
    def __init__(self, x, y):
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
        self.center = center
        self.width = width
        self.height = height
        self.screen_limits = Point(320, 240)

    def __repr__(self):
        return "center: ({:3d}, {:3d})  width, height: {:3d} {:3d}.".format(
            self.center.x, self.center.y, self.width, self.height)

    def get_area(self):
        return self.width * self.height

    def is_against_left_edge(self):
        return self.center.x - (self.width + 1) / 2 <= 0

    def is_against_right_edge(self):
        return self.center.x + (self.width / 2 + 1) / 2 >= self.screen_limits.x

    def is_against_top_edge(self):
        return self.center.y - (self.height + 1) / 2 <= 0

    def is_against_bottom_edge(self):
        return self.center.y + (self.height + 1) / 2 >= self.screen_limits.y

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
#    ToneMaker
###############################################################################
class ToneMaker(object):
    def __init__(self):
        self._tone_maker = ev3.Sound

    def play_tone(self, frequency, duration):
        """
        Starts playing a tone at the given frequency (in Hz) for the given
        duration (in milliseconds).
        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. Returns a subprocess.Popen,
        so if you want the sound-playing to block until the sound is completed
        (e.g. if the next statement will immediately make another sound),
        then use   tone  like this:
             tone_player = ToneMaker()
             tone_player.play_tone(400, 500).wait()
        :rtype subprocess.Popen
        """
        return self._tone_maker.tone(frequency, duration)

    def play_tone_sequence(self, tones):
        """
        Starts playing a sequence of tones, where each tone is a 3-tuple:
          (frequency, duration, delay_until_next_tone_in_sequence)
        Does NOT block; see   play_tone  above.
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
        ]).wait()
          :rtype subprocess.Popen
        """
        return self._tone_maker.tone(tones)


###############################################################################
#    SpeechMaker
###############################################################################
class SpeechMaker(object):
    def __init__(self):
        self._speech_maker = ev3.Sound

    def speak(self, phrase):
        """
        Speaks the given phrase aloud.
        The phrase must be short.
        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. Returns a subprocess.Popen,
        so if you want the sound-playing to block until the sound is completed
        (e.g. if the next statement will immediately make another sound),
        then use   speak  like this:
             speech_player = SpeechMaker()
             speech_player.speak().wait()
        IMPORTANT:  speak().wait()  does not appear to work correctly in all
        circumstances.  Put a   time.sleep()  after a   speak  as needed.
        :type  phrase:  str
        :rtype subprocess.Popen
        """
        return self._speech_maker.speak(phrase)


###############################################################################
#    SongMaker
###############################################################################
class SongMaker(object):
    pass


###############################################################################
#    LEDs
###############################################################################
class Led(object):
    """
    Each Led has a RED and a GREEN component.
    """
    def __init__(self, left_or_right):
        """
          Constructs a single LED object. Valid left_or_right values:
            "left" or "right"
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
    """ Class to know if a button is pressed on the remote control. """
    def __init__(self, channel_value):
        """
        Creates an object that can be used to check if a button is being
        pressed on the remote control.  You might need as many as four of
        these classes if you used all the channels of the remote.
        Valid channels: 1, 2, 3, or 4
        :type channel: int
        """
        self._remote_control = ev3.RemoteControl(channel=channel_value)

    def red_up(self):
        """
        Returns True if the remote control red up button is pressed
        :rtype bool
        """
        return self._remote_control.red_up

    def red_down(self):
        """
        Returns True if the remote control red down button is pressed
        :rtype bool
        """
        return self._remote_control.red_down

    def blue_up(self):
        """
        Returns True if the remote control blue up button is pressed
        :rtype bool
        """
        return self._remote_control.blue_up

    def blue_down(self):
        """
        Returns True if the remote control blue down button is pressed
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
        :rtype bool
        """
        return self._buttons.up

    def down(self):
        """
        Returns True if the EV3 brick down button is pressed
        :rtype bool
        """
        return self._buttons.down

    def left(self):
        """
        Returns True if the EV3 brick left button is pressed
        :rtype bool
        """
        return self._buttons.left

    def right(self):
        """
        Returns True if the EV3 brick right button is pressed
        :rtype bool
        """
        return self._buttons.right

    def backspace(self):
        """
        Returns True if the EV3 brick backspace button is pressed
        :rtype bool
        """
        return self._buttons.backspace

# Coming soon with ev3dev2...
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
