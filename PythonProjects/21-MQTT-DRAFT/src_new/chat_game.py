import mqtt_for_csse120 as mqtt
import time
import tkinter
from tkinter import ttk


class Receiver(object):
    def __init__(self, controller):
        self.controller = controller

    def message_received(self, message):
        print("I have received the following message:")
        print("  --", message)
        self.controller.act_on_message_received(message)


class Sender(object):
    def __init__(self, receiver, who_am_i):
        unique_id = "mutchler"
        if who_am_i == 1:
            self.sender = mqtt.SenderReceiver(unique_id, "one", "two", receiver)
        else:
            self.sender = mqtt.SenderReceiver(unique_id, "two", "one", receiver)

    def send_message(self, message):
        self.sender.send_message(message)


class Controller(object):
    def __init__(self, who_am_i):
        self.gui = None
        self.game = None
        receiver = Receiver(self)
        self.sender = Sender(receiver, who_am_i)

    def set_gui_and_game(self, gui, game):
        self.gui = gui
        self.game = game

    def act_on_message_received(self, message):
        self.game.accept_message_received(message)
        self.gui.update_messages_received(self.game.messages_received)

    def act_on_message_to_send(self, message):
        self.game.accept_message_sent(message)
        self.gui.update_messages_sent(self.game.messages_sent)
        self.sender.send_message(message)


class Game(object):
    def __init__(self):
        self.messages_received = []
        self.messages_sent = []

    def accept_message_received(self, message):
        self.messages_received.append(message)

    def accept_message_sent(self, message):
        self.messages_sent.append(message)


class GUI(object):
    def __init__(self, controller):
        self.controller = controller

        self.root = tkinter.Tk()
        frame = ttk.Frame(self.root, padding=10)
        frame.grid()

        self.messages_sent_label = None
        self.messages_received_label = None
        self.message_to_send_entry = None
        self.make_frame(frame)

    def start(self):
        self.root.mainloop()

    def make_frame(self, frame):
        label1 = ttk.Label(frame, text="Messages received:")
        self.messages_received_label = ttk.Label(frame, text="")

        label2 = ttk.Label(frame, text="Messages sent:")
        self.messages_sent_label = ttk.Label(frame, text="")

        label3 = ttk.Label(frame, text="Next message to send:")
        self.message_to_send_entry = ttk.Entry(frame)
        send_message_button = ttk.Button(frame, text="Send message")
        send_message_button["command"] = lambda: self.send_message()

        label1.grid(row=1, column=0, padx=10)
        self.messages_received_label.grid(row=2, column=0)

        label2.grid(row=1, column=1, padx=10)
        self.messages_sent_label.grid(row=2, column=1)

        label3.grid(row=0, column=0, padx=10)
        self.message_to_send_entry.grid(row=0, column=1)
        send_message_button.grid(row=0, column=2)

    def update_messages_received(self, messages):
        self.messages_received_label["text"] = self.list_to_string(messages)

    def update_messages_sent(self, messages):
        self.messages_sent_label["text"] = self.list_to_string(messages)

    def list_to_string(self, list_of_strings):
        long_string = ""
        for string in list_of_strings:
            long_string = long_string + string + "\n"
        return long_string

    def send_message(self):
        message = self.message_to_send_entry.get()
        self.controller.act_on_message_to_send(message)


def start_game(who_am_i):
    controller = Controller(who_am_i)
    gui = GUI(controller)
    game = Game()
    controller.set_gui_and_game(gui, game)

    gui.start()
