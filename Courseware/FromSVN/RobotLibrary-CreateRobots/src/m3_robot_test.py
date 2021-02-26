"""
Demonstrates most of the methods in the Create (robot) class.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.  September 2015.
"""

import safest_create as create
import time


def main():
    """ Calls  robot  to run your robot code in  run_robot  safely. """
    # ------------------------------------------------------------------
    # Set the port to whatever COM number YOUR laptop is using
    # for its connection to the BAM on the Create robot.
    # Leave   run_despite_sensor_garbage    False.
    # ------------------------------------------------------------------
    port = 26  # 'sim'  # 102  # Use YOUR laptop's COM number
    run_despite_sensor_garbage = False

    # ------------------------------------------------------------------
    # Always run your robot code by using start_robot.
    # It will call  run_MY_robot  to get YOUR robot code running.
    # ------------------------------------------------------------------
    start_robot(port, run_despite_sensor_garbage)


def run_MY_robot(robot):
    """
    YOUR robot code should start here, using given already-connected robot.
    :type robot: create.Create
    """
    demo_singing(robot)
    demo_moving(robot)
    demo_sensing(robot)
    demo_other(robot)


def demo_singing(robot):
    """ :type robot: create.Create """
    print()
    print('Demo/testing singing functions:')
    print('   playNote, playSong, setSong + playSongNumber')

    robot.playNote(50, 128)
#     robot.playNote(-2, 128) # Test error handling
#     robot.playNote(1000, 128) # Test error handling
#     robot.playNote('hi', 128) # Test error handling
#     robot.playNote(50, 1000) # Test error handling
#     robot.playNote(50, 'he') # Test error handling
    wait_for_song_to_finish(robot)
    time.sleep(1)

    robot.playSong([(60, 8), (64, 8), (67, 8), (72, 8)])
    # Test error handling:
#     robot.playSong([('hi', 8), (64, 8), (67, 8), (72, 8)])
#     robot.playSong([(60, 8), (64, 'ho'), (67, 8), (72, 8)])
#     robot.playSong(1)
    wait_for_song_to_finish(robot)
    time.sleep(1)

    robot.setSong(2, [(46, 8), (48, 8), (51, 8), (56, 8), (40, 64)])
    # Test error handling:
#     robot.setSong('hi', [(46, 8), (48, 8), (51, 8), (56, 8), (40, 64)])
#     robot.setSong(2, [('ho', 8), (48, 'he'), (51, 8), (56, 8), (40, 64)])

    robot.playSongNumber(2)
#     robot.playSongNumber(3)  # Test error handling
    wait_for_song_to_finish(robot)
    time.sleep(1)


def wait_for_song_to_finish(robot):
    """ :type robot: create.Create """
    song_sensor = create.Sensors.song_playing
    while True:
        if not robot.getSensor(song_sensor):
            break


def demo_moving(robot):
    """ :type robot: create.Create """
    print()
    print('Demo/testing movement functions: drive, driveDirect, go, stop')

    time.sleep(1)
    robot.playNote(50, 8)
    robot.drive(100, 25, 'CW')
#     robot.drive('hi', 25, 'CW')  # Test error handling
#     robot.drive(10, 0, None)  # Test error handling (treats non-CW as CCW)
    time.sleep(1)
    robot.stop()

    time.sleep(1)
    robot.playNote(50, 8)
    robot.driveDirect(10, 25)
#     robot.driveDirect('10', 25)  # Test error handling
    time.sleep(1)
    robot.stop()

    time.sleep(1)
    robot.playNote(50, 8)
    robot.go(0, 180)
    time.sleep(1)
    robot.go(100, 0)
    time.sleep(1)
    robot.stop()
    robot.go(10, 20)
#     robot.go('10', 25)  # Test error handling
#     robot.go(10, '25')  # Test error handling
#     robot.go(1000, 1000)  # Test error handling
    time.sleep(1)
    robot.stop()


def demo_sensing(robot):
    """ :type robot: create.Create """
    print()
    print('Demo/testing sensing functions: getSensor')

    sensor_name = create.Sensors.cliff_front_left_signal
#     sensor_name = "bad name"  # Test error handling
    value = robot.getSensor(sensor_name)
    print('Value for ' + sensor_name + ': ' + str(value))

    robot.go(0, 90)
    time.sleep(1)
    robot.stop()
    value = robot.getSensor(sensor_name)
    print('Value for ' + sensor_name + ': ' + str(value))

    robot.driveDirect(10, 10)
    for _ in range(100):
        value = robot.getSensor(sensor_name)
        print('Value for ' + sensor_name + ': ' + str(value))
        time.sleep(0.05)

    # Would like to test the error handling on sensor garbage,
    # but it is hard to force that


def demo_other(robot):
    """ :type robot: create.Create """
    pass  # No testing yet.


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
        robot = create.Create(port, run_despite_sensor_garbage)

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

    except create.RobotError:
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
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
