"""
Capstone Team Project.  Code to run on a LAPTOP (NOT the robot).

This module intentionally has NO   main   function.

Instead, the one and only   main   function for LAPTOP code is in module
  m0_run_this_on_LAPTOP
When  m0_run_this_on_LAPTOP  runs, it calls its  main   to construct the one
and only  tkinter.Tk  object and runs  mainloop  on it.  The  m0  module calls
   get_my_frame
in THIS module to get and display the   ttk.Frame  object for the code herein.
See the doc-string in    m0_run_this_on_LAPTOP   for details.

The   m0_run_this_on_LAPTOP module   also constructs the MQTT object and
  1. Sends it to your   get_my_frame   function to use as you see fit
       for SENDING messages to the robot.
  2. Calls methods in your "delegate" class below when it RECEIVES messages
       from the robot.

Your professor will explain further when talking about MQTT and this code.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. Put your name in the above.

import tkinter
from tkinter import ttk

from libs import mqtt_remote_method_calls as mqtt


def get_my_frame(main_frame, mqtt_sender, delegate):
    """
    Constructs your GUI, putting it into a ttk.Frame that is returned.
      :type main_frame:  ttk.Frame
      :type mqtt_sender  mqtt.MqttClient
      :type delegate:    MyLaptopDelegate
    """

    # -------------------------------------------------------------------------
    # Construct your frame:
    # -------------------------------------------------------------------------
    frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="David Fisher")
    frame_label.grid()
    # TODO: 2.  Put your name in the above.
    #    Adjust your frame's characteristics as desired.

    # -------------------------------------------------------------------------
    # Add the rest of your GUI to your frame:
    # -------------------------------------------------------------------------
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    # -------------------------------------------------------------------------
    # Return your frame:
    # -------------------------------------------------------------------------
    return frame


# -----------------------------------------------------------------------------
# TODO: Add functions here as needed.
# -----------------------------------------------------------------------------
def print_message_received(method_name, arguments):
    print()
    print("The laptop's delegate has received a message")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def print_message_sent(method_name, arguments):
    print()
    print("The laptop has SENT a message to the ROBOT")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


# -----------------------------------------------------------------------------
# The  MyLaptopDelegate   class has methods that are called on the delegate
#   object by the process running in the background that listens
#   for messages received from the robot (via the Broker).
# -----------------------------------------------------------------------------
class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # -------------------------------------------------------------------------
    # TODO: Add methods here as needed.
    # -------------------------------------------------------------------------
