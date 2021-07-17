"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In tests the various SENSORS available to you.

Authors:  Your professors (for the framework).
Winter term, 2019-2020.
"""

###############################################################################
# STUDENTS: This module is ALREADY IMPLEMENTED.
#   RUN it to test the sensors.
#   You may MODIFY or AUGMENT this module as you choose.
###############################################################################

import libs.rosebot as rb
import time


def main():
    """ Tests the   various Sensors   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  various Sensors  of a robot")
    print("--------------------------------------------------")

    # Change the following if you want the readings to appear
    #   more slowly (try 1.0) or more quickly (try 0.1).
    #   The default is half a second between readings.
    seconds_between_readings = 0.5  # Default: 0.5 second between each reading.

    print()
    print("This program displays readings from most")
    print("of the sensors on your Snatch3r robot.")
    print("It also makes sounds.")
    print("  1. If you want to SKIP readings from a")
    print("     particular sensor, or sounds, either:")
    print("      -- comment-out its call in MAIN, or")
    print("      -- press Control-C when that sensor starts.")
    print("  2. The readings are displayed at a rate of")
    print("       {:5.2} seconds per reading, by default.".format(
        seconds_between_readings))
    print("     Change the number in MAIN (or in the function")
    print("     function calls in MAIN), if you want them")
    print("     more quickly or slowly.")

    # Comment-out the tests/readings you want to skip.
    make_sounds()
    print_touch_sensor_readings(seconds_between_readings)
    print_color_sensor_readings(seconds_between_readings)
    print_infrared_proximity_readings(seconds_between_readings)
    print_beacon_sensor_readings(seconds_between_readings)
    print_remote_control_readings(seconds_between_readings)
    print_camera_readings(seconds_between_readings)


def make_sounds():
    try:
        robot = rb.RoseBot()

        print()
        print("--------------------------------------------------")
        print("Demonstrating how to make sounds.")
        print("--------------------------------------------------")

        print()
        print("Remember: Leave time between any sound-making,")
        print("else sounds may be clipped.  If sounds are")
        print("clipped, you may have to reboot the robot.")

        print()
        print("Beep 5 times.")
        for k in range(5):
            robot.sound.beep()
            time.sleep(0.2)

        print()
        print("Play a fun song.")
        robot.sound.play_vader_song()

        print()
        print("Play 5 tones.")
        for tone in range(100, 350, 50):
            duration = 50  # milliseconds
            robot.sound.play_tone(tone, duration)

        print()
        print("Play a 6-tone sequence.")
        robot.sound.play_tone_sequence([(100, 200, 10),
                                        (150, 50, 50),
                                        (200, 100, 10),
                                        (250, 1000, 20),
                                        (300, 50, 5),
                                        (350, 50, 10)])

        print()
        print("Play a WAV file.")
        robot.sound.play_lego_wav_file()

        print()
        print("Speak. Speaking may not work if you make")
        print("other sounds before speaking.")
        print("After speaking, other sounds may fail.")
        print("Leave plenty of time for the speech")
        print("to happen, and use SHORT phrases.")
        robot.sound.speak("Greetings, Earthlings.")
        time.sleep(3)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_touch_sensor_readings(seconds_between_readings):
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("--------------------------------------------------")
    print("Testing the  Touch Sensor  of a robot")
    print("--------------------------------------------------")

    print()
    print("This function displays readings,")
    print("once per {:5.2f} second,".format(seconds_between_readings))
    print("from the physical Touch Sensor that is underneath")
    print("the physical motor at the top of the Arm and Claw.")

    print()
    print("While this test is running, try pressing and releasing")
    print("that physical Touch Sensor to see its readings.")

    print("")
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            print("Pressed (True or False)? Value (0 or 1)?: {:5} {}".format(
                str(robot.touch_sensor.is_pressed()),
                robot.touch_sensor.get_reading()))
            time.sleep(seconds_between_readings)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_color_sensor_readings(seconds_between_readings):
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("--------------------------------------------------")
    print("Testing the  Color Sensor  of a robot")
    print("--------------------------------------------------")

    print()
    print("This function displays readings,")
    print("once per {:5.2f} second,".format(seconds_between_readings))
    print("from the downward-facing physical Color Sensor.")

    print()
    print("While this test is running, try moving the robot around,")
    print("placing the physical Color Sensor on different colors.")

    print()
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            print("As name, number, reflectance: {:8} {:1} {:3}".format(
                robot.color_sensor.get_color_as_name(),
                robot.color_sensor.get_color_as_number(),
                robot.color_sensor.get_reflected_light_intensity()))
            time.sleep(seconds_between_readings)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_infrared_proximity_readings(seconds_between_readings):
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("--------------------------------------------------")
    print("Testing the  Infrared Proximity Sensor  of a robot")
    print("--------------------------------------------------")

    print()
    print("This function displays readings,")
    print("once per {:5.2f} second,".format(seconds_between_readings))
    print("from the forward-facing physical Infrared Proximity")
    print("Sensor (the thing on the front of the claw).")

    print()
    print("While this test is running, try putting your hand")
    print("different distances from that physical Infrared sensor.")

    print()
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")

    try:
        while True:
            print("Distance in inches: {:5.2f}".format(
                robot.infrared_proximity_sensor.get_distance_in_inches()))
            time.sleep(seconds_between_readings)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_beacon_sensor_readings(seconds_between_readings):
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("--------------------------------------------------")
    print("Testing the  Beacon Sensor  of a robot")
    print("--------------------------------------------------")

    print()
    print("This function displays readings,")
    print("once per {:5.2f} second,".format(seconds_between_readings))
    print("from the Beacon (the stand-alone remote-control thing).")

    print()
    print("While this test is running, try turning the Beacon")
    print("on, then moving it to various places in front")
    print("of the robot, as well as places out of the Infrared")
    print("Sensors field of vision. Then try turning the Beacon off.")

    print()
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")

    try:
        while True:
            message = "Distance (inches), heading (sort of degrees): {:3} {:3}"
            print(message.format(robot.beacon_sensor.get_distance(),
                                 robot.beacon_sensor.get_heading()))
            time.sleep(seconds_between_readings)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_remote_control_readings(seconds_between_readings):
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("--------------------------------------------------")
    print("Testing the  Remote Control Sensor  of a robot")
    print("--------------------------------------------------")

    print()
    print("This function displays readings,")
    print("once per {:5.2f} second,".format(seconds_between_readings))
    print("from the Remote Control (the stand-alone thing).")

    print()
    print("While this test is running, try pressing the")
    print("Remote Control's four buttons (one at a time)")
    print("while pointing the Remote Control toward the front")
    print("of the robot (and elsewhere too).")
    print()
    print("Also try the red switch as its four settings.")
    print("When no button is pressed, nothing will be printed.")

    print()
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")

    try:
        while True:
            for red_switch in [1, 2, 3, 4]:
                for button in ["red_up", "red_down", "blue_up", "blue_down"]:
                    if robot.remote_control.is_pressed(red_switch, button):
                        msg = "Button {} with red switch at {} is pressed."
                        print(msg.format(button, red_switch))
            time.sleep(seconds_between_readings)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_camera_readings(seconds_between_readings):
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("--------------------------------------------------")
    print("Testing the  Camera  of a robot")
    print("--------------------------------------------------")

    print()
    print("This function displays readings,")
    print("once per {:5.2f} second,".format(seconds_between_readings))
    print("from the Camera.")

    print()
    print("Before running this test, train your Camera")
    print("on a colored object to get a good color model.")
    print("Also, make sure the Camera is NOT")
    print("in Arduino mode.")

    print()
    print("While this test is running, try putting the object")
    print("that you used for training in front of the physical")
    print("camera, then slowly moving it to various places")
    print("to the left/right and up/down, as well as")
    print("places out of the Camera's field of vision.")

    print()
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")

    try:
        while True:
            blob = robot.camera.get_biggest_blob()
            print(blob)
            time.sleep(seconds_between_readings)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")
