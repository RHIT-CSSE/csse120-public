/*******************************************************************************
 * A RoseBot uses a master/slave architecture where:
 *   -- The slave runs on an Arduino. It controls the robot hardware.
 *   -- The master runs on some other device, e.g. in CSSE 120
 *        a Python program running on a laptop.
 *   -- The master repeatedly sends commands to the slave,
 *        which executes those commands.
 *
 * This file contains the code for the slave, running on the Arduino.
 * It uses the following protocol:
 *   1. Establish a connection to the master.
 *        (or a connection like the WiFly that behaves like a Serial).
 *   2. Repeatedly:
 *        a. Fetch a command from the master.
 *        b. Send an acknowledgment (optional).
 *        c. Execute the command, sending to the master any information
 *             that is requested.
 *
 * FIXME: Is the above comment about WiFly accurate.  Fix next paragraph.
 *
 * Currently:
 *   -- The bytes-read are always 3 bytes where:
 *        Byte 1 encodes the COMMAND.
 *        Byte 2 encodes the SIGNAL for the command (e.g. LED), if any.
 *        Byte 3 encodes the DATA for the command
 *          (e.g. a digital value to write), if any.
 *   -- The acknowledgement is the first of the bytes that it read
 *          for the COMMAND.
 *   -- 10-bit sensor data is sent as one byte,
 *         truncating each item by 2 bits.
 *         
 * Authors:  David Mutchler and Valerie Galluzz, based on work by Dave Fisher
 *           and Sparkfun.  February, 2017.
 ******************************************************************************/

// TODO: Improve the simple communication protocol being used, by:
//         -- Compact messages to improve performance.
//         -- Add error detection and recovery.
//         -- Allow additional commands.





