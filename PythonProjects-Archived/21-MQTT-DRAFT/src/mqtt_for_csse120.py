import paho.mqtt.client as paho_mqtt
import time


class Broker(object):
    def __init__(self, hostname="broker.hivemq.com", tcp_port=1883,
                 web_socket_port=8000):
        self.hostname = hostname
        self.tcp_port = tcp_port
        self.web_socket_port = web_socket_port

    def __repr__(self):
        return "Hostname {} at ports {} and {}".format(
            self.hostname, self.tcp_port, self.web_socket_port)


class SenderReceiver(object):
    def __init__(self,
                 unique_id, subscriber_topic_suffix, publisher_topic_suffix,
                 receiver, broker=None):
        self.subscription_topic_name = unique_id + "/" + subscriber_topic_suffix
        self.publish_topic_name = unique_id + "/" + publisher_topic_suffix
        self.receiver = receiver
        if not broker:
            broker = Broker()
        self.broker = broker
        self.has_two_way_connection = False

        self.client = paho_mqtt.Client()

        self._try_to_connect()
        self._wait_for_two_way_connection()

    def send_message(self, message):
        """
        Send the given message to the Broker.
          :type message str
        """
        if not isinstance(message, str):
            print("You tried to send a message that is NOT a string.")
            print("All messages MUST be strings.")
            self.close()
        print()
        print("I am sending (i.e. publishing) the following message:")
        print("  --", message)
        self.client.publish(self.publish_topic_name, message)

    def _try_to_connect(self):
        print("I am trying to connect to the following mqtt broker:")
        print("  --", self.broker, "...")
        self.client.on_connect = self._on_connect
        self.client.message_callback_add(self.subscription_topic_name,
                                         self._on_message)
        self.client.connect(self.broker.hostname,
                            self.broker.tcp_port, self.broker.web_socket_port)
        self.client.loop_start()

    def _wait_for_two_way_connection(self):
        while True:
            if self.has_two_way_connection:
                break
            time.sleep(0.1)

    # noinspection PyUnusedLocal
    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("OK, connected!")
        else:
            print("Error connecting! Return code was:", rc)
            print("Exiting the program!")
            exit()

        print("I am now publishing to topic:", self.publish_topic_name)
        self.client.on_subscribe = self._on_subscribe

        self.client.subscribe(self.subscription_topic_name)

    # noinspection PyUnusedLocal
    def _on_subscribe(self, client, userdata, mid, granted_qos):
        print("I am now subscribed to topic:", self.subscription_topic_name)
        self.has_two_way_connection = True

    # noinspection PyUnusedLocal
    def _on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        if not self.receiver:
            print("You MUST have supplied a Receiver")
            print("when you constructed this SenderReceiver.")
            print("You did NOT do so, it seems!")
            print("Exiting the program!")
            exit()
        try:
            self.receiver.message_received(message)
        except TypeError:
            print("Your Receiver MUST have a 'message_received' method")
            print("with one parameter (namely, the message received).")
            print("Your Receiver does NOT have such a method!")
            print("Exiting the program!")
            exit()
