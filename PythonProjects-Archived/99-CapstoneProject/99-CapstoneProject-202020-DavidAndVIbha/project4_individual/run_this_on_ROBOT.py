"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).
This is the  INDIVIDUAL  part of the project.

This code contains the one and only  MAIN  function for running on the robot.

This code constructs a robot with an associated MQTT object and runs an
infinite loop while listening for messages from the laptop and responding to
them via its "delegate" object.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Fall term, 2019-2020.
"""
# TODO: 1.  Put YOUR name in the above.

import time
import libs.rosebot as rb
import libs.mqtt_remote_method_calls as mqtt
import project4_individual.robot_number as robot_number


# TODO: 2. READ and UNDERSTAND the following code.  ASK QUESTIONS as desired.
def main():
    """
    This code, which must run on the ROBOT:
      1. Constructs a robot, an MQTT SENDER, and a DELEGATE to respond
           to messages FROM the LAPTOP sent TO the ROBOT via MQTT.
      2. Stays in an infinite loop while a listener (for MQTT messages)
           runs in the background, "delegating" work to the "delegate".
    """
    robot = rb.RoseBot()

    delegate = DelegateForRobotCode(robot)
    mqtt_sender = mqtt.MqttClient(delegate)
    delegate.set_mqtt_sender(mqtt_sender)

    number = robot_number.get_robot_number()
    mqtt_sender.connect_to_mqtt_to_talk_to_laptop(lego_robot_number=number)

    time.sleep(1)  # To let the connection process complete
    print()
    print("Starting to listen for messages. The delegate responds to them.")
    print()

    # Stay in an infinite loop while the listener (for MQTT messages)
    # runs in the background:
    while True:
        time.sleep(0.01)
        if delegate.is_time_to_quit:
            break


# TODO: 3. READ and UNDERSTAND the following code.  ASK QUESTIONS as desired.
class DelegateForRobotCode(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        """
          :type robot: rb.RoseBot
        """
        print("Constructing a delegate for the Robot.")
        self.robot = robot  # type: rb.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot loop

    def set_mqtt_sender(self, mqtt_sender):
        """
          :type mqtt_sender: mqtt.MqttClient
        """
        print("Setting the MqttClient associated with this delegate.")
        self.mqtt_sender = mqtt_sender

    def go(self, speed):
        print_message_received("go", [speed])
        self.robot.drive_system.go(speed, speed)

    def stop(self):
        print_message_received("stop")
        self.robot.drive_system.stop()

    # -------------------------------------------------------------------------
    # TODO: Add methods here as needed.
    # -------------------------------------------------------------------------


# TODO: 4. READ and UNDERSTAND the following code.  ASK QUESTIONS as desired.
# -----------------------------------------------------------------------------
# TODO: Add more functions here as needed.
# -----------------------------------------------------------------------------
def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def print_message_sent(method_name, arguments=None):
    print()
    print("The robot has SENT a message to the LAPTOP")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,')
    print('your code raised the following exception:')
    print()
    time.sleep(1)
    raise
