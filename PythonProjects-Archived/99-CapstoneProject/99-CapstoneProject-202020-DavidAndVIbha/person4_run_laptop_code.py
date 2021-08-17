"""
Use this module to run code that should run on your LAPTOP.
ALWAYS run THIS module for laptop code,
NOT the ones in any of the SUB-FOLDERS.
"""

import project4_individual.run_this_on_LAPTOP as run_on_laptop


def main():
    """ Runs the LAPTOP main function. """
    run_on_laptop.main()


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
