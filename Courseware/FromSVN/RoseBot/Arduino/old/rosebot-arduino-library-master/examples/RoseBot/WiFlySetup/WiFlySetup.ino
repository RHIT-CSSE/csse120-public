/**
 * The purpose of this sketch is to help you connect your WiFly module to your WiFi network from your Sparkfun Redbot board.
 * You will use the RoseBotFirmata for all Python/Scratch programs and you will use this sketch ONLY to get your WiFly setup.
 * This sketch is nice because you don't need any other hardware beyong a WiFly and a RedBot (RoseBot).
 *
 * In order to use this sketch you need to:
 *   - Turn power off on the RedBot and unplug the batteries
 *   - Plug a WiFly module into your RedBot (RoseBot) and flip the switch at the top center of the board to "XBEE SW SERIAL"
 *   - Plug in the USB cable to RedBot and your computer, then turn on the RedBot Power switch
 *   - Make sure you have selected Tools->Board Arduino Uno and you have the Tools->Port set, then upload this sketch to your RedBot
 *   - Open the Serial Monitor (icon in top right that looks like a magnifying glass)
 *   - Set the Serial Monitor to "Carriage Return" and "115200 baud" (keep Autoscroll checked)
 *     - Note, the speed used for the Serial Monitor is not necessarially (and probably isn't) the same speed that WiFly uses (totally ok)
 *   * Follow the prompts to setup your WiFly (make sure to always finish a recipe with a save then a reboot, s then r)
 *     - Depending on your setup, you should probably write down the WiFly's ip address when you do the reboot too!
 *   - After your WiFly is setup, open and upload the Examples -> RoseBot -> RoseBotFirmata sketch onto RedBot board
 *   - Power down, remove the USB cable, flip the switch back to "XBEE HW SERIAL", plug in the batteries, then turn power on.
 *   - You should be able to run Python and Scratch programs to drive the RoseBot again
 *
 * There are many things you can do with this sketch, but here are the common recipes that I predict you'll need.
 *
 * #1.  Set the baudrate to 57600 for a new WiFly
 * When you buy a new WiFly module and plug it in for the very first time the baudrate is 9600.  You need to fix that.
 * The first time you ever connect you will need to connect to WiFly using the 9600 baudrate and send some commands.  Run the steps
 * shown above and for the * step, you'll be running these commands:
 *   set uart baudrate 57600
 *   save
 *   reboot
 * You'll do that using the menu shortcuts:
 * (select option 1 to connect at 9600, then send each command below, one at a time)
 *   b 2
 *   s
 *   r
 * You will only need to do this once ever.  After your WiFly reboots it will be at a different baudrate.  Also after a reboot
 8 your WiFly will no longer be in command mode.  So after this r command, you need to close the Serial Monitor then reopen it.
 * Next time you are asked to connect use the 57600 option.
 *
 *
 * #2.  Get the WiFly onto your WiFi network.
 * Connect at whatever baudrate your WiFly is using from the recipe above (probably 57600 which is choice 2).  Then you'll use
 * these commands:
 *   set wlan join 1
 *   scan
 *   set wlan ssid YOUR$WIFI$NAME$NO$SPACES
 *   set wlan pass ifUneed1
 *   save
 *   reboot
 * You'll do that using the menu shortcuts:
 *   a
 *   1
 *   3 YOUR WIFI NAME NO SPACES
 *   4 ifUneed1
 *   s
 *   r
 * Note, this sketch will convert spaces for parameters in $ for you.  The WiFly doesn't like spaces so you use $ instead, but that
 * is all handled internally by this sketch.  The reboot should show you the IP Address of your WiFly on the network.  Write that down.
 *
 *
 * #3. Getting the IP Address of your WiFly if you forgot it.
 * If you forgot to write down your IP address or if it magically changed on you from a DHCP lease renewal you need to do this:
 *   get ip a
 *   exit
 * You'll do that using the menu shortcuts:
 *   i
 *   x
 * Write it down.  BTW you can try to avoid IP Addresses by setting the WiFly hostname, for example
 *   h r05
 * To name your WiFly, then maybe your WiFi network will use the hostname to give you a NAMED address.  If you try that trick you can
 * figure out if it worked by opening a command window (Terminal) and typing nslookup 127.0.0.1 (put in your WiFly ip address, 127.0.0.1 is just an example)
 * Note there is also a Static IP command, but I much prefer the hostname trick if you can get that to work.
 *
 * Note, there are many additional commands that you can learn about from the WiFly user's guide:
 * http://cdn.sparkfun.com/datasheets/Wireless/WiFi/rn-wiflycr-ug-v1.2r.pdf
 * Learn about commands you need to drop into manual mode to use them.
 *
 *   Good luck!
 *   David Fisher 10-2-2015
 */

#include <SoftwareSerial.h>

// These are shortcuts that you can use if you find yourself typing the same thing a lot into the box (if you switch networks a lot)
#define DEFAULT_WIFLY_BAUDRATE_CHOICE '2' // corresponds to choice 2 which is 57600 (main baudrate used).  For the initial question just hit Send instead of 2 <Send> if you want this choice.
#define HARDCODED_NETWORK_NAME "RHIT-OPEN"  // This is used for option 2 in the shortcut menu.  Rose students need RHIT-OPEN, but set it differently if needed.
#define DEFAULT_OTHER_NETWORK_NAME "Casa$de$Fisher"  // This is used if you don't pass a parameter to option 3 (set as needed to reduce typing if you like for your alternate network than option 2).
#define DEFAULT_NETWORK_PASSWORD "Rose-Hulman" // This is used if you don't pass a parameter to option 4 (set as needed to reduce typing if you like, love putting passwords in plain text :) ).

// If you are not doing setup stuff, you can use the contants below to make a direct serial bridge to WiFly.
#define USE_DIRECT_SERIAL_BRIDGE false  // Set this value to 1 only if you know exactly what you're doing with WiFly. :)
#define USE_DIRECT_SERIAL_BRIDGE_BAUDRATE 57600 // Set the WiFly baudrate value directly here as you will not get any menus with this option

SoftwareSerial WiflySerial(15, 14);  // SoftwareSerial (RX, TX)

/**
 * Puts the WiFly into command mode.
 */
void setup() {
  boolean didEnterCommandMode = false;
  Serial.begin(115200);  // Baudrate used in the Serial Monitor window (can be anything)

  // Not recommended unless you know what you are doing.
  if (USE_DIRECT_SERIAL_BRIDGE) {
    Serial.println("USE_DIRECT_SERIAL_BRIDGE is set to true!");
    Serial.println(" Tips: Enter WiFly's command mode via $$$ with 'No line ending' then use 'Carriage return' for commands.");
    WiflySerial.begin(USE_DIRECT_SERIAL_BRIDGE_BAUDRATE);
    runManualMode();  // never to return
  }

  // Use the helper function to put your WiFly into command mode.
  didEnterCommandMode = enterCommandModeWithWiFly();
  if (!didEnterCommandMode) {
    Serial.println(F("\nAbort!\n"));
    while(1);  // Abort this run by stopping any further execution.  Nothing more will happen.  Cycle RedBot power to try again.
  }
}

/**
 * Loops endlessly asking the user for commands to send.  See recipes for commands in the top comment block.
 */
void loop() {
  // Select an option below:
  //   0: Exit this shortcut menu and just let me manually type commands to send to the WiFly.
  //   1: scan (this option looks for WiFi networks that are in range)
  //   2: set wlan ssid RHIT-OPEN
  //   3: set wlan ssid <network name> (example usage: 3 myNetworkName)
  //   4: set wlan pass <password> (example usage: 4 ifUneed1)
  //   b: set uart baudrate <baudrate choice of either 1 for 9600, 2 for 57600, 3 for 115200>
  //   n: show net (see if the WiFly is connected to the WiFi or not)
  //   i: get ip a (get the ip address of the WiFly)
  //   h: set opt deviceid <customhostname> (Rose students please don't change the device name!)
  //   a: set wlan join 1 (auto connect on startup. This needs to be done only once.)
  //   f: factory RESET (just in case you are really having issues and want to start over)
  //   s: save
  //   r: reboot
  //   x: exit (this exits the WiFly command mode)
  char stringParameter[64];
  unsigned long millisInitialValue;
  char selection = getMenuSelection(stringParameter);
  switch (selection) {
    case '0':
      Serial.println(F("0")); // Display the user's selection
      runManualMode();  // never to return
      break;
    case '1':
      Serial.println(F("1")); // Display the user's selection
      Serial.println(F("scan")); // Display the command to the user
      Serial.println(F("Scanning..."));
      WiflySerial.print(F("scan\r")); // Send it to WiFly
      // From datasheet: "The default scan time is 200 ms/channel or about 3 seconds."
      displayPrintableWiFlyCharacters(4000);
      break;
    case '2':
      Serial.println(F("2")); // Display the user's selection
      Serial.print(F("set wlan ssid "));
      Serial.println(HARDCODED_NETWORK_NAME);
      WiflySerial.print(F("set wlan ssid "));
      WiflySerial.print(HARDCODED_NETWORK_NAME);
      WiflySerial.print(F("\r"));
      checkForWiFlyConfirmation(selection);
      break;
    case '3':
      Serial.println(F("3")); // Display the user's selection
      Serial.print(F("set wlan ssid "));
      WiflySerial.print(F("set wlan ssid "));
      if (stringParameter[0] == '\0') {
        Serial.println(DEFAULT_OTHER_NETWORK_NAME);
        WiflySerial.print(DEFAULT_OTHER_NETWORK_NAME);
      } else {
        Serial.println(stringParameter);
        WiflySerial.print(stringParameter);
      }
      WiflySerial.print(F("\r"));
      checkForWiFlyConfirmation(selection);
      break;
    case '4':
      Serial.println(F("4")); // Display the user's selection
      Serial.print(F("set wlan pass "));
      WiflySerial.print(F("set wlan pass "));
      if (stringParameter[0] == '\0') {
        Serial.println(DEFAULT_NETWORK_PASSWORD);
        WiflySerial.print(DEFAULT_NETWORK_PASSWORD);
      } else {
        Serial.println(stringParameter);
        WiflySerial.print(stringParameter);
      }
      WiflySerial.print(F("\r"));
      checkForWiFlyConfirmation(selection);
      break;
    case 'b':
      Serial.println(F("b")); // Display the user's selection
      Serial.print(F("set uart baudrate "));
      WiflySerial.print(F("set uart baudrate "));
      if (stringParameter[0] == '\0') {
        stringParameter[0] = DEFAULT_WIFLY_BAUDRATE_CHOICE;
      }
      switch (stringParameter[0]) {
        case '1':
          Serial.println(F("9600"));
          WiflySerial.print(F("9600\r"));
          break;
        case '2':
          Serial.println(F("57600"));
          WiflySerial.print(F("57600\r"));
          break;
        case '3':
          Serial.println(F("115200"));
          WiflySerial.print(F("115200\r"));
          break;
        default:
          Serial.println(F("Error!  did not receive a baudrate parameter!  Please try again."));
          break;
      }
      checkForWiFlyConfirmation(selection);
      break;
    case 'n':
      Serial.println(F("n")); // Display the user's selection
      Serial.println(F("show net"));
      WiflySerial.print(F("show net\r"));
      displayPrintableWiFlyCharacters(2000);
      break;
    case 'i':
      Serial.println(F("i")); // Display the user's selection
      Serial.println(F("get ip a"));
      WiflySerial.print(F("get ip a\r"));
      displayPrintableWiFlyCharacters(2000);
      break;
    case 'h':
      Serial.println(F("h")); // Display the user's selection
      Serial.print(F("set opt deviceid "));
      Serial.println(stringParameter);
      WiflySerial.print(F("set opt deviceid "));
      WiflySerial.print(stringParameter);
      WiflySerial.print(F("\r"));
      checkForWiFlyConfirmation(selection);
      break;
    case 'a':
      Serial.println(F("a")); // Display the user's selection
      Serial.println(F("set wlan join 1"));
      WiflySerial.print(F("set wlan join 1\r"));
      checkForWiFlyConfirmation(selection);
      break;
    case 'f':
      Serial.println(F("f")); // Display the user's selection
      Serial.println(F("factory RESET"));
      WiflySerial.print(F("factory RESET\r"));
      Serial.println(F("reboot  (note the baudrate is now 9600)"));
      WiflySerial.print(F("reboot\r"));
      runManualMode();  // never to return
      break;
    case 's':
      Serial.println(F("s")); // Display the user's selection
      Serial.println(F("save"));
      WiflySerial.print(F("save\r"));
      checkForWiFlyConfirmation(selection);
      break;
    case 'r':
      Serial.println(F("r")); // Display the user's selection
      Serial.println(F("reboot"));
      WiflySerial.print(F("reboot\r"));
      runManualMode();  // never to return
      break;
    case 'x':
      Serial.println(F("x")); // Display the user's selection
      Serial.println(F("exit"));
      WiflySerial.print(F("exit\r"));
      runManualMode();  // never to return
      break;
    case 'm':
      // This is a hidden command that we need at Rose.
      Serial.println(F("m")); // Display the user's selection
      Serial.println(F("get mac"));
      WiflySerial.print(F("get mac\r"));
      displayPrintableWiFlyCharacters(2000);
      break;
    default:
      Serial.print(selection);
      Serial.println(F("Unknown command"));
      break;
  }
  delay(100); // not required I just like having small delays at the end of the loop function if possible. :)
}


/**
 * Puts the user into a direct serial bridge mode as described below.
 */
void runManualMode() {
  Serial.println(F("You are now directly communicating with the WiFly."));
  Serial.println(F("Things you type will be sent to WiFly.  Things from WiFly display on the Serial Monitor."));
  Serial.println(F("If you ever want to go back to the menu mode, just close and then reopen the Serial Monitor."));
  while(1) {
    if (WiflySerial.available()) {
      Serial.write(WiflySerial.read());
    }
    if (Serial.available()) {
      WiflySerial.write(Serial.read());
    }
  }
}
