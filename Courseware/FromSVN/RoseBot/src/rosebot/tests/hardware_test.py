import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import time
from enum import Enum, unique
import random


@unique
class ConnectionType(Enum):
    wired = 1
    wireless = 2

#     port = '/dev/cu.usbserial-AL00EWSO'
#     port = '/dev/cu.usbserial-A012KMUK'
#     port = '/dev/cu.usbserial-A9048HVI'
#     port = '/dev/cu.usbserial-A9048HVD'  # R12
#     port = '/dev/cu.usbserial-A9048HV2'  # R15
#     port = '/dev/cu.usbserial-A9048HV7'  # R25
#     port = '/dev/cu.usbserial-A9048HUT'  # R01

PORT = '/dev/cu.usbserial-A9048HUT'  # R07


class ByteObject(object):
    value = 0


def main():
    root = tkinter.Tk()
    robot = rb.RoseBot()

    frame = ttk.Frame(root, padding=10)
    frame.grid()

    connection_gui(frame, robot)
    blink_tone_gui(frame, robot)
    movement_gui(frame, robot)
    sensor_gui(frame, robot)
    pixy_gui(frame, robot)
#     sensor_with_movement_gui(
#         make_subframe(frame, 'For testing sensors with movment'), robot)
#     communication_gui(frame, robot)
    root.mainloop()


def make_subframe(frame, frame_text):
    return ttk.LabelFrame(frame, padding=5, text=frame_text)


def make_labeled_Entry(frame, text):
    subframe = ttk.Frame(frame, padding=10)
    label = ttk.Label(subframe, text=text)
    entry = ttk.Entry(subframe)
    label.grid(row=1)
    entry.grid(row=2)
    return subframe, entry


def connection_gui(frame, robot):
    subframe = make_subframe(frame, 'Connecting to Robot')
    subframe.grid()
    port_frame, port_entry = make_labeled_Entry(subframe,
                                                'Port or robot number:')
    port_entry.insert(0, PORT)
    port_frame.grid(row=1, column=1)

    wired_or_wireless_frame = ttk.Frame(subframe, padding=10)
    wired_or_wireless_frame.grid(row=1, column=2)

    wired_or_wireless = tkinter.StringVar(value=ConnectionType.wired)
    wired_radio_btn = ttk.Radiobutton(wired_or_wireless_frame,
                                      text='wired',
                                      variable=wired_or_wireless,
                                      value=ConnectionType.wired)

    wireless_radio_btn = ttk.Radiobutton(wired_or_wireless_frame,
                                         text='wireless',
                                         variable=wired_or_wireless,
                                         value=ConnectionType.wireless)
    wired_radio_btn.grid(row=1, sticky='w')
    wireless_radio_btn.grid(row=2, sticky='w')

    button_frame = ttk.Frame(subframe, padding=10)
    button_frame.grid(row=1, column=3)
    make_button(button_frame, 'Connect',
                lambda: connect(robot, port_entry, wired_or_wireless),
                1, 1)

    make_button(button_frame, 'Disconnect',
                lambda: disconnect(robot),
                2, 1)
#     make_button(subframe, 'Blink', lambda: blink(robot), 1, 4)


def blink_tone_gui(frame, robot):
    subframe = make_subframe(frame, 'Test Blink and Tone')
    subframe.grid()
    make_button(subframe, 'Blink', lambda: blink(robot), 1, 1)

    make_button(subframe, 'Play tones',
                lambda: play_tones(robot), 1, 2)


def movement_gui(frame, robot):
    subframe = make_subframe(frame, 'Test Robot Movement')
    subframe.grid()

    make_movement_buttons(subframe, robot, 1)


def sensor_gui(frame, robot):
    subframe = make_subframe(frame, 'Test Robot Sensors')
    subframe.grid()

    make_sensor_buttons(subframe, robot, 1)


def pixy_gui(frame, robot):
    subframe = make_subframe(frame, 'Test Pixy Camera')
    subframe.grid()

    results_frame = ttk.Frame(subframe, padding=10)
    ttk.Label(results_frame, text='x').grid(row=1, column=1)
    ttk.Label(results_frame, text='y').grid(row=1, column=2)
    ttk.Label(results_frame, text='width').grid(row=1, column=3)
    ttk.Label(results_frame, text='height').grid(row=1, column=4)

    x_result = ttk.Label(results_frame, text='')
    y_result = ttk.Label(results_frame, text='')
    width_result = ttk.Label(results_frame, text='')
    height_result = ttk.Label(results_frame, text='')
    x_result.grid(row=2, column=1)
    y_result.grid(row=2, column=2)
    width_result.grid(row=2, column=3)
    height_result.grid(row=2, column=4)
    result_labels = [x_result, y_result, width_result, height_result]

    make_button(subframe, 'Take picture, show values',
                lambda: take_picture_show_values(robot, result_labels),
                row=1, column=1)
    results_frame.grid(row=1, column=2)

    make_button(subframe, 'Track', lambda: track_with_camera(robot),
                1, 3)

# def sensor_with_movement_gui(frame, robot):
#     frame.grid()


def make_button(frame, text, function, row, column):
    button = ttk.Button(frame, text=text)
    button['command'] = function
    button.grid(row=row, column=column)
    return button


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
        port = '/dev/cu.usbserial-A9048GN8'
    robot.connector.connect_wired(port)


def connect_wireless(robot, robot_number_entry):
    address = robot_number_entry.get()
    if address == '':
        address = 7
    robot.connector.connect_wireless(address)


def track_with_camera(robot):
    # Warm up the camera:
    for _ in range(10):
        robot.camera.get_block()
        time.sleep(0.2)

    # Track:
    while True:
        if robot.sensor_reader.left_bump_sensor.read() == 0:
            break
        block = robot.camera.get_block()
        if block is None:
            robot.motor_controller.stop()
        else:
            if block.x < 150:
                robot.motor_controller.drive_pwm(-40, 40)
            elif block.x > 170:
                robot.motor_controller.drive_pwm(40, -40)
            else:
                robot.motor_controller.stop()

    robot.motor_controller.stop()
#
#
#
#     return connection_frame
#
# def make_communication_frame(frame, robot):
#     communication_frame = ttk.LabelFrame(frame, padding=10,
#                                          text='Testing Communication')
#     make_button(communication_frame, 'Test the Startup Sequence',
#                 lambda: test_startup_sequence(robot),
#                 1, 1)
#     byte_object = ByteObject()
#     make_button(communication_frame, 'Echo', lambda: echo(robot, byte_object),
#                 1, 2)
#
#     return communication_frame
# #     make_button(frame, 'Connect wireless',
# #                 lambda: connect_wireless(robot, port_entry),
# #                 row, column + 3)
#
# def make_command_frame(frame, robot):
#     command_frame = ttk.LabelFrame(frame, padding=10,
#                                    text='Robot Commands')
#
#     make_movement_buttons(command_frame, robot, 1)
#
#     make_sensor_buttons(command_frame, robot, 2)
#
#     make_button(command_frame, 'Blink', lambda: blink(robot), 3, 1)
#
#     make_button(command_frame, 'Play tones',
#                 lambda: play_tones(robot), 3, 2)
#
#     return command_frame


def test_startup_sequence(robot):
    communicator = robot.connector._communicator

    fstring = 'Sent: {:3}. Received: {:3}.'
    for _ in range(10):
        random_byte = random.randrange(255)
        communicator.send_bytes(bytearray([random_byte]))
        print(fstring.format(random_byte,
                             communicator.receive_bytes(1)))
    communicator.send_bytes(bytearray([255, 255]))

    print(fstring.format(255,
                         communicator.receive_bytes(1)))
    print(fstring.format(255,
                         communicator.receive_bytes(1)))

    for _ in range(5):
        random_byte = random.randrange(254)
        communicator.send_bytes(bytearray([random_byte]))
        print(fstring.format(random_byte,
                             communicator.receive_bytes(1)))

        communicator.send_bytes(bytearray([255]))
        print(fstring.format(255,
                             communicator.receive_bytes(1)))

    communicator.send_bytes(bytearray([0]))
    print(fstring.format(0,
                         communicator.receive_bytes(1)))

    communicator.send_bytes(bytearray([255]))
    print(fstring.format(255,
                         communicator.receive_bytes(1)))
    communicator.send_bytes(bytearray([255]))
    print(fstring.format(255,
                         communicator.receive_bytes(1)))
    communicator.send_bytes(bytearray([255]))
    print(fstring.format(255,
                         communicator.receive_bytes(1)))

    print('Should be one more than last time this ran:')
    print(communicator.receive_bytes(1))


def echo(robot, byte_object):
    """
      :type robot: rb.RoseBot
      :type byte_object: ByteObject
      """
    bytes_to_send = bytearray([byte_object.value])
    robot.connector._communicator.send_bytes(bytes_to_send)
    print('Echo:', robot.connector._communicator.receive_bytes(1))
    byte_object.value = (byte_object.value + 1) % 255


def move(robot, left_speed, right_speed, seconds):
    fstring1 = 'Testing movement at left/right speeds of {} and {}'
    fstring2 = 'Will run for {} seconds'
    print()
    print(fstring1.format(left_speed, right_speed))
    print(fstring2.format(seconds))

    robot.motor_controller.drive_pwm(left_speed, right_speed)
    time.sleep(seconds)
    robot.motor_controller.stop()


def sense(sensors):
    for sensor in sensors:
        print('{:5}'.format(sensor.read()), end='')
    print()


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


def take_picture_show_values(robot, result_labels):
    block = robot.camera.get_block(1)
    print(block)
    if block:
        print(block.x, block.y, block.width, block.height)
        result_labels[0]['text'] = str(block.x)
        result_labels[1]['text'] = str(block.y)
        result_labels[2]['text'] = str(block.width)
        result_labels[3]['text'] = str(block.height)
    else:
        result_labels[0]['text'] = ''
        result_labels[1]['text'] = ''
        result_labels[2]['text'] = ''
        result_labels[3]['text'] = ''


def make_movement_buttons(frame, robot, row):
    make_button(frame, 'Go forward', lambda: move(robot, 100, 100, 2),
                row=row, column=1)
    make_button(frame, 'Go backward', lambda: move(robot, -100, -100, 2),
                row=row, column=2)
    make_button(frame, 'Spin left', lambda: move(robot, -100, 100, 2),
                row=row, column=3)
    make_button(frame, 'Spin right', lambda: move(robot, 100, -100, 2),
                row=row, column=4)


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
    make_button(frame, 'Reflectance sensors',
                (lambda:
                 sense([robot.sensor_reader.left_reflectance_sensor,
                        robot.sensor_reader.middle_reflectance_sensor,
                        robot.sensor_reader.right_reflectance_sensor])),
                row=row, column=3)
    make_button(frame, 'Proximity sensors',
                (lambda:
                 sense([robot.sensor_reader.left_proximity_sensor,
                        robot.sensor_reader.front_proximity_sensor,
                        robot.sensor_reader.right_proximity_sensor])),
                row=row, column=4)
    row = row + 1
    make_button(frame, 'Latency',
                (lambda:
                 test_latency([
                     robot.sensor_reader.left_proximity_sensor])),
                row=row, column=1)
    row = row + 1
    make_button(frame, 'Encoders',
                (lambda:
                 get_encoders(robot)),
                row=row, column=1)
    make_button(frame, 'Reset left',
                (lambda:
                 robot.sensor_reader.left_encoder.reset()),
                row=row, column=2)
    make_button(frame, 'Reset right',
                (lambda:
                 robot.sensor_reader.right_encoder.reset()),
                row=row, column=3)


def get_encoders(robot):
    left = robot.sensor_reader.left_encoder.read()
    right = robot.sensor_reader.right_encoder.read()
    print('{:6}  {:6}'.format(left, right))


def test_latency(sensors):
    for k in range(50):
        sense(sensors)
        for sensor in sensors:
            print('{:5.2f}'.format(sensor.cached_latency), end='')
        print()
        time.sleep(0.005)


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
