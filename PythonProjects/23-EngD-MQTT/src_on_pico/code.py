# Example showing Pico communicating with another device through MQTT.
# Author:  David Mutchler, Rose-Hulman Institute of Technology.

import time
import random
import board
import busio
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as adafruit_socket
import adafruit_minimqtt.adafruit_minimqtt as adafruit_MQTT

from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi

# Load the WiFi and HiveMQ Cloud credentials from secrets.py
from secrets import secrets

# MQTT Topics to publish/subscribe from/to Pico to/from HiveMQ Cloud
UNIQUE_ID = "DavidMutchler1019"  # Use something that no one else will use
PC_TO_DEVICE_TOPIC = UNIQUE_ID + "/pc_to_device"
DEVICE_TO_PC_TOPIC = UNIQUE_ID + "/device_to_pc"

# Initialize the Pico pins and WiFi module.
esp32_cs = DigitalInOut(board.GP13)
esp32_ready = DigitalInOut(board.GP14)
esp32_reset = DigitalInOut(board.GP15)
spi = busio.SPI(board.GP10, board.GP11, board.GP12)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

# Handle HTTP requests
requests.set_socket(adafruit_socket, esp)

# Check ESP32 status
print("Checking ESP32")
if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("\tESP32 found and in idle mode")
print("\tFirmware version: ", esp.firmware_version)
print("\tMAC address: ", [hex(i) for i in esp.MAC_address])

# List the detected WiFi networks
print("Discovered WiFi networks:")
for ap in esp.scan_networks():
    print("\t", (str(ap["ssid"], "utf-8")), "\t\tRSSI: ", ap["rssi"])

# Connect to the configured WiFi network
print("Connecting to WiFi: ", secrets["ssid"])
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("\tCould not connect to WiFi: ", e)
        continue
print("\tConnected to ", str(esp.ssid, "utf-8"), "\t\tRSSI:", esp.rssi)
print("\tIP address of this board: ", esp.pretty_ip(esp.ip_address))
print("\tPing google.com: " + str(esp.ping("google.com")) + "ms")

# Configure MQTT to use the ESP32 interface
adafruit_MQTT.set_socket(adafruit_socket, esp)

# Configure MQTT client.
mqtt_client = adafruit_MQTT.MQTT(
    broker=secrets["broker"],
    port=secrets["port"],
    username=secrets["mqtt_username"],
    password=secrets["mqtt_key"],
)

# Define callback methods and assign them to the MQTT events
def connected(client, userdata, flags, rc):
    print("\tConnected to MQTT broker: ", client.broker)

def on_message(mqtt_client, userdata, message):
    print("\tReceived a message:", message)

mqtt_client.on_connect = connected
mqtt_client.on_message = on_message

# Connect to the MQTT broker
print("Connecting to MQTT broker...")
try:
    mqtt_client.connect()
    mqtt_client.subscribe(PC_TO_DEVICE_TOPIC)
except Exception as e:
    print("\tMQTT connect failed: ", e)

# Simulate sending sensor data to the Broker by sending random numbers.
counter = 0
while True:
    mqtt_client.loop()  # Poll for about 1 second to see if any messages have arrived

    # Send a message (simulating sending sensor data):
    if counter >= 3:  # Send (publish) every 3 times through this loop
        counter = 0
        simulated_sensor_data = random.randint(1, 100)  # Simulate sensor data
        message_to_send = str(simulated_sensor_data)
        print("Sending (publishing) message:", message_to_send)
        mqtt_client.publish(DEVICE_TO_PC_TOPIC, message_to_send)

    time.sleep(0.1)  # Sleep a bit to safeguard against inundating the message-passing
    counter = counter + 1
