#!/usr/bin/env python3
"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1.  Put your name in the above.

import rosebot
import mqtt_remote_method_calls as com
import time


def main():
    """ Test a robot's using MQTT. """
    print()
    print('--------------------------------------------------')
    print(' Listening for MQTT messages from the PC')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 3. Construct an MQTT client passing in the robot as the argument.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 4. Connect to talk to the laptop
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 5. Create a loop which can be shutdown
    #          Add a field on the robot called should_shutdown
    #          That is set to False
    #          And add a method that can modify that field called shutdown
    # -------------------------------------------------------------------------


main()
