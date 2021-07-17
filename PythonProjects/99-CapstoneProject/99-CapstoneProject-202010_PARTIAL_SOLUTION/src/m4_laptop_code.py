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
Fall term, 2019-2020.
"""
# TODO: 1. Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, main_frame, mqtt_sender):
    """
    Constructs your GUI, putting it into a ttk.Frame that is returned.
      :type root:  tkinter.Tk
      :type main_frame:  ttk.Frame
      :type mqtt_sender  mqtt.MqttClient
    """

    # -------------------------------------------------------------------------
    # Construct your frame:
    # -------------------------------------------------------------------------
    frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="PUT_YOUR_NAME_HERE")
    frame_label.grid()
    # TODO: 2.  Put your name in the above.
    #    Adjust your frame's characteristics as desired.

    # -------------------------------------------------------------------------
    # Add the rest of your GUI to your frame:
    # -------------------------------------------------------------------------
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    get_teleoperation_frame(root, frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Return your frame:
    # -------------------------------------------------------------------------
    return frame


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


# -----------------------------------------------------------------------------
# TODO: Add more functions here as needed.
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


def get_teleoperation_frame(root, window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  root:         tkinter.Tk
      :type  window:       ttk.Frame | ttk.TopLevel
      :type  mqtt_sender:  mqtt.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Go Forward")
    backward_button = ttk.Button(frame, text="Go Backward")
    left_button = ttk.Button(frame, text="Spin Left")
    right_button = ttk.Button(frame, text="Spin Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def go(mqtt_sender, direction, left_wheel_speed, right_wheel_speed):
    """
    Sends a message to the robot to go in the given direction
    using the given wheel motor speeds.
      :type mqtt_sender:       mqtt.MqttClient
      :type direction:         str
      :type left_wheel_speed:  int
      :type right_wheel_speed: int
    """
    print()
    print("Sending a message to the robot to", direction)
    print("  using wheel motor speeds:", left_wheel_speed, right_wheel_speed)
    mqtt_sender.send_message("go", [left_wheel_speed, right_wheel_speed])


def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given, thus going FORWARD.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      mqtt.MqttClient
    """
    left = int(left_entry_box.get())
    right = int(right_entry_box.get())
    go(mqtt_sender, "GO FORWARD", left, right)


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes,
    thus going BACKWARD.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      mqtt.MqttClient
    """
    left = -int(left_entry_box.get())
    right = -int(right_entry_box.get())
    go(mqtt_sender, "GO BACKWARD", left, right)


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box,
    thus spinning LEFT.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      mqtt.MqttClient
    """
    left = -int(left_entry_box.get())
    right = int(right_entry_box.get())
    go(mqtt_sender, "SPIN LEFT", left, right)


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
    thus spinning RIGHT.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      mqtt.MqttClient
    """
    left = int(left_entry_box.get())
    right = -int(right_entry_box.get())
    go(mqtt_sender, "SPIN RIGHT", left, right)


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  mqtt.MqttClient
    """
    print()
    print("Sending a message to the robot to STOP.")
    mqtt_sender.send_message("stop", [])