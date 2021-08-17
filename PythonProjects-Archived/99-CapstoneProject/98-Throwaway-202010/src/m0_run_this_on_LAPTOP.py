"""
  THROW-AWAY Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
  Fall term, 2019-2020.
"""
# TODO 1:  Put the name of EACH team member in the above.

import tkinter
from tkinter import ttk

import m1_laptop_code as m1
import m2_laptop_code as m2
import m3_laptop_code as m3


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs and displays a GUI for teleoperation and EACH team
         member's part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # TODO: The root TK object for the GUI:
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: The main frame, upon which the other frames are placed:
    #   Give it a fun title (keep it G-rated!)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: Each team member has their own frame for their own GUI.
    #   Get them from each mX.get_my_frame(), and grid them left to right.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: The event loop:
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
