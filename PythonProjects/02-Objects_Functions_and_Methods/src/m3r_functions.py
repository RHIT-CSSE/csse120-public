"""
Exploration of CALLING FUNCTIONS.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2. READ the code below. TRACE (by hand) the execution of the code,
#   predicting what will get printed.  Then run the code
#   and compare your prediction to what actually was printed.
#   Then mark this _TODO_ as DONE and commit-and-push your work.
###############################################################################


def main():
    hello("Snow White")
    goodbye('Bashful')
    hello("Grumpy")
    hello("Sleepy")
    hello_and_goodbye("Magic Mirror", "Cruel Queen")


def hello(friend):
    print("Hello,", friend, "- how are things?")


def goodbye(friend):
    print("Goodbye,", friend, "- see you later!")
    print('   Ciao!')
    print('   Bai bai!')


def hello_and_goodbye(person1, person2):
    hello(person1)
    goodbye(person2)


main()
