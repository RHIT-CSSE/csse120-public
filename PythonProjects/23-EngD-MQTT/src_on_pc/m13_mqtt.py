"""
Example showing for tkinter and ttk:
  -- MQTT for communicating with another device through the Internet.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk
import paho.mqtt.client

UNIQUE_ID = "DavidMutchler1019"  # Use something that no one else will use

PC_TO_DEVICE_TOPIC = UNIQUE_ID + "/pc_to_device"
DEVICE_TO_PC_TOPIC = UNIQUE_ID + "/device_to_pc"
BROKER = "broker.hivemq.com"
TCP_PORT = 1883


def main():
    # Root (main) window and Frame on it.
    root = tkinter.Tk()
    root.title("MQTT example")
    frame = ttk.Frame(root)
    frame.grid()

    # mqtt object, properly initialized.
    mqtt_client = MyMqttClient()

    # Entry box with data to send to the other computer.
    # Button that sends data in the Entry box to the other computer.
    # Label to simulate receiving data from the other computer.
    entry = ttk.Entry(frame)
    entry.grid()

    button = ttk.Button(frame, text="Send Entry box data to the other computer")
    button.grid()
    button["command"] = lambda: send_contents_of_entry_box_via_mqtt(entry,
                                                                    mqtt_client)

    label = ttk.Label(frame, text="No data yet")
    label.grid()
    mqtt_client.label_for_message_from_device = label

    # Stay in the event loop for the rest of the program's run.
    root.mainloop()


class MyMqttClient(paho.mqtt.client.Client):
    def __init__(self):
        super().__init__()
        self.on_connect = on_connect
        self.on_message = on_message
        self.label_for_message_from_device = None  # Set later

        print("Connecting to the broker...")
        self.connect(BROKER, TCP_PORT)
        self.loop_start()
        self.subscribe(DEVICE_TO_PC_TOPIC)


def on_connect(client, userdata, flags, rc):
    print("Connected to the broker.\n")


def on_message(mqtt_client, userdata, message_packet):
    """ Called when a message arrives.  Display it on Console and in GUI. """
    message = message_packet.payload.decode()
    print("Received message:", message)  # Show on the Console
    mqtt_client.label_for_message_from_device["text"] = message  # Show in GUI


def send_contents_of_entry_box_via_mqtt(entry, mqtt_client):
    """ Publish (send to other device) the string in the given ttk.Entry. """
    message = entry.get()
    print("Sending", message)  # For debugging, as needed
    mqtt_client.publish(PC_TO_DEVICE_TOPIC, message)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
