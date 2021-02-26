"""
Demonstrates how to run the robot code SAFELY, that is,
with every attempt made to always do a  shutdown()  on the robot,
even if the code breaks.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.  September 2015.
"""

import safest_create
import time


def main():
    """ Calls  robot  to run your robot code in  run_robot  safely. """
    # ------------------------------------------------------------------
    # Set the port to whatever COM number YOUR laptop is using
    # for its connection to the BAM on the Create robot.
    # Leave   run_despite_sensor_garbage    False.
    # ------------------------------------------------------------------
    port = 'sim'  # 'sim'  # 102  # Use YOUR laptop's COM number
    run_despite_sensor_garbage = False

    # ------------------------------------------------------------------
    # Always run your robot code by using start_robot.
    # It will call  run_MY_robot  to get YOUR robot code running.
    # ------------------------------------------------------------------
    start_robot(port, run_despite_sensor_garbage)


def run_MY_robot(robot):
    """
    YOUR robot code should start here, using given already-connected robot.
    :type robot: safest_create.Create
    """
    # ------------------------------------------------------------------
    # Start moving:
    #   -- left wheel at 30 centimeters per second forwards,
    #   -- right wheel at 25 centimeters per second forwards.
    # (so forward but veering to the right).
    # Sleep for 3 seconds (while doing the above motion),
    # then stop.
    # ------------------------------------------------------------------

    robot.driveDirect(30, 25)
    time.sleep(3)
    robot.stop()

    # ------------------------------------------------------------------
    # All sensor data is obtained by the   getSensor   method.
    # The   Sensors  class has constants for all sensor names available.
    # ------------------------------------------------------------------
    sensor = safest_create.Sensors.cliff_front_left_signal
    reflectance = robot.getSensor(sensor)
    print('Current value of the front left cliff (reflectance) sensor:',
          reflectance)


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

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
