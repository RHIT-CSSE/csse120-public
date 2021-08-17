"""
A simple way for computers to send/receive messages to/from each other.

It is built on top of a protocol called MQTT (see mqtt.org) and a Python
implementation of MQTT called paho-mqtt (see pypi.org/project/paho-mqtt).

*** See the accompanying video for how to use this module. ***

Authors: David Mutchler, Dave Fisher, Sana Ebrahimi, Mohammad Noureddine
         and their colleagues at Rose-Hulman Institute of Technology.
Licensed under CC BY-NC-SA 4.0.  To view a copy of this license, visit
  https://creativecommons.org/licenses/by-nc-sa/4.0.
"""

import inspect
import sys
import time
import traceback

import paho.mqtt.client as paho_mqtt


def activate(unique_id, sender, receiver=None, broker=None):
    """
    Constructs a TalkerToBroker and gives it to the given Sender and Receiver.

    Constructing a TalkerToBroker connects to the given (or default) Broker
    and establishes communication with the other computers through that Broker.

    The  unique_id  distinguishes YOUR simpleMQTT-enabled program from other
    simpleMQTT-enabled programs that may be running at the same time and with
    the same Broker as yours.  Choose a string that is unique to you,
    e.g. something involving your name and/or your program's name.

    Type hints:
      :type unique_id: str
      :type sender:    mq.Sender
      :type receiver:  mq.Receiver
      :type broker:    mq.Broker
    """
    talker_to_broker = TalkerToBroker(sender, receiver, unique_id, broker)
    sender._talker_to_broker = talker_to_broker
    receiver._talker_to_broker = talker_to_broker


class Receiver:
    """
    A Receiver receives messages from a Broker and calls
    its   controller   object to act on the message.
    """

    def __init__(self, controller, verbosity=3):
        """
        A Receiver receives messages from a Broker and calls its   controller
        object to act on the message.  See the  message_received  method below.

        Parameters:
          -- controller: an instance of a class that MUST have the following
                         method definition, spelled exactly like this:
                             def act_on_message_received(message, sender_id):
                                 ...
          -- verbosity: indicates whether to PRINT messages when received;
                        see the  print_message  method below for details.
        Type hints:
          :type controller: Any
          :type verbosity:  int
        """
        self.controller = controller
        self.verbosity = verbosity
        self.verify_controller()

        self._talker_to_broker = None  # Set by the  activate   function

    def message_received(self, message, sender_id):
        """
        Called when this Receiver receives a message from another computer.

        Parameters:
          -- message: The string that another computer sent to this one.
          -- sender_id:  The positive integer (1, 2, ...) that identifies
                         the computer that sent the message.
        Side effects:
          Prints the message (for debugging purposes) and then calls the
          act_on_message_received   method on this Receiver's controller object,
          sending the message and sender_id to that method as arguments.
        Type hints:
          :type message:   str
          :type sender_id: int
        """
        self.print_message(message, sender_id)
        self.controller.act_on_message_received(message, sender_id)

    def print_message(self, message, sender_id):
        """
        Parameters:
          -- message: The string that another computer sent to this one.
          -- sender_id:  The positive integer (1, 2, ...) that identifies
                         the computer that sent the message.
        Side effects:
          Prints the message (for debugging purposes).  Printing is controlled
          by the   verbosity  instance variable, where if verbosity is:
              0:  Do not print messages.
              1:  Print only the message.
              2:  Print the sender's ID and the message.
              3:  Print the sender's and recipient's IDs and the message.
          and bigger numbers print the same as the latter but more verbosely.
        Type hints:
          :type message:   str
          :type sender_id: int
        """
        self._talker_to_broker.print_message(message, self, sender_id)

    def verify_controller(self):
        """ Prints an error message if the  controller  argument is invalid. """
        try:
            method = getattr(self.controller, "act_on_message_received")
            assert callable(method)
            sig = inspect.signature(method)
            assert len(sig.parameters) == 2
        except (AttributeError, AssertionError):
            print_in_red("You constructed a Receiver using code like this:")
            print_colored("   receiver = Receiver(BLAH)", color="blue")
            print_in_red("This simpleMQTT module requires that when you do so,")
            print_in_red("the BLAH argument MUST be an instance of a class")
            print_in_red("that MUST have a method EXACTLY like this:")
            print_colored("  def act_on_message_received(message, sender_id):",
                          color="blue")
            print_in_red("Your BLAH object does NOT meet that requirement.")
            print_in_red("Check that you spelled the method correctly, etc.")
            raise


class Sender:
    """
    A Sender sends messages to a Broker who forwards the messages
    to other computers participating in this communication.
    """

    def __init__(self, who_am_i, number_of_computers=2, verbosity=3):
        """
        A Sender sends messages to a Broker who forwards the messages
        to other computers participating in this communication.

        Parameters:
          -- who_am_i:  a positive integer that identifies this Sender.
          -- number_of_computers:  how many computers are communicating.
          -- verbosity: indicates whether to PRINT messages when they are
               received; see the  print_message  method below for details.
        Type hints:
          :type who_am_i:            int
          :type number_of_computers: int
          :type verbosity:           int
        """
        self.who_am_i = who_am_i
        self.number_of_computers = number_of_computers
        self.verbosity = verbosity

        self._talker_to_broker = None  # Set by the  activate   function

    def send_message(self, message):
        """
        Parameters:
          -- message: The string to send to the other computers.
        Side effects:
          Prints the message (for debugging purposes) and then sends the
          given message to all computers participating in this communication.
        Type hints:
          :type message: str
        """
        if self._talker_to_broker:
            self.print_message(message)
            self._talker_to_broker.send_message(message)
        else:
            print()
            print_in_red("It appears that this Sender has NOT been activated.")
            print_in_red("No message will be sent.")

    def print_message(self, message):
        """
        Parameters:
          -- message: The string to send to the other computers.
        Side effects:
          Prints the message (for debugging purposes).  Printing is controlled
          by the   verbosity  instance variable, where if verbosity is:
              0:  Do not print messages.
              1:  Print only the message.
              2:  Print the sender's ID and the message.
          and bigger numbers print the same as the latter but more verbosely.
        Type hints:
          :type message:   str
        """
        self._talker_to_broker.print_message(message, self)


class Broker:
    """ A Broker accepts and forwards messages, per the MQTT protocol. """

    def __init__(self, hostname="broker.hivemq.com", tcp_port=1883,
                 web_socket_port=8000):
        """ A Broker accepts and forwards messages, per the MQTT protocol. """
        self.hostname = hostname
        self.tcp_port = tcp_port
        self.web_socket_port = web_socket_port

    def __repr__(self):
        return "Hostname {} at ports {} and {}".format(
            self.hostname, self.tcp_port, self.web_socket_port)


class TalkerToBroker:
    """ A TalkerToBroker connects to a Broker and sets up communication. """

    def __init__(self, sender, receiver, unique_id, broker=None):
        """
        A TalkerToBroker connects to the given (or default) Broker
        and sets up communication so that:
          -- The given Sender can send messages that will go to all the
               computers participating in this communication.
          -- The given Receiver will receive messages sent by any Sender
               participating in this communication.

        The  unique_id  distinguishes this simpleMQTT-enabled run from unrelated
        other simpleMQTT-enabled runs that may be running at the same time.

        Type hints:
          :type sender:    Sender
          :type receiver:  Receiver
          :type unique_id: str
          :type broker:    Broker
        """
        self.sender = sender
        self.receiver = receiver
        self.unique_id = unique_id
        self.broker = broker or Broker()  # Use default Broker if broker is None

        # The   publisher_topic   identifies this use of simpleMQTT and this
        # computer.  The Sender uses that Topic for all messages that it sends.
        prefix = unique_id + "/computer"
        self.publisher_topic = "{}-{}".format(prefix, self.sender.who_am_i)

        # The  subscriber_topics  is a list containing the publisher_topics
        # for all the computers participating in this communication.
        self.subscriber_topics = []
        for k in range(1, self.sender.number_of_computers + 1):
            if k != self.sender.who_am_i:
                self.subscriber_topics.append("{}-{}".format(prefix, k))

        # Construct the mqtt_client that does all the heavy lifting.
        # Establish its callbacks.
        self.has_two_way_connection_with_broker = False
        self.mqtt_client = paho_mqtt.Client()
        self.mqtt_client.on_connect = self._on_connect
        self.mqtt_client.on_message = self._on_message
        self.mqtt_client._on_subscribe = self._on_subscribe

        # Initiate the connection process. Wait until it is done or times out.
        self._try_to_connect()
        self._wait_for_two_way_connection_with_broker()

    def send_message(self, message):
        """
        Send the given message (which MUST be a string) to the Broker.
          :type message str
        """
        if not isinstance(message, str):
            print_in_red("You tried to send a message that is NOT a string.")
            print_in_red("All messages MUST be strings.")
        self.mqtt_client.publish(self.publisher_topic, message)

    def _try_to_connect(self):
        """
        Initiate the process of connecting to the Broker.
        Enter the loop that runs in the background, waiting for messages.
        The   on_connect   callback will run when a connection is established.
        """
        print_in_blue("I am trying to connect to the following MQTT broker:")
        print_in_blue("  --", self.broker, "...")

        self.mqtt_client.connect(self.broker.hostname, self.broker.tcp_port,
                                 self.broker.web_socket_port)
        self.mqtt_client.loop_start()

    def _wait_for_two_way_connection_with_broker(self):
        """ Wait until connections are complete or time out. """
        while True:
            if self.has_two_way_connection_with_broker:
                break
            time.sleep(0.01)

    # noinspection PyUnusedLocal
    def _on_connect(self, client, userdata, flags, rc):
        """
        Called when a connection with the Broker is established.
        Send a message to the Broker, asking to subscribe to all the topics.
        The  _on_subscribe  callback will run when the Broker acknowledges.
        """
        if rc == 0:
            print_in_blue("OK, connected!")
        else:
            print_in_red("Error connecting! Return code was:", rc)
            print_in_red("Exiting the program!")
            exit()

        print_in_blue("I am now publishing to topic:", self.publisher_topic)

        topic_tuples = []
        for topic in self.subscriber_topics:
            topic_tuples.append((topic, 0))  # qos will be 0 for all topics
        self.mqtt_client.subscribe(topic_tuples)

    # noinspection PyUnusedLocal
    def _on_subscribe(self, client, userdata, mid, granted_qos):
        if len(self.subscriber_topics) == 1:
            print_in_blue("I am now subscribed to topic:",
                          self.subscriber_topics[0])
        else:
            print_in_blue("I am now subscribed to topics:",
                          self.subscriber_topics)

        self.has_two_way_connection_with_broker = True

    # noinspection PyUnusedLocal
    def _on_message(self, client, userdata, msg):
        """
        :type msg: mq.MQTTMessage
        """
        message = msg.payload.decode()
        sender_id = int(msg.topic.split("-")[-1])

        # The following is a fix for paho_mqtt version 1.5.0, which SILENCES
        # exceptions raised in callbacks.  paho_mqtt version 1.5.1 fixes this.
        # CONSIDER: What SHOULD happen when an exception occurs in response
        # to the user program acting on a message?  Just print? Stop the
        # program? Print/pause?  Have flags to allow different responses????
        # noinspection PyBroadException
        try:
            self.receiver.message_received(message, sender_id)
        except Exception:
            traceback.print_exc()

    def print_message(self, message, sender_or_receiver, sender_id=None):
        """
        Print the message, at the sender_or_receiver's verbosity level of:
            0:  Do not print messages.
            1:  Print only the message.
            2:  Print the sender's ID and the message.
            3:  Print the sender's and recipient's IDs and the message.
          and bigger numbers print as above but more verbosely.
         """
        who_am_i = self.sender.who_am_i
        verbosity = sender_or_receiver.verbosity

        # If the sender_id is None, then this is a Sender printing.
        # Otherwise, this is a Receiver printing and sender_id is who sent the
        # message (as determined by the Topic).
        sender_number = sender_id or who_am_i

        if verbosity == 0:
            return
        elif verbosity == 2:
            if sender_id:
                print("Received from {}: ".format(sender_number), end="")
            else:
                print("Sent by {}: ".format(who_am_i), end="")
        elif verbosity == 3:
            if sender_id:
                print("Received by {} from {}: ".format(who_am_i,
                                                        sender_number), end="")
            else:
                print("Sent by {} to all: ".format(who_am_i), end="")
        elif verbosity >= 4:
            if sender_id:
                print("Received by {} from {}:".format(who_am_i, sender_number))
            else:
                print("Sent by {} to all:".format(who_am_i))
            print("  -- ", end="")

        print_in_blue(message)


# noinspection PyUnusedLocal
def print_colored(*args, color="black", flush=True, **kwargs):
    color_codes = {"black": 20,
                   "red": 31,
                   "green": 32,
                   "yellow": 33,
                   "blue": 34,
                   "magenta": 35,
                   "cyan": 36,
                   "white": 37
                   }
    text = ""
    for arg in args:
        text = text + " " + str(arg)
    text = text.replace(" ", "", 1)
    sys.stdout.write('\033[%sm%s\033[0m' % (color_codes[color], text))
    print(**kwargs)


def print_in_red(*args, **kwargs):
    print_colored(*args, color="red", **kwargs)


def print_in_blue(*args, **kwargs):
    print_colored(*args, color="blue", **kwargs)
