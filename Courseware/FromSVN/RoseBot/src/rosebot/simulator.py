"""
Simulator.
"""

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb


class Simulator(object):

    def __init__(self, robots=None, root=None, parent=None,
                 width=600, height=400, background='grey',
                 canvas_options=None, gui=None,
                 milliseconds_per_cycle=50,
                 robot_milliseconds_per_cycle=50):
        """
        Optional arguments are:
        -- robot:
             Either a single RoseBot, or a sequence of RoseBots.
             If None, the sequence of RoseBots is set to an empty list.
        -- gui:
             A SimulatorGUI in which the simulator's results are shown.
             If None, a SimulatorGUI will be constructed.
             If not None,  any arguments that refer to
             "the constructed GUI" will be ignored.
        -- width, height, background, canvas_options:
             The width, height, background color,
             and additional options used for the constructed Canvas.
             The  canvas_options  argument is not yet implemented.
        -- parent:
             A Widget that the constructed Canvas uses as its parent.
             If None, then a Toplevel object is constructed and used
             as the parent.
        -- root:
             The sole  Tk  object for the GUI.
             If None, then a  Tk  object is constructed.
        -- milliseconds_per_cycle:
             The simulation takes this many milliseconds (or more, if
             more is needed) for each of its cycles (iterations).
        -- robot_milliseconds_per_cycle:
             The simulation runs each of its RoseBots for this many
             simulated seconds at each cycle (iteration).
        """
        if isinstance(robots, rb.RoseBot):
            self.robots = [robots]
        else:
            self.robots = robots or []

        self.root = root or tkinter.Tk()
        self.parent = parent or tkinter.Toplevel()
        self.gui = gui or SimGUI(self.robots, parent,
                                 width, height, background)
        self.milliseconds_per_cycle = milliseconds_per_cycle
        self.robot_milliseconds_per_cycle = robot_milliseconds_per_cycle

        # The user must call  run  to start the simulation.
        # By default, the GUI starts out visible.
        self.is_running = False
        self._is_visible = True

    def mainloop(self):
        # CONSIDER - maybe this should NOT be available to the user?
        self.root.mainloop()

    # TODO - Make show and hide be properties via is_visable
    def show(self):
        if not self._is_visible:
            self._is_visible = True
            self.gui.show()

    def hide(self):
        if self._is_visible:
            self._is_visible = False
            self.gui.hide()

    def run(self, show_gui=True):
        self.show() if show_gui else self.hide()
        if not self.is_running:
            self.is_running = True
            self.update()

    def pause(self, show_gui=True):
        self.is_running = False
        self.show() if show_gui else self.hide()

    def update(self):
        if self.is_running:
            # Consider: Should each robot have its own AFTER?
            for robot in self.robots:
                robot_position = robot.update_position(
                    self.gui.get_robots_environment())
                self.gui.move(robot, robot_position)
            self.root.after(self.milliseconds_per_cycle, self.update)


class RobotPath(object):
    def __init__(self, center, start_angle, end_angle, direction):
        self.center = center
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.direction = direction


class RobotPosition(object):
    def __init__(self, center, heading):
        self.center = center  # Point
        self.heading = heading  # float, in radians


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SimGUI(object):

    def __init__(self, robots, parent, width, height, background):
        self.robots = robots

        self.canvas = SimCanvas(parent, robots, width=width,
                                height=height, background=background)

        self.controls_frame = SimControlsFrame()
        self.show()

    def update(self, robot, robot_path):
        self.canvas.update(robot, robot_path)

    def show(self):
        self.canvas.grid(row=1, column=1)
        self.controls_frame.grid(row=1, column=2)

    def hide(self):
        self.canvas.grid_forget()
        self.controls_frame.grid_forget()

    def get_robots_environment(self):
        return self.canvas.robots_environment


class RobotEnvironment(object):
    def __init__(self, width, height):
        pass

        """
        horizontal_scrollbar = ttk.Scrollbar(parent,
                                             orient=tkinter.HORIZONTAL)
        vertical_scrollbar = ttk.Scrollbar(parent,
                                           orient=tkinter.VERTICAL)
        super().__init__(parent,
                         scrollregion=(0, 0, width, height),
                         yscrollcommand=vertical_scrollbar.set,
                         xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar['command'] = self.xview
        vertical_scrollbar['command'] = self.yview
        ttk.Sizegrip(parent).grid(column=1, row=1, sticky=(tkinter.S,
                                                           tkinter.E))

        self.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W,
                                           tkinter.E, tkinter.S))
        horizontal_scrollbar.grid(column=0, row=1, sticky=(tkinter.W,
                                                           tkinter.E))
        vertical_scrollbar.grid(column=1, row=0, sticky=(tkinter.N,
                                                         tkinter.S))
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.lastx, self.lasty = 0, 0

        self.bind("<Button-1>", self.xy)
        self.bind("<B1-Motion>", self.addLine)
        self.bind("<B1-ButtonRelease>", self.doneStroke)

        id = self.create_rectangle(
            (10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
        self.tag_bind(id, "<Button-1>", lambda x: self.setColor("red"))
        id = self.create_rectangle(
            (10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
        self.tag_bind(id, "<Button-1>", lambda x: self.setColor("blue"))
        id = self.create_rectangle((10, 60, 30, 80), fill="black", tags=(
            'palette', 'paletteblack', 'paletteSelected'))
        self.tag_bind(id, "<Button-1>", lambda x: self.setColor("black"))

        self.setColor('black')
        self.itemconfigure('palette', width=5)
        """

#     def xy(self, event):
#         self.lastx, self.lasty = (self.canvasx(event.x),
#                                   self.canvasy(event.y))
#
#     def setColor(self, newcolor):
#         self.color = newcolor
#         self.dtag('all', 'paletteSelected')
#         self.itemconfigure('palette', outline='white')
#         self.addtag('paletteSelected', 'withtag',
#                     'palette%s' % self.color)
#         self.itemconfigure('paletteSelected', outline='#999999')
#
#     def addLine(self, event):
#         x, y = self.canvasx(event.x), self.canvasy(event.y)
#         self.create_line((self.lastx, self.lasty, x, y),
#                          fill=self.color,
#                          width=5, tags='currentline')
#         self.lastx, self.lasty = x, y
#
#     def doneStroke(self, _):
#         self.itemconfigure('currentline', width=1)


class SimCanvas(tkinter.Canvas):
    colors = {'blue', 'green', 'red'}  # TODO add more

    def __init__(self, parent, robots, width, height, background):
        super().__init__(parent, width=width, height=height,
                         background=background)
        self.robots_environment = RobotEnvironment(width, height)
        self.sim_robots = {}
        self.make_robots(robots)
        self.draw_axes_and_labels()

    def draw_axes_and_labels(self):
        width, height = self.get_width_and_height()
        self.create_line((0, height // 2, width, height // 2),
                         fill='black', width=5, tags='x_axis')
        self.create_line((width // 2, 0, width // 2, height),
                         fill='black', width=5, tags='y_axis')

    def get_width_and_height(self):
        return int(self.cget('width')), int(self.cget('height'))

    def make_robots(self, robots):
        for k in range(len(robots)):
            robot = robots[k]
            color = self.colors[k % len(self.colors)]
            self.canvas_robots[robot] = self.make_robot(robot)

        self.robot_representations = self.make_robots(robots)

    def make_robot(self, robot):
        # Default is a filled polygon that forms a rectangle.
        pass

    def update(self, robot, robot_position):
        pass


def make_robot_image(self, robot, position=None, color='blue', size=None):
    return self.canvas.create_polygon()


class SimControlsFrame(ttk.Frame):
    def __init__(self):
        super().__init__()
        button = ttk.Button(self, text='Draw walls')
        button.grid()
        button = ttk.Button(self, text='Draw on floor')
        button.grid()


def main():
    test()
    return

    robot = rb.RoseBot()
    root = tkinter.Tk()
    frame0 = ttk.Frame(root)
    frame0.grid()

    sim = Simulator(robot, root, frame0)
    sim.run()
    root.mainloop()


import time


def my_sleep(widget, count, start, rate, seconds):
    if count == 0:
        print((time.time() - start) / seconds)
        return
#     if count % 1000 == 0:
#         print(time.time() - t)

    widget.after(rate, (lambda:
                        my_sleep(widget,
                                 count - rate,
                                 start, rate, seconds)))


def my_sleep2(widget, count, start, rate, seconds):
    for k in range(count // rate):
        time.sleep(rate / 1000)
    print((time.time() - start) / seconds)
#     if count % 1000 == 0:
#         print(time.time() - t)


def test():
    root = tkinter.Tk()
    start = time.time()
    rate = 10
    seconds = 5

    my_sleep2(root, seconds * 1000, start, rate, seconds)
    root.mainloop()

    end = time.time()


main()
