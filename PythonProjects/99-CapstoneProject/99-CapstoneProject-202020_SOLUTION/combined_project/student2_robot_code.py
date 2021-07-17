"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module intentionally has NO   main   function.

Instead, the one and only   main   function for ROBOT code is in module
  m0_run_this_on_ROBOT
When  m0_run_this_on_ROBOT  runs, it calls its   main   to construct a robot
(with associated objects) and sits in an infinite loop waiting to RECEIVE
messages from the LAPTOP code.  When the   m0_run_this_on_ROBOT   code receives
a message from the LAPTOP that is destined for YOUR "delegate" code, it calls
the relevant method which YOU define in the  MyRobotDelegate  class below.

See the doc-string in    m0_run_this_on_ROBOT   for details.
Your professor will explain further when talking about MQTT and this code.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. Put your name in the above.

from libs import mqtt_remote_method_calls as mqtt, rosebot


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """

    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot loop

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # -------------------------------------------------------------------------
    # TODO: Add methods here as needed.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TODO: Add more functions here as needed.
# -----------------------------------------------------------------------------
def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def print_message_sent(method_name, arguments):
    print()
    print("The robot has SENT a message to the LAPTOP")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)
