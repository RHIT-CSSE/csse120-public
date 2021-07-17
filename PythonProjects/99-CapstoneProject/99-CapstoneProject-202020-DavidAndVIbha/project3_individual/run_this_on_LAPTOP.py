"""
Capstone Team Project.  Code to run on a LAPTOP (NOT the robot).

This code contains the one and only  MAIN  function for running on the laptop.

This code:
  1. Displays and runs the Graphical User Interface (GUI), and
  2. Talks to the robot (by sending MQTT messages) through the GUI, and
  3. Listens for messages from the robot in the background, and
  4. Acts upon any such messages via its DelegateForLaptopCode object.

In particular, this code constructs the one and only   tkinter.Tk   object
and runs  mainloop   on it.  It obtains most of its GUI (including callbacks)
from calling:
  get_my_frame()
and displaying the frame thereby obtained.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Fall term, 2019-2020.
"""
# TODO: 1.  Put YOUR name in the above.

import tkinter
from tkinter import ttk

import libs.mqtt_remote_method_calls as mqtt
import project3_individual.robot_number as robot_number
import time


def main():
    """
    This code, which must run on a LAPTOP:
      1. Displays and runs the Graphical User Interface (GUI) and
      2. Constructs the MQTT object for SENDING messages to the ROBOT and
           RECEIVING messages from the ROBOT.  ALso constructs a "delegate"
           object to which the MQTT RECEIVER routes messages from the ROBOT.
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
    speed_label = ttk.Label(frame, text="Enter a speed: -100 to 100")
    speed_entry_box = ttk.Entry(frame)

    go_button = ttk.Button(frame, text="Make the robot GO")
    go_button["command"] = lambda: go_callback(mqtt_sender, speed_entry_box)

    stop_button = ttk.Button(frame, text="Make the robot STOP")
    stop_button["command"] = lambda: stop_callback(mqtt_sender)

    speed_label.grid(row=0, column=0)
    speed_entry_box.grid(row=0, column=1)
    go_button.grid(row=1, columnspan=2)
    stop_button.grid(row=2, columnspan=2)
    # TODO: 4. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.

    # TODO: 5. Add widgets as desired to your  main_frame below here:

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
    # TODO: 6. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.

    # Use  None  for the robot number to just show the GUI (and NOT connect):
    number = robot_number.get_robot_number()
    mqtt_sender.connect_to_mqtt_to_talk_to_robot(lego_robot_number=number)
    # TODO: 7. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()
    mqtt_sender.close()
    # TODO: 8. READ and UNDERSTAND the above code.  ASK QUESTIONS as desired.


# TODO: 9. READ and UNDERSTAND the following code.  ASK QUESTIONS as desired.
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


# TODO: 10. READ and UNDERSTAND the following code.  ASK QUESTIONS as desired.
# -----------------------------------------------------------------------------
# TODO: Add more functions here as needed, including CALLBACK functions.
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


def go_callback(mqtt_sender, speed_entry_box):
    """
      :type mqtt_sender:     mqtt.MqttClient
      :type speed_entry_box: ttk.Entry
    """
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("go", [speed])
    print_message_sent("go", [speed])


def stop_callback(mqtt_sender):
    """
      :type mqtt_sender:     mqtt.MqttClient
    """
    mqtt_sender.send_message("stop")
    print_message_sent("stop")