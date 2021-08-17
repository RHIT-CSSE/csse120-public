"""
Use this module to run code that should run on your ROBOT.
ALWAYS run THIS module for robot code, NOT the ones in any of the SUB-FOLDERS.
"""
# -----------------------------------------------------------------------------
# IMPORTANT: Do NOT commit this module, since doing so may lead to CONFLICTS
# with how TEAMMATES are using this module to test THEIR code.
# -----------------------------------------------------------------------------

import labs.lab1a_drive_system as lab1a
import labs.lab1b_drive_system as lab1b
import labs.lab2a_touch_sensor as lab2a


def main():
    """ Runs the TEST functions. """
    # -------------------------------------------------------------------------
    # Un-comment the appropriate line below for what YOU want to TEST.
    # -------------------------------------------------------------------------
    # lab1a.main()
    # lab1b.main()
    # lab2a.main()
    lab2b.main()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,')
    print('your code raised the following exception:')
    print()
    time.sleep(1)
    raise
