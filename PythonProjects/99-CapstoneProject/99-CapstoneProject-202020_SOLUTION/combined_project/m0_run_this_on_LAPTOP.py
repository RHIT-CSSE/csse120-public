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
  student1_laptop_code.get_my_frame
  student2_laptop_code.get_my_frame
  student3_laptop_code.get_my_frame
  student4_laptop_code.get_my_frame
and displaying the frames thereby obtained.
Hence, most of the "action" really happens in the mX_laptop_code modules.

This code uses what is called "multiple inheritance" to allow the 4 modules
to each have their own "delegate" class in their own modules (and hence
to reduce the likelihood of GIT conflicts).  Your professor will explain
how this fits into your own code when talking about this framework and MQTT.

Authors:  Your professors (for the framework)
    and Dave Fisher testing.
Winter term, 2019-2020.
"""
# TODO: 1.  Put the name of EACH team member in the above.

import tkinter
from tkinter import ttk

import student1_laptop_code
import student2_laptop_code
import student3_laptop_code
import student4_laptop_code

import mqtt_remote_method_calls as mqtt
import set_robot_number


def main():
    """
    This code, which must run on a LAPTOP:
      1. Displays and runs the Graphical User Interface (GUI) (with large parts
           of it of it obtained from the   mX_laptop_code  modules), and
      2. Constructs the MQTT object for SENDING messages to the ROBOT and
           RECEIVING messages from the ROBOT.  ALso constructs a "delegate"
           object to which the MQTT RECEIVER routes messages from the ROBOT.
    """
    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("Team 27: Dave Fisher testing")
    # TODO: 2.  Fill in the XX's above appropriately for your team.

    # -------------------------------------------------------------------------
    # Construct a DELEGATE (for responding to MQTT messages from the robot)
    # and a MQTT SENDER (to send messages to the robot).  The latter gets sent
    # to the   mX_laptop_code   modules via their  get_my_frame   methods.
    # Then  "connect"  the MQTT SENDER to the MQTT server, arranging for
    # messages to go to and from YOUR robot, while also making the
    # MQTT LISTENER start running in a loop in the background.
    # -------------------------------------------------------------------------
    delegate = DelegateForLaptopCode(root)
    mqtt_sender = mqtt.MqttClient(delegate)
    delegate.set_mqtt_sender(mqtt_sender)

    # Use  None  for the robot number to just show the GUI (and NOT connect):
    number = set_robot_number.get_robot_number()
    mqtt_sender.connect_to_mqtt_to_talk_to_robot(lego_robot_number=number)

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()
    # TODO: 3.  Modify the characteristics of the above  main_frame  as desired.

    # -------------------------------------------------------------------------
    # Each team member has their own frame for their own GUI.  Get and grid
    # those frames, sending the objects that the separate GUIs may need.
    # -------------------------------------------------------------------------
    frames = [student1_laptop_code.get_my_frame(main_frame, mqtt_sender, delegate),
              student2_laptop_code.get_my_frame(main_frame, mqtt_sender, delegate),
              student3_laptop_code.get_my_frame(main_frame, mqtt_sender, delegate),
              student4_laptop_code.get_my_frame(main_frame, mqtt_sender, delegate)]

    for k in range(len(frames)):
        if frames[k] is not None:
            frames[k].grid(row=0, column=k)
    # TODO: 4.  Modify the layout of the sub-frames as desired.

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()
    mqtt_sender.close()


class DelegateForLaptopCode(student1_laptop_code.MyLaptopDelegate,
                            student2_laptop_code.MyLaptopDelegate,
                            student3_laptop_code.MyLaptopDelegate,
                            student4_laptop_code.MyLaptopDelegate):
    """
    Uses "multiple inheritance" to route messages to the "delegates"
    in the   mX_laptop_code   modules.
    """
    def __init__(self, root):
        super().__init__(root)

    def set_mqtt_sender(self, mqtt_sender):
        super().set_mqtt_sender(mqtt_sender)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
