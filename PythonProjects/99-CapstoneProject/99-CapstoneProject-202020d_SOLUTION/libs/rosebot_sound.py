"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the Sound class, for making different sounds.  Sounds
can including beeps, tones, speech, or wav files.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.


import rosebot_ev3dev_api as rose_ev3


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
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.beeper = rose_ev3.Beeper()
        self.speech_maker = rose_ev3.SpeechMaker()
        self.tone_maker = rose_ev3.ToneMaker()
        self.wav_file_player = rose_ev3.WavFilePlayer()

    def beep(self):
        """ Makes the robot beep. """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.beeper.beep()

    def speak(self, phrase):
        """
          Makes the robot speak the given phrase
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.speech_maker.speak(phrase)

    def play_tone(self, frequency, duration):
        """
        Plays a tone at the given frequency for the given duration.
        :param frequency: frequency for the tone (Hertz)
        :type frequency: float
        :param duration: length of time to play the tone in milliseconds (ms)
        :type duration: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.tone_maker.play_tone(frequency, duration)

    def play_vader_song(self):
        """
        Plays a Darth Vader song using a list of tones.
        Note: Each tone in the list is a 3 item tuple:
          (frequency, duration ms, delay_until_next_tone_in_sequence ms)
        """
        tone_list = [
            (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
            (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
            (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
            (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
            (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
            (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
            (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
            (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100),
            (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
            (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
            (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100),
            (466.16, 25, 100), (587.32, 700, 100)]
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.tone_maker.play_tone_sequence(tone_list)

    def play_lego_wav_file(self):
        # File from http://www.moviesoundclips.net/ev3.Sound.php?id=288
        # Had to convert it to a PCM signed 16-bit little-endian .wav file
        # http://audio.online-convert.com/convert-to-wav
        file_location_on_robot = "/home/robot/csse120/assets/awesome_pcm.wav"
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.wav_file_player.play(file_location_on_robot)
