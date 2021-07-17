"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the Sound class, for making different sounds.
Sounds can including beeps, tones, speech, or wav files.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""

###############################################################################
# STUDENTS: This module is ALREADY IMPLEMENTED.
#   READ its code so that you know how to use make various sounds if you wish
#   to do so.  You may also AUGMENT this module if you choose.
###############################################################################
import libs.rosebot_ev3dev_api as ev3dev


###############################################################################
#    Sound
###############################################################################
class Sound(object):
    """
    Module to control different sounds the robot can make.
    """

    def __init__(self):
        """
        Constructs the different types of sound related objects.
          """
        self.beeper = ev3dev.Beeper()
        self.speech_maker = ev3dev.SpeechMaker()
        self.tone_maker = ev3dev.ToneMaker()
        self.wav_file_player = ev3dev.WavFilePlayer()

    def beep(self):
        """
        Starts playing a BEEP sound.

        This method is blocking, meaning the next line of your code will not
        run until the Beeper is done (usually this IS what you want).
        """
        self.beeper.beep()

    def speak(self, phrase):
        """
        Speaks the given phrase aloud.  The phrase must be short.

        This method is blocking, meaning the next line of your code will not
        run until the SpeechMaker is done (usually this IS what you want).

        :param phrase: The string that you would like the robot to say.
        :type  phrase:  str
        """
        self.speech_maker.speak(phrase)

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
        self.tone_maker.play_tone(frequency, duration)

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
        self.tone_maker.play_tone_sequence(tones)

    def play_vader_song(self):
        """
        Plays a Darth Vader song using a list of tones.
        Note: Each tone in the list is a 3 item tuple:
          (frequency, duration ms, delay_until_next_tone_in_sequence ms)
        """
        tone_list = [
            (392, 350, 100), (392, 350, 100), (392, 350, 100),
            (311.1, 250, 100),
            (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100),
            (466.2, 25, 100),
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
            (466.16, 25, 100), (587.32, 700, 100)]
        self.play_tone_sequence(tone_list)

    def play_wav_file(self, file_location_on_robot):
        """
        Plays a WAVE file from a file location.

        This method is blocking, meaning the next line of your code will not
        run until the ToneMaker is done playing (usually this IS what you want).

        :type file_location_on_robot: str
        """
        self.wav_file_player.play(file_location_on_robot)

    def play_lego_wav_file(self):
        # File from http://www.moviesoundclips.net/ev3.Sound.php?id=288
        # Had to convert it to a PCM signed 16-bit little-endian .wav file
        # http://audio.online-convert.com/convert-to-wav
        file_location_on_robot = "assets/awesome_pcm.wav"
        self.play_wav_file(file_location_on_robot)

    def beep_nonblocking(self):
        """
        Starts playing a BEEP sound.

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. See also the   beep   method above.

        :rtype subprocess.Popen
        """
        self.beeper.beep_nonblocking()

    def speak_nonblocking(self, phrase):
        """
        Speaks the given phrase aloud. The phrase must be short.

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. See also the   speak   method above.

        :rtype subprocess.Popen
        """
        self.speech_maker.speak_nonblocking(phrase)

    def play_tone_nonblocking(self, frequency, duration):
        """
        Same as the play_tone method, but...

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. See also the  play_tone  method above.

        :param frequency: Frequency (Hertz) to play
        :type frequency: float
        :param duration: Length of time to play the tone in milliseconds (ms)
        :type duration: float
        """
        self.tone_maker.play_tone_nonblocking(frequency, duration)

    def play_tone_sequence_nonblocking(self, tones):
        """
        Same as the play_tone_sequence method, but...

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. See also the  play_tone_sequence
        method above.

        :param tones: List of 3-tuple tones (frequency, duration_ms, delay_ms)
        :type tones: list of tuple
        """
        self.tone_maker.play_tone_sequence_nonblocking(tones)

    def play_wav_file_nonblocking(self, file_location_on_robot):
        """
        Same as the play_wav method, but...

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. See also the  play_wav  method above.

        :type file_location_on_robot: str
        """
        self.wav_file_player.play_wav_nonblocking(file_location_on_robot)
