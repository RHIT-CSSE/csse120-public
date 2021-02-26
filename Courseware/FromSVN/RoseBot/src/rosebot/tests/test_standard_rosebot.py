# TODO Put comments in this file.

# import rosebot.faux_rosebot as rb
import rosebot.standard_rosebot as rb
import rosebot.command
import unittest
import time


class TestStandardRosebot(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(self):
        self.port = '/dev/cu.usbserial-AL00EWSO'  # R08
        self.port = '/dev/cu.usbserial-A9048HUT'
        self.port = '/dev/cu.usbserial-AI02KMUK'  # R01
        self.port = '/dev/cu.usbserial-AL00F14M'  # R32?
        self.port = '/dev/cu.usbserial-A9048HVD'  # R12
        self.port = '/dev/cu.usbserial-AL00EWSL'  # R02
        self.port = '/dev/cu.usbserial-A9048HV2'  # R15 or R32
        self.port = '/dev/cu.usbserial-A9048HV2'  # R32 or R15
        self.port = '/dev/cu.usbserial-AL00EXQL'  # R07
        self.port = '/dev/cu.usbserial-A9048HV2'  # no wifly

        self.port = '/dev/cu.usbserial-A9048HVD'  # R12
        self.port = '/dev/cu.usbserial-A9048HV7'  # R25
        self.port = 'r22'
        self.port = '/dev/cu.usbserial-A9048GN8'  # R25
#         self.port = 'r07'

        self.robot = rb.RoseBot()
        self.robot.connector.connect_wired(self.port)


#     def testRoseBotConstruction(self):
#         rb.RoseBot()

#     def testRoseBotConnect(self):
#         robot = rb.RoseBot()
#         robot.connector.connect(port)

#     def testWireless(self):
#         print('Connected wireless!')

#     # TODO test for what SHOULD happen when connect has no arguments
#     def testRoseBotConnect_2(self):
#         robot = rb.RoseBot()
#         robot.connector.connect()

#     def testLEDCommand(self):
#         command = rosebot.command.LEDCommand()
#         num = command.command_number
#         pin = command.pin_number
#         expected_command_number = (rosebot.command.COMMAND_NUMBER.
#                                    digital_write)
#         expected_pin_number = (rosebot.command.PIN_MAPPING
#                                [rosebot.command.PIN.LED])
#         self.assertEqual(expected_command_number, num)
#         self.assertEqual(expected_pin_number, pin)


#     def testLED_off(self):
#         robot = rb.RoseBot()
#         robot.connector.connect(port)
#         time.sleep(3)
#         robot.led.turn_off()

    def testLED_blink(self):
        print('Testing LED blink.  It should blink 4 times.')
        time.sleep(2)
        for _ in range(8):
            time.sleep(0.5)
            self.robot.led.turn_off()
            time.sleep(0.5)
            self.robot.led.turn_on()

        self.robot.disconnect()
#
#     def testButton(self):
#         print('Testing the Button. 8 reads, 0.5 seconds after each.')
#         time.sleep(2)
#         for _ in range(8):
#             print(self.robot.sensor_reader.button_sensor.read())
#             time.sleep(1.5)
#
#     def testBumpSensors(self):
#         print('Testing the Bump Sensors.')
#         print('Right Bump Sensor, then Left.')
#         print('  8 reads for each sensor, 0.5 seconds after each.')
#         print('2 seconds when switching from Right to Left')
#         print('First the Right Bump Sensor:')
#         time.sleep(2)
#         for _ in range(8):
#             print(self.robot.sensor_reader.right_bump_sensor.read())
#             time.sleep(0.5)
#         print('Now the Left Bump Sensor:')
#         time.sleep(2)
#         for _ in range(8):
#             print(self.robot.sensor_reader.left_bump_sensor.read())
#             time.sleep(0.5)
#
#     def testProximitySensors(self):
#         print('Testing the Proximity Sensors.')
#         print('Left, then Front, then Right, immediately after each other.')
#         print('10 reads, with 2 seconds between each.')
#         time.sleep(2)
#         for _ in range(10):
#             print(self.robot.sensor_reader.left_proximity_sensor.read(),
#                   self.robot.sensor_reader.front_proximity_sensor.read(),
#                   self.robot.sensor_reader.right_proximity_sensor.read())
#             time.sleep(2)

#     def testProximitySensors2(self):
#         print('Testing the Proximity Sensors.')
#         print('Right, then Left, then Front.')
#         print('  4 reads for each sensor, 2 seconds after each.')
#         print('2 seconds when switching from one sensor to another.')
#         print('First the Right Proximity Sensor:')
#         time.sleep(2)
#         for _ in range(100):
#             print(self.robot.sensor_reader.right_proximity_sensor.read())
#             time.sleep(2)
#         print('Now the Left Proximity Sensor:')
#         time.sleep(2)
#         for _ in range(4):
#             print(self.robot.sensor_reader.left_proximity_sensor.read())
#             time.sleep(2)
#         print('Now the Front Proximity Sensor:')
#         time.sleep(2)
#         for _ in range(4):
#             print(self.robot.sensor_reader.front_proximity_sensor.read())
#             time.sleep(2)

#     def testReflectanceSensors(self):
#         print('Testing the Reflectance Sensors.')
#         print('All 3, immediately after each other.')
#         print('10 reads, with 2 seconds between each.')
#         time.sleep(2)
#         for _ in range(10):
#             print(self.robot.sensor_reader.right_reflectance_sensor.read(),
#                   self.robot.sensor_reader.middle_reflectance_sensor.read(),
#                   self.robot.sensor_reader.left_reflectance_sensor.read())
#             time.sleep(2)
#
#     def testBuzzer(self):
#         for k in range(1, 255, 20):
#             fstring = '{:6} {:12}'
#             print(fstring.format(round(440 * pow(1.059463094359, k - 40)),
#                                  round(5000 * k / 255)))
#             self.robot.buzzer.play_tone(k)
#             time.sleep(0.25)
#             self.robot.buzzer.stop()
#             time.sleep(0.25)
#         self.robot.buzzer.stop()
#
#     def testLeftMotor(self):
#         print("Turning on the left motor slowly forward in 2 seconds:")
#         time.sleep(2)
#         self.robot.motor_controller.left_wheel_pwm(50)
#         time.sleep(2)
#         self.robot.motor_controller.stop()
#         print("Turning on the left motor fast backward in 2 seconds:")
#         time.sleep(2)
#         self.robot.motor_controller.left_wheel_pwm(-255)
#         time.sleep(2)
#         self.robot.motor_controller.stop()
#
#     def testRightMotor(self):
#         print("Turning on the right motor slowly forward in 2 seconds:")
#         time.sleep(2)
#         self.robot.motor_controller.right_wheel_pwm(50)
#         time.sleep(2)
#         self.robot.motor_controller.stop()
#         print("Turning on the right motor fast backward in 2 seconds:")
#         time.sleep(2)
#         self.robot.motor_controller.right_wheel_pwm(-255)
#         time.sleep(2)
#
#     def testForward(self):
#         print("Turning on both motors slowly forward in 2 seconds:")
#         time.sleep(2)
#         self.robot.motor_controller.drive_pwm(50, 50)
#         time.sleep(2)
#         self.robot.motor_controller.stop()
#         print("Turning on both motors fast backward in 2 seconds:")
#         time.sleep(2)
#         self.robot.motor_controller.drive_pwm(-255, -255)
#         time.sleep(2)
#         self.robot.motor_controller.stop()
#
#     def testBackward(self):
#         print("Turning on the left motor in 2 seconds:")
#         time.sleep(2)
#         self.robot.motor_controller.left_wheel_pwm(50)
#         time.sleep(2)
#         self.robot.motor_controller.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStandardRosebot))
    return suite

if __name__ == "__main__":
    unittest.main()
