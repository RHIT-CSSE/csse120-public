"""
The goal of this module is to practice running code on the EV3.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time


# -----------------------------------------------------------------------------
# TODO: 2. Put your own name where the code below says "PUT_YOUR_NAME_HERE".
#  Then, with your instructor's help:
#   1. Do the PyCharm setup necessary to connect to your EV3 robot.
#   2. Connect to your EV3 robot.
#   3. Deploy this file to the EV3 robot (i.e., copy this file to the robot).
#   4. Make an SSH connection to your EV3 robot.
#   5. In your SSH window (running on your robot, but displayed in PyCharm):
#      a. Change directory (CD) into the correct folder, then
#      b. Run this program on your robot (NOT on your computer!)
#         by typing at the SSH prompt the command:
#                python  m1_hello_world.py
#         Use "auto-complete" to help you type the filename (the .py file).
#         Try the up-arrow key to redo the command.
#   6. In PyCharm:
#      a. Modify the program as desired, then
#      b. Repeat Step 3 above to re-deploy the (modified) program.
#      c. In your existing SSH window, repeat step 5b to re-run the program.
#         (If your SSH window is gone, you can repeat step 4 to make a new one.)
# -----------------------------------------------------------------------------
def main():
    name = "PUT_YOUR_NAME_HERE"
    for k in range(10):
        print(k, "Hello, " + name)
        time.sleep(0.75)
    print("Goodbye")


main()
