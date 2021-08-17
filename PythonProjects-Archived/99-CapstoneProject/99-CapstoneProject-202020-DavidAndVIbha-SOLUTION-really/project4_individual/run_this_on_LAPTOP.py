"""
Capstone Team Project.  Code to run on a LAPTOP (NOT the robot).

This code contains the one and only  MAIN  function for running on the laptop.

This code:
  1. Displays and runs the Graphical User Interface (GUI), and
  2. Talks to the robot (by sending MQTT messages) through the GUI, and
  3. Listens for messages from the robot in the background, and
  4. Acts upon any such messages via its DelegateForLaptopCode object.

In particular, this code constructs the one and only   tkinter.Tk   object,
puts widgets on it, and runs  mainloop   on it.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Fall term, 2019-2020.
"""
# TODO: 1.  Put YOUR name in the above.

import tkinter
from tkinter import ttk

import libs.mqtt_remote_method_calls as mqtt
import project4_individual.robot_number as robot_number
import time


def main():
    """
    This code, which must run on a LAPTOP:
      1. Displays and runs the Graphical User Interface (GUI).

      2. Constructs the MQTT object for:
           -- SENDING messages to the ROBOT and
           -- RECEIVING messages from the ROBOT.
         ALso constructs a "delegate" object to which the MQTT RECEIVER
         routes messages from the ROBOT.

      3. Puts widgets on the GUI and arranges for buttons et al
           to send appropriate messages to the robot, using callbacks
           and the   send_message   method of the MqttClient class.

      4. Receives messages from the robot and acts upon them,
           via the   DelegateForLaptopCode  object.
    """
    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("Team XX, Person XX")
    # TODO: 2.  Fill in the XX's above appropriately for your team.

    # -------------------------------------------------------------------------
    # The main frame, upon which the widgets (including sub-frames) are placed.
    # -------------------------------------------------------------------------
    frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    frame.grid()
    # TODO: 3.  Modify the characteristics of the above  main_frame  as desired.

    # -------------------------------------------------------------------------
    # Add widgets to your  main_frame  as desired.
    # -------------------------------------------------------------------------
    label_text = "Enter speeds for left and\nright wheels: -100 to 100"
    speed_label = ttk.Label(frame, text=label_text)

    left_speed_entry_box = ttk.Entry(frame)
    right_speed_entry_box = ttk.Entry(frame)

    go_button = ttk.Button(frame, text="Make the robot GO")
    go_button["command"] = lambda: go_callback(mqtt_sender,
                                               left_speed_entry_box,
                                               right_speed_entry_box)

    stop_button = ttk.Button(frame, text="Make the robot STOP")
    stop_button["command"] = lambda: stop_callback(mqtt_sender)

    speed_label.grid(row=0, column=0)
    left_speed_entry_box.grid(row=0, column=1)
    right_speed_entry_box.grid(row=0, column=2)
    go_button.grid(row=1, column=1)
    stop_button.grid(row=1, column=2)

    button_text = "Read sensors, print values on SSH window."
    read_sensors_button = ttk.Button(frame, text=button_text)
    read_sensors_button.grid(row=3, columnspan=3)
    read_sensors_button['command'] = lambda: read_sensors_callback(mqtt_sender)

    # -------------------------------------------------------------------------
    # TODO: 4. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 5. Add widgets as desired to your  main_frame below here:
    # -------------------------------------------------------------------------
    # SOLUTION: REMOVE before giving this to the students.

    # For the Arm and Claw:
    arm_label = ttk.Label(frame, text="Desired arm position:")
    arm_entry_box = ttk.Entry(frame)
    arm_calibrate_button = ttk.Button(frame, text="Calibrate the arm")
    arm_up_button = ttk.Button(frame, text="raise arm all the way UP")
    arm_down_button = ttk.Button(frame, text="lower arm all the way DOWN")
    arm_move_button = ttk.Button(frame, text="Move arm to desired position")

    arm_label.grid(row=4, column=0)
    arm_entry_box.grid(row=4, column=1)
    arm_move_button.grid(row=4, column=2)
    arm_calibrate_button.grid(row=5, column=0)
    arm_up_button.grid(row=5, column=1)
    arm_down_button.grid(row=5, column=2)

    arm_calibrate_button['command'] = lambda: arm_calibrate_callback(
        mqtt_sender)
    arm_move_button['command'] = lambda: arm_move_callback(mqtt_sender,
                                                           arm_entry_box)
    arm_up_button['command'] = lambda: arm_up_callback(mqtt_sender)
    arm_down_button['command'] = lambda: arm_down_callback(mqtt_sender)

    # For the LEDs:
    line1 = "Color to which to set\n"
    line2 = "the LEFT/RIGHT LED:\n"
    line3 = "red, green, amber, or off."
    color_label = ttk.Label(frame, text=line1 + line2 + line3)
    left_led_color_entry_box = ttk.Entry(frame)
    left_led_button = ttk.Button(
        frame, text="Set the LEFT LED\nto the specified color")
    right_led_color_entry_box = ttk.Entry(frame)
    right_led_button = ttk.Button(
        frame, text="Set the RIGHT LED\nto the specified color")

    color_label.grid(row=6, rowspan=2, column=0)
    left_led_color_entry_box.grid(row=6, column=1)
    left_led_button.grid(row=6, column=2)
    right_led_color_entry_box.grid(row=7, column=1)
    right_led_button.grid(row=7, column=2)

    left_led_button['command'] = lambda: set_led_callback(
        mqtt_sender, left_led_color_entry_box, "left")
    right_led_button['command'] = lambda: set_led_callback(
        mqtt_sender, right_led_color_entry_box, "right")

    # -------------------------------------------------------------------------
    # Construct a DELEGATE (for responding to MQTT messages from the robot)
    # and a MQTT SENDER (to send messages to the robot).  The latter gets sent
    # to the   mX_laptop_code   modules via their  get_my_frame   methods.
    # Then  "connect"  the MQTT SENDER to the MQTT server, arranging for
    # messages to go to and from YOUR robot, while also making the
    # MQTT LISTENER start running in a loop in the background.
    # -------------------------------------------------------------------------
    delegate = DelegateForLaptopCode(root, frame)
    mqtt_sender = mqtt.MqttClient(delegate)
    delegate.set_mqtt_sender(mqtt_sender)
    # -------------------------------------------------------------------------
    # TODO: 6. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.
    # -------------------------------------------------------------------------

    # Use  None  for the robot number to just show the GUI (and NOT connect):
    number = robot_number.get_robot_number()
    mqtt_sender.connect_to_mqtt_to_talk_to_robot(lego_robot_number=number)
    # -------------------------------------------------------------------------
    # TODO: 7. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()
    mqtt_sender.close()
    # -------------------------------------------------------------------------
    # TODO: 8. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TODO: 9. READ and UNDERSTAND the following code.  ASK QUESTIONS as desired.
# -----------------------------------------------------------------------------
class DelegateForLaptopCode(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a ROBOT via MQTT.
    """
    def __init__(self, root, frame):
        """
          :type root:  tkinter.Tk
          :type frame  ttk.Frame
        """
        self.root = root
        self.frame = frame
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        """
          :type mqtt_sender:  mqtt.MqttClient
        """
        self.mqtt_sender = mqtt_sender

    # -------------------------------------------------------------------------
    # TODO: Add methods here as needed.
    # -------------------------------------------------------------------------

    # SOLUTION: REMOVE before giving this to the students.


# -----------------------------------------------------------------------------
# TODO: 10. READ and UNDERSTAND the following code.  ASK QUESTIONS as desired.
# -----------------------------------------------------------------------------
def print_message_received(method_name, arguments=None):
    print()
    print("The laptop's delegate has received a message")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def print_message_sent(method_name, arguments=None):
    print()
    print("The laptop has SENT a message to the ROBOT")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def go_callback(mqtt_sender, left_speed_entry_box, right_speed_entry_box):
    """
      :type mqtt_sender:              mqtt.MqttClient
      :type left_speed_entry_box: ttk.Entry
      :type right_speed_entry_box ttk.Entry
    """
    left_speed = int(left_speed_entry_box.get())
    right_speed = int(right_speed_entry_box.get())

    mqtt_sender.send_message("go", [left_speed, right_speed])
    print_message_sent("go", [left_speed, right_speed])


def stop_callback(mqtt_sender):
    """ :type mqtt_sender: mqtt.MqttClient """
    mqtt_sender.send_message("stop")
    print_message_sent("stop")


def read_sensors_callback(mqtt_sender):
    """ :type mqtt_sender: mqtt.MqttClient """
    mqtt_sender.send_message("read_sensors")
    print_message_sent("read_sensors")


# -----------------------------------------------------------------------------
# TODO: Add more functions here as needed, including CALLBACK functions.
# -----------------------------------------------------------------------------
# SOLUTION: REMOVE before giving this to the students.
def arm_calibrate_callback(mqtt_sender):
    """ :type mqtt_sender: mqtt.MqttClient """
    mqtt_sender.send_message("arm_calibrate")
    print_message_sent("arm_calibrate")


def arm_up_callback(mqtt_sender):
    """ :type mqtt_sender: mqtt.MqttClient """
    mqtt_sender.send_message("arm_up")
    print_message_sent("arm_up")


def arm_down_callback(mqtt_sender):
    """ :type mqtt_sender: mqtt.MqttClient """
    mqtt_sender.send_message("arm_down")
    print_message_sent("arm_down")


def arm_move_callback(mqtt_sender, entry_box):
    """
    :type mqtt_sender: mqtt.MqttClient
    :type entry_box:   ttk.Entry
    """
    mqtt_sender.send_message("arm_move", int(entry_box.get()))
    print_message_sent("arm_move", int(entry_box.get()))


def set_led_callback(mqtt_sender, entry_box, left_or_right):
    """
    :type mqtt_sender:   mqtt.MqttClient
    :type entry_box:     ttk.Entry
    :type left_or_right: str
    """
    mqtt_sender.send_message("set_led", [entry_box.get(), left_or_right])
    print_message_sent("set_led", [entry_box.get(), left_or_right])
