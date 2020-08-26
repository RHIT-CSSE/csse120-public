import random

import tkinter
from tkinter import ttk


class Raindrop(object):
    def __init__(self, canvas, x, y, width=5, height=10, color="blue"):
        self.canvas = canvas
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        self.color = color
        self.speed = random.randint(5, 18)

        self.id = None  # Set by next statement
        self.draw()
        self.is_active = True

    def draw(self):
        self.id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
                                          fill=self.color)

    def move(self):
        self.y1 = self.y1 + self.speed
        self.y2 = self.y2 + self.speed

        if self.y1 > self.canvas.height:
            self.is_active = False
        elif self.y1 > 200:
            self.color = "red"

    def redraw(self):
        self.canvas.coords(self.id, self.x1, self.y1, self.x2, self.y2)
        self.canvas.itemconfigure(self.id, fill=self.color)

    def handle_inactive(self):
        self.canvas.delete(self.id)


class Cloud:
    def __init__(self, canvas, x, y, color="black"):
        self.canvas = canvas
        self.center_x = x
        self.center_y = y
        self.color = color
        self.speed = random.randint(5, 18)

        self.id = self.cloud_image = None  # Set by next statement
        self.draw()
        self.is_active = True

    def draw(self):
        self.cloud_image = tkinter.PhotoImage(file="cloud.png")
        self.id = self.canvas.create_image(100, 30, image=self.cloud_image)

    def move(self):
        x_amount = random.randrange(-5, 6)
        self.center_x = self.center_x + x_amount

    def redraw(self):
        self.canvas.coords(self.id, self.center_x, self.center_y)

    def rain(self, game_objects):
        rain_x = random.randint(self.center_x - 50, self.center_x + 50)
        new_raindrop = Raindrop(self.canvas, rain_x, self.center_y + 30)
        game_objects.append(new_raindrop)

    def handle_inactive(self):
        pass


class Game(object):
    def __init__(self, cycle_ms=10):
        self.gui = GUI(self)

        self.cycle_ms = cycle_ms
        self.game_objects = []

        self.cloud = Cloud(self.gui.canvas, 150, 20)
        self.game_objects.append(self.cloud)

    def run_one_cycle(self):
        self.move_objects()
        self.remove_inactive_objects()
        self.redraw_objects()

        self.cloud.rain(self.game_objects)

    def move_objects(self):
        for game_object in self.game_objects:
            game_object.move()

    def redraw_objects(self):
        for game_object in self.game_objects:
            game_object.redraw()

    def remove_inactive_objects(self):
        active_game_objects = []
        for game_object in self.game_objects:
            if game_object.is_active:
                active_game_objects.append(game_object)
            else:
                game_object.handle_inactive()
        self.game_objects = active_game_objects


class GUI(object):
    def __init__(self, game):
        self.game = game

        self.root = tkinter.Tk()
        frame = ttk.Frame(self.root, padding=10)
        frame.grid()

        self.make_canvas(frame)
        self.root.after(1000, self.game_loop)

    def make_canvas(self, frame):
        canvas_width = 400
        canvas_height = 300
        self.canvas = tkinter.Canvas(frame, width=canvas_width,
                                     height=canvas_height)
        self.canvas.width = canvas_width
        self.canvas.height = canvas_height
        self.canvas.grid()

    def start(self):
        self.root.mainloop()

    def game_loop(self):
        self.game.run_one_cycle()
        self.root.after(self.game.cycle_ms, self.game_loop)


def main():
    game = Game()
    game.gui.start()


main()