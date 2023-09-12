# Example showing a Pico, running CircuitPython,
# communicating with another device through MQTT.
# Author:  David Mutchler, Rose-Hulman Institute of Technology,
#          based on examples from the internet.

# These imports are for the WIFI and MQTT communication:
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

# These imports are for simulating sending sensor data:
import random
import time

# MQTT Topics to publish/subscribe from/to Pico to/from HiveMQ Cloud
UNIQUE_ID = "DavidMutchler1019"  # Use something that no one else will use
PC_TO_DEVICE_TOPIC = UNIQUE_ID + "/pc_to_device"
DEVICE_TO_PC_TOPIC = UNIQUE_ID + "/device_to_pc"

# Load the WiFi and HiveMQ Cloud credentials from the file: secrets.py
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Connect to the configured WiFi network
print("\n\nAttempting to connect to WiFi: ", secrets["ssid"], "...")
wifi.radio.connect(secrets["ssid"], secrets["password"])

print("\tConnected to %s!\n" % secrets["ssid"])


# Define callback methods and assign them to the MQTT events
def on_message(mqtt_client, userdata, message):
    print("\tReceived a message:", message)


def on_connect(client, userdata, flags, rc):
    print("\tConnected to MQTT broker: ", client.broker, "\n")


def on_disconnect(mqtt_client, userdata, rc):
    print("Disconnected from MQTT Broker!")


def on_subscribe(mqtt_client, userdata, topic, granted_qos):
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))


def on_unsubscribe(mqtt_client, userdata, topic, pid):
    print("Unsubscribed from {0} with PID {1}".format(topic, pid))


def on_publish(mqtt_client, userdata, topic, pid):
    print("Published to {0} with PID {1}".format(topic, pid))


# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=secrets["broker"],
    port=secrets["port"],
    username=secrets["mqtt_username"],
    password=secrets["mqtt_key"],
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Connect callback handlers to mqtt_client
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.on_disconnect = on_disconnect
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_unsubscribe = on_unsubscribe
# mqtt_client.on_publish = on_publish

# Connect to the MQTT broker
print("Attempting to connect to %s ..." % mqtt_client.broker)
try:
    mqtt_client.connect()
    mqtt_client.subscribe(PC_TO_DEVICE_TOPIC)
except Exception as e:
    print("\tMQTT connect failed: ", e)

# Simulate sending sensor data to the Broker by sending random numbers.
counter = 0
loop_counter = 0
while True:
    mqtt_client.loop()  # Poll for about 1 second to see if any messages have arrived

    # Send a message (simulating sending sensor data):
    if counter >= 10:  # Send (publish) every 10 times through this loop
        counter = 0
        simulated_sensor_data = random.randint(1, 100)  # Simulate sensor data
        message_to_send = str(simulated_sensor_data)
        print("Sending (publishing) message:", message_to_send)
        mqtt_client.publish(DEVICE_TO_PC_TOPIC, message_to_send)

    time.sleep(0.1)  # Sleep a bit to safeguard against inundating the message-passing
    counter = counter + 1
    loop_counter = loop_counter + 1
#    if loop_counter > 300:
#        break

print("Unsubscribing from %s" % PC_TO_DEVICE_TOPIC)
mqtt_client.unsubscribe(PC_TO_DEVICE_TOPIC)

print("Disconnecting from %s" % mqtt_client.broker)
mqtt_client.disconnect()