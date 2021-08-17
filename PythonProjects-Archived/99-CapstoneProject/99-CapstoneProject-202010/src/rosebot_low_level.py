"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code contains lower-level code that interacts with the EV3 robot library.

STUDENTS:  *** Do NOT change ANYTHING in this module. ***

Fall term, 2019-2020.
"""

import ev3dev.ev3 as ev3


###############################################################################
# STUDENTS:  *** Do NOT change ANYTHING in this module. ***
###############################################################################

###############################################################################
#    Motor
###############################################################################
class Motor(object):
    # Future enhancements: Add additional methods from the many things
    # an ev3.Motor can do.

    def __init__(self, port, motor_type='large'):
        # port must be 'A', 'B', 'C', or 'D'.
        if motor_type == 'large':
            self._motor = ev3.LargeMotor('out' + port)
        else:
            self._motor = ev3.MediumMotor('out' + port)

    def turn_on(self, speed):  # speed must be -100 to 100
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self):
        self._motor.stop(stop_action="brake")

    def get_position(self):  # Units are degrees (that the motor has rotated).
        return self._motor.position

    def reset_position(self):
        self._motor.position = 0


###############################################################################
#    TouchSensor
###############################################################################
class TouchSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._touch_sensor = ev3.TouchSensor('in' + str(port))

    def is_pressed(self):
        """ Returns True if this TouchSensor is pressed, else returns False """
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
        return self.COLORS[self.get_color()]

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


class SongMaker(object):
    pass


class LED(object):
    """
    Each LED has a RED and a GREEN component.
    """

    def __init__(self, left_or_right):  # Must be "left" or "right"
        self.which_led = left_or_right

        if self.which_led == "left":
            self.which_led_code = ev3.Leds.LEFT
        elif self.which_led == "right":
            self.which_led_code = ev3.Leds.RIGHT

        # Some common colors for an LED.  The two-tuple specifies the
        # brightness of the RED and GREEN components of the LED, respectively.
        self.BLACK = (0, 0)
        self.RED = (1, 0)
        self.GREEN = (0, 1)
        self.AMBER = (1, 1)
        self.ORANGE = (1, 0.5)
        self.YELLOW = (0.1, 1)

    def turn_on(self):
        """
        Sets this LED to 100% of its RED and GREEN, which results in AMBER.
        """
        self.set_color_by_name(self.AMBER)

    def turn_off(self):
        """ Turns this LED off. """
        self.set_color_by_name(self.BLACK)

    def set_color_by_name(self, color_name):
        """
        Sets this LED to the given color (as a name or tuple).  For example:
          left_led = LED("left")
          left_led.set_color_by_name(self.GREEN)
          left_led.set_color_by_name((0.5, 0.33))
        """
        ev3.Leds.set_color(self.which_led_code, color_name)

    def set_color_by_fractions(self, fraction_red, fraction_green):
        """
        Sets the brightness of this LED to the specified amount of
        RED and GREEN, respectively, where each argument is a number
        between 0 (none) and 1 (full brightness).
        Example:
          left_led = LED()
          left_led.set_color(0.5, 0.33)
        """
        self.set_color_by_name((fraction_red, fraction_green))


class BeaconButton(object):
    pass


class BrickButton(object):
    pass