"""
THROW-AWAY Capstone Project. If you mess up this THROW-AWAY project,
  ** no worries. **
It lets you practice skills & concepts needed for the REAL Capstone Project.

This module contains code intended to run directly on the EV3 robot
(NOT on a laptop, NOT via a GUI running on a laptop).
It TESTS the   TouchSensor   class that is in the  libs  folder.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# -----------------------------------------------------------------------------
# NOTE to students: Start this exercise WITH YOUR INSTRUCTOR.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 1.  If you have not already done so, with your instructor,
#  READ and UNDERSTAND the  HowToShareModules.pdf  document in this project.
#    -- If you understand it, change this _TODO_ to DONE.
#    -- Otherwise, ** do NOT modify this module **
#         and get help before continuing.
#  _
#  Throughout this module, ** use the process in HowToShareModules.pdf. **
#  _
#  In particular, *** only ONE team member should modify this file ***
#    (but often pair-programming using the same computer).
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 2. Change the   PUT_YOUR_NAMES_HERE   above to the names of
#  EACH team member who contributes (in any way) to this module.
#  _
#  REMINDER: Use ONLY ** ONE ** team member's computer to make changes herein.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 3. With your instructor, import the modules needed herein:
#     from libs import rosebot_touch_sensor
#     time
#  Make sure you understand WHY those imports are needed.
# -----------------------------------------------------------------------------


def main():
    """ Calls the desired TEST functions. """
    # -------------------------------------------------------------------------
    # TODO: 4. With your instructor, construct a TouchSensor, that is,
    #          a   rosebot_touch_sensor.TouchSensor(1)   object.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 5. Un-comment the first TEST function below.
    #  Re-comment it when you are finished using its tests,
    #  and then proceed to the next TEST function below.
    # -------------------------------------------------------------------------
    # run_test_get_reading(touch_sensor)
    # run_test_is_pressed(touch_sensor)
    # run_test_wait_until_pressed(touch_sensor)
    # run_test_wait_until_released(touch_sensor)


def run_test_get_reading(touch_sensor):
    """
    Tests the  get_reading  method of the  TouchSensor  class.
    :type touch_sensor rosebot_touch_sensor.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   get_reading   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Stop this program by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")

    while True:
        # -------------------------------------------------------------------------
        # TODO: 6. Call the   get_reading   method on the given TouchSensor
        #   object and print the returned value.  Then sleep for 0.5 seconds
        #   so that we are not overwhelmed by the output.
        # -------------------------------------------------------------------------
        pass


def run_test_is_pressed(touch_sensor):
    """
    Tests the  is_pressed  method of the  TouchSensor  class.
    :type touch_sensor rosebot_touch_sensor.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   is_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Stop this program by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")

    while True:
        # -------------------------------------------------------------------------
        # TODO: 7. Call the   is_pressed   method on the given TouchSensor
        #   object and print the returned value.  Then sleep for 0.5 seconds
        #   so that we are not overwhelmed by the output.
        # -------------------------------------------------------------------------]
        pass


def run_test_wait_until_pressed(touch_sensor):
    """
    Tests the  wait_until_pressed  method of the  TouchSensor  class.
    :type touch_sensor rosebot_touch_sensor.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   wait_until_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Press the ENTER key when ready")
    input("to wait until the Touch Sensor is pressed.")

    # -------------------------------------------------------------------------
    # TODO: 8. Call the  wait_until_pressed  method of the  TouchSensor  class.
    #   Print a relevant message when the function call returns.
    # -------------------------------------------------------------------------


def run_test_wait_until_released(touch_sensor):
    """
    Tests the  wait_until_released  method of the  TouchSensor  class.
    :type touch_sensor rosebot_touch_sensor.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   wait_until_released   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Press the ENTER key when ready")
    input("to wait until the Touch Sensor is released.")

    # -------------------------------------------------------------------------
    # TODO: 9. Call the  wait_until_released  method of the  TouchSensor  class.
    #   Print a relevant message when the function call returns.
    # -------------------------------------------------------------------------


main()

