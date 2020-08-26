""" Same as m1e_communication but without comments, to focus on the code. """

import tkinter
from tkinter import ttk

import old_mqtt_for_csse120 as communicator


def main(who_am_i):
    game = Game(who_am_i)
    game.start()


class Game(object):
    def __init__(self, who_am_i):
        self.gui = GUI(self)
        canvas = self.gui.canvas
        receiver = communicator.Receiver(self)
        self.sender = communicator.Sender(receiver, "something_unique",
                                          who_am_i)
        if who_am_i == 1:
            color = "blue"
        else:
            color = "red"
        self.ball = Ball(color, canvas)

    def start(self):
        self.gui.start()

    def act_on_message_received(self, message):
        message_parts = message.split()
        x = int(message_parts[0])
        y = int(message_parts[1])
        self.ball.move_to(x, y)

    def send_xy(self, x, y):
        self.sender.send_message("{} {}".format(x, y))


class GUI(object):
    def __init__(self, game):
        self.game = game
        self.root = tkinter.Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()
        self.canvas = self.make_canvas()
        self.make_chooser_for_xy()

    def make_canvas(self):
        canvas_width = 400
        canvas_height = 300
        canvas = tkinter.Canvas(self.frame, width=canvas_width,
                                height=canvas_height)
        canvas.width = canvas_width
        canvas.height = canvas_height
        canvas.grid()
        return canvas

    def make_chooser_for_xy(self):
        entry_for_x = ttk.Entry(self.frame)
        entry_for_y = ttk.Entry(self.frame)
        send_button = ttk.Button(self.frame, text="Send X and Y")
        send_button["command"] = lambda: self.send_xy(entry_for_x, entry_for_y)
        entry_for_x.grid()
        entry_for_y.grid()
        send_button.grid()

    def send_xy(self, entry_for_x, entry_for_y):
        x = int(entry_for_x.get())
        y = int(entry_for_y.get())
        self.game.send_xy(x, y)

    def start(self):
        self.root.mainloop()


class Ball(object):
    def __init__(self, color, canvas):
        self.canvas = canvas
        x = 200
        y = 200
        self.diameter = 20
        self.id = self.canvas.create_oval(x, y,
                                          x + self.diameter, y + self.diameter,
                                          fill=color)

    def move_to(self, x, y):
        self.canvas.coords(self.id, x, y, x + self.diameter, y + self.diameter)
