""" Same as m1e_animation, by with no comments, to emphasize the code. """

import random

import tkinter
from tkinter import ttk


def main():
    animation = Animation()
    animation.start()


class Animation(object):
    def __init__(self):
        self.gui = GUI(self)
        self.canvas = self.gui.canvas
        ball = Ball(self.canvas)
        self.balls = [ball]
        self.cycle_ms = 10

    def start(self):
        self.gui.start()

    def run_one_cycle(self):
        r = random.randrange(1, 201)
        if r == 1:
            self.balls.append(Ball(self.canvas))
        for ball in self.balls:
            ball.run_one_cycle()


class GUI(object):
    def __init__(self, animation):
        self.animation = animation
        self.root = tkinter.Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()
        self.canvas = self.make_canvas()
        self.root.after(1000, self.animation_loop)

    def make_canvas(self):
        canvas_width = 400
        canvas_height = 300
        canvas = tkinter.Canvas(self.frame, width=canvas_width,
                                height=canvas_height)
        canvas.width = canvas_width
        canvas.height = canvas_height
        canvas.grid()
        return canvas

    def start(self):
        self.root.mainloop()

    def animation_loop(self):
        self.animation.run_one_cycle()
        self.root.after(self.animation.cycle_ms, self.animation_loop)


class Ball(object):
    def __init__(self, canvas):
        self.canvas = canvas
        x = 200
        y = 200
        self.diameter = 20
        self.colors = ["red", "green", "blue"]
        r = random.randrange(len(self.colors))
        self.color = self.colors[r]
        self.id = self.canvas.create_oval(x, y,
                                          x + self.diameter, y + self.diameter,
                                          fill=self.color)

    def run_one_cycle(self):
        if self.color == "red":
            delta_x = random.randrange(-5, 6)
            delta_y = random.randrange(-2, 3)
            self.canvas.move(self.id, delta_x, delta_y)
        elif self.color == "green":
            x = random.randrange(50, 101)
            y = random.randrange(20, 41)
            self.canvas.coords(self.id, x, y,
                               x + self.diameter, y + self.diameter)
        r1 = random.randrange(1, 101)
        if r1 == 1:
            r2 = random.randrange(len(self.colors))
            self.color = self.colors[r2]
            self.canvas.itemconfigure(self.id, fill=self.color)


main()
