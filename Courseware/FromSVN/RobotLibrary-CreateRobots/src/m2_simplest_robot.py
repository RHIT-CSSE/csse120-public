"""
This module is a VERY BASIC introduction to the Create robot.
We'll use it to:
  -- Help you figure out the mechanics of establishing and using
       a Bluetooth connection to the robot.
  -- Serve as a basic example.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and PUT YOUR NAME HERE.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import safest_create
import time

# ----------------------------------------------------------------------
# TODO 2: READ the program below and RUN it (with your robot if you can
#         or the simulator if your robot is not working for you today).
#
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it, THEN:
#
#     ** Put  I GET IT  anywhere in this pink comment ** other than this line.
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
# ----------------------------------------------------------------------


def main():
    """ Calls  robot  to run your robot code in  run_robot  safely. """
    # ------------------------------------------------------------------
    # Set the port to whatever COM number YOUR laptop is using
    # for its connection to the BAM on the Create robot.
    # Leave  run_despite_sensor_garbage  False.
    # ------------------------------------------------------------------
    port = 26  # 'sim'  # 102  # Use YOUR laptop's COM number
    run_despite_sensor_garbage = False

    # Always run your robot code by using start_robot:
    start_robot(port, run_despite_sensor_garbage)


def start_robot(port, run_despite_sensor_garbage):
    """
    Constructs a robot and calls   run_MY_robot, sending it the robot.
     ** Put all YOUR code in the  run_MY_robot  function. **

    The code in this function ensures that the robot calls its  shutdown
    method even if the code breaks.  DO NOT MODIFY THIS FUNCTION.
    """
    try:
        # --------------------------------------------------------------
        # 1. Construct a robot using the given port.
        # --------------------------------------------------------------
        robot = safest_create.Create(port, run_despite_sensor_garbage)

        # --------------------------------------------------------------
        # 2. Run YOUR robot code.
        # --------------------------------------------------------------
        run_MY_robot(robot)

        # --------------------------------------------------------------
        # 3. If the robot was constructed, execute a   robot.shutdown()
        #    to leave the robot in a clean state.
        # --------------------------------------------------------------
        if robot:
            robot.shutdown()

    except safest_create.RobotError:
        # If this Exception is raised, the  safest_create  code has already
        # done a  robot.shutdown()  and printed a sensible error message.
        # So nothing more needs to be done in this case.
        pass
    except:
        # Any other Exception: attempt a  robot.shutdown().
        # Then raise the Exception so the student can see its message.
        if robot:
            robot.try_shutdown()
        raise


def run_MY_robot(robot):

    # ------------------------------------------------------------------
    # Start moving:
    #   -- left wheel at 30 centimeters per second forwards,
    #   -- right wheel at 25 centimeters per second forwards.
    # (so forward but veering to the right).
    # Sleep for 4 seconds (while doing the above motion),
    # then stop.
    # ------------------------------------------------------------------

    robot.driveDirect(10, 10)
    time.sleep(3)
    robot.stop()
#     robot.print_all_interesting_sensors()
#
#     # ------------------------------------------------------------------
#     # All sensor data is obtained by the   getSensor   method.
#     # The   Sensors  class has constants for all sensor names available.
#     # ------------------------------------------------------------------
#     sensor = safest_create.Sensors.cliff_front_left_signal
#     reflectance = robot.getSensor(sensor)
#     print('Current value of the front left cliff sensor:', reflectance)

    # ------------------------------------------------------------------
    # ALWAYS execute the following before your program ends.  Otherwise,
    # your robot may be left in a funky state and on the NEXT run,
    # it might fail to connect or it might run incorrectly.
    # ------------------------------------------------------------------
#     robot.shutdown()

# ----------------------------------------------------------------------
# TODO 3: Do the DOT trick on a  robot  constructed via the   safest_create
#   library.  That is, at the end of  main  (above), type:
#             robot.
#  (note the DOT) and pause.  Scroll through what it shows.
#  The items with an  M  beside them are the METHODs (aka function
#  attributes), that is, all the things a robot can DO.  Click on the
#    driveDirect  method (for example) to see its documentation.
#
#   When you have done the above, asking questions as needed,
#   and you feel that you understand how to look up the documentation
#   for ANY of the methods that a robot can do:
#
#     ** Put  I GET IT  anywhere in this pink comment ** other than this line.
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
