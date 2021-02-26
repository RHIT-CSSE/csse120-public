import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import time
from enum import Enum, unique


@unique
class ConnectionType(Enum):
    wired = 1
    wireless = 2

# Set this to whatever you want to appear in the default PORT Entry box.
DEFAULT_PORT = '/dev/cu.usbserial-AL00F14M'

# ----------------------------------------------------------------------
# MAIN starts here:
# ----------------------------------------------------------------------


def main():

    root = tkinter.Tk()
    robot = rb.RoseBot()

    frame = ttk.Frame(root, padding=10)
    frame.grid()

    connection_gui(frame, robot, DEFAULT_PORT)
    blink_tone_gui(frame, robot)
    movement_gui(frame, robot)
    sensor_gui(frame, robot)
    pixy_gui(frame, robot)

    root.mainloop()


# ----------------------------------------------------------------------
# Functions for making subframes and such:
# ----------------------------------------------------------------------
def make_subframe(frame, frame_text):
    label = ttk.Label(text=frame_text + '\n\n',
                      font=('Helvetica', '16', 'bold'),
                      width=20)
    subframe = ttk.LabelFrame(frame,
                              labelwidget=label,
                              labelanchor='w')
#     subframe.grid_propagate(0)
    return subframe


def make_labeled_Entry(frame, text):
    subframe = ttk.Frame(frame, padding=10)
    label = ttk.Label(subframe, text=text)
    entry = ttk.Entry(subframe)
    label.grid(row=1)
    entry.grid(row=2)
    return subframe, entry


def make_button(frame, text, function, row, column):
    button = ttk.Button(frame, text=text)
    button['command'] = function
    button.grid(row=row, column=column)
    return button


# ----------------------------------------------------------------------
# The subframes to display:
#   connection_gui [to connect to the robot]
#   blink_tone_gui [to blink the LED or play tones]
#   movement_gui   [to go forward, backward, left, right]
#   sensor_gui     [to display sensor readings]
#   pixy_gui       [to display camera readings]
# ----------------------------------------------------------------------
def connection_gui(frame, robot, default_port):
    subframe = make_subframe(frame, '\nConnect/Disconnect:\n')
    subframe.grid(sticky='w')
    port_frame, port_entry = make_labeled_Entry(subframe,
                                                'Port or robot number:')
    port_entry.insert(0, default_port)
    port_frame.grid(row=1, column=1)

    wired_or_wireless_frame = ttk.Frame(subframe, padding=10)
    wired_or_wireless_frame.grid(row=1, column=2)

    wired_or_wireless = tkinter.StringVar(value=ConnectionType.wired)
    wired_or_wireless.set(ConnectionType.wireless)

    wired_radio_btn = ttk.Radiobutton(wired_or_wireless_frame,
                                      text='wired',
                                      variable=wired_or_wireless,
                                      value=ConnectionType.wired)

    wireless_radio_btn = ttk.Radiobutton(wired_or_wireless_frame,
                                         text='wireless',
                                         variable=wired_or_wireless,
                                         value=ConnectionType.wireless)
    wireless_radio_btn.grid(row=1, sticky='w')
    wired_radio_btn.grid(row=2, sticky='w')

    button_frame = ttk.Frame(subframe, padding=10)
    button_frame.grid(row=1, column=3)
    make_button(button_frame, 'Connect',
                lambda: connect(robot, port_entry, wired_or_wireless),
                1, 1)

    make_button(button_frame, 'Disconnect',
                lambda: disconnect(robot),
                2, 1)


def blink_tone_gui(frame, robot):
    subframe = make_subframe(frame, 'Test Blink and Tone:')
    subframe.grid(sticky='w')
    make_button(subframe, 'Blink', lambda: blink(robot), 1, 2)

    make_button(subframe, 'Play tones',
                lambda: play_tones(robot), 1, 3)


def movement_gui(frame, robot):
    subframe = make_subframe(frame, 'Test Movement')
    subframe.grid(sticky='w')

    make_movement_buttons(subframe, robot, 1)


def make_movement_buttons(frame, robot, row):
    make_button(frame, 'Go forward', lambda: move(robot, 100, 100, 2),
                row=row, column=1)
    make_button(frame, 'Go backward', lambda: move(robot, -100, -100, 2),
                row=row, column=2)
    make_button(frame, 'Spin left', lambda: move(robot, -100, 100, 2),
                row=row, column=3)
    make_button(frame, 'Spin right', lambda: move(robot, 100, -100, 2),
                row=row, column=4)


def sensor_gui(frame, robot):
    subframe = make_subframe(frame, ('Test Sensors\n'
                                     + '(prints on Console)\n'))
    subframe.grid(sticky='w')

    make_sensor_buttons(subframe, robot, 1)


def make_sensor_buttons(frame, robot, row):
    make_button(frame, 'Bump sensors',
                (lambda:
                 sense([robot.sensor_reader.left_bump_sensor,
                        robot.sensor_reader.right_bump_sensor])),
                row=row, column=1)
    make_button(frame, 'Button sensor',
                (lambda:
                 sense([robot.sensor_reader.button_sensor])),
                row=row, column=2)
    row = row + 1
    make_button(frame, 'Reflectance sensors',
                (lambda:
                 sense([robot.sensor_reader.left_reflectance_sensor,
                        robot.sensor_reader.middle_reflectance_sensor,
                        robot.sensor_reader.right_reflectance_sensor])),
                row=row, column=1)
    make_button(frame, 'Proximity sensors',
                (lambda:
                 sense([robot.sensor_reader.left_proximity_sensor,
                        robot.sensor_reader.front_proximity_sensor,
                        robot.sensor_reader.right_proximity_sensor])),
                row=row, column=2)

    row = row + 1
    make_button(frame, 'Encoders',
                (lambda:
                 get_encoders(robot)),
                row=row, column=1)
    make_button(frame, 'Reset encoders',
                (lambda:
                 reset_encoders(robot)),
                row=row, column=2)


def pixy_gui(frame, robot):
    subframe = make_subframe(frame,
                             'Test Pixy Camera\n(prints on Console)')
    subframe.grid(sticky='w')

    make_button(subframe, 'Take picture, show values',
                lambda: take_picture_show_values(robot),
                row=1, column=1)

    make_button(subframe, 'Take pictures repeatedly until the left bumper is pressed',
                lambda: take_pictures(robot),
                row=2, column=1)


# ----------------------------------------------------------------------
# Robot ACTIONS: CONNECT / DISCONNECT.
# ----------------------------------------------------------------------
def connect(robot, port_or_robot_number_entry_box, wired_or_wireless):
    if str(wired_or_wireless.get()) == str(ConnectionType.wired):
        connect_wired(robot, port_or_robot_number_entry_box)
    else:
        connect_wireless(robot, port_or_robot_number_entry_box)


def disconnect(robot):
    robot.connector.disconnect()


def connect_wired(robot, port_entry):
    port = port_entry.get()
    if port == '':
        print('You must enter a PORT in the Entry box.')
        return
    robot.connector.connect_wired(port)


def connect_wireless(robot, robot_number_entry):
    address = robot_number_entry.get()
    if address == '':
        print('You must enter a rXX in the Entry box.')
        return
    robot.connector.connect_wireless(address)


# ----------------------------------------------------------------------
# Robot ACTIONS: BLINK the LED / play TONES.
# ----------------------------------------------------------------------
def blink(robot):
    print()
    print('Testing LED blink.  It should blink 4 times.')
    print('Test will start in 1 second:')
    time.sleep(1)
    for _ in range(4):
        time.sleep(0.25)
        robot.led.turn_off()
        time.sleep(0.25)
        robot.led.turn_on()


def play_tones(robot):
    print()
    print('Playing tones.')
    for k in range(1, 102, 10):
        frequency = 440 * pow(1.059463094359, (k - 40))
        print('Tone: {}.  Frequency: {:0.0f}.'.format(k, frequency))
        robot.buzzer.play_tone(k)
        time.sleep(0.1)
        robot.buzzer.stop()
        time.sleep(0.1)
    robot.buzzer.stop()


# ----------------------------------------------------------------------
# Robot ACTIONS: MOVE forward / backward / left / right.
# ----------------------------------------------------------------------
def move(robot, left_speed, right_speed, seconds):
    fstring1 = 'Testing movement at left/right speeds of {} and {}'
    fstring2 = 'Will run for {} seconds'
    print()
    print(fstring1.format(left_speed, right_speed))
    print(fstring2.format(seconds))

    robot.motor_controller.drive_pwm(left_speed, right_speed)
    time.sleep(seconds)
    robot.motor_controller.stop()


# ----------------------------------------------------------------------
# Robot ACTIONS: Get and print SENSOR readings.
# ----------------------------------------------------------------------
def sense(sensors):
    for sensor in sensors:
        print('{:5}'.format(sensor.read()), end='')
    print()


def reset_encoders(robot):
    robot.sensor_reader.left_encoder.reset()
    robot.sensor_reader.right_encoder.reset()


# ----------------------------------------------------------------------
# Robot ACTIONS: Get and print CAMERA readings.
# ----------------------------------------------------------------------
def take_picture_show_values(robot):
    block = robot.camera.get_block(1)
    print(block)
    if block:
        print(block.x, block.y, block.width, block.height)


def take_pictures(robot):
    # Warm up the camera:
    for _ in range(5):
        robot.camera.get_block(1)
        time.sleep(0.2)

    # Take pictures until the user presses the left bumper:
    while True:
        if robot.sensor_reader.left_bump_sensor.read() == 0:
            break
        take_picture_show_values(robot)


def get_encoders(robot):
    left = robot.sensor_reader.left_encoder.read()
    right = robot.sensor_reader.right_encoder.read()
    print('{:6}  {:6}'.format(left, right))


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
