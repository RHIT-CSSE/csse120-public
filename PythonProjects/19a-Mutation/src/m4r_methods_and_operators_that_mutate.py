"""
This module shows some common methods and operators that mutate lists:
  -- append, insert, sort, remove
  -- the DEL and IS operators
  -- the IS vs == operators
  

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2.  *** There is a FOLLOW-ME VIDEO associated with this module. ***
#  Start running that video and follow along with it.  Change this _TODO_
#  to DONE after you have started the associated follow-me video.
# -----------------------------------------------------------------------------

import time
import testing_helper


def main():
    """ Run these one at a time to demonstrate the concepts. """
    # show_append()
    # show_insert()
    # show_sort()
    # show_remove()
    # show_del()
    # show_is_vs_equals()
    # show_in()


def show_append():
    # Use APPEND to add an item at the end of the list:
    print()
    print("Showing APPEND:")

    example = [10, "hello", 3]
    print("  Before appending:     ", example)

    example.append("ok")
    print("  After appending once: ", example)

    example.append(505)
    print("  After appending again:", example)


def show_insert():
    # Use INSERT to add an item before a given position in the list.
    print()
    print("Showing INSERT:")

    example = [10, 20, 30, 40, 50]
    print("  Before inserting:")
    print("     ", example)

    example.insert(3, 88)
    print("  After inserting 88 before index 3:")
    print("     ", example)

    example.insert(1, 99)
    print("  After inserting 99 before index 1:")
    print("     ", example)

    example.insert(3, 33)
    print("  After inserting 33 before index 3:")
    print("     ", example)


def show_sort():
    # Use SORT to sort a list.
    print()
    print("Showing SORT:")

    example = [3, 1, 8, 3, 20, 2, 5, 7]
    print("  Before sort:")
    print("     ", example)

    example.sort()
    print("  After sort:")
    print("     ", example)


def show_remove():
    # Use REMOVE to remove a specified item:
    print()
    print("Showing REMOVE:")

    example = [10, "hello", 3, 20, "ok", "hello", 3, 3, 3]
    print("  Before removing:")
    print("     ", example)

    example.remove(20)
    print("  After removing 20:")
    print("     ", example)

    example.remove("hello")
    print("  After removing 'hello':")
    print("     ", example)

    example.remove(3)
    print("  After removing 3:")
    print("     ", example)

    example.remove(3)
    print("  After removing another 3:")
    print("     ", example)

    print("  Attempting to remove an item")
    print("  that is not in the list (crashes):")
    example.remove(5)


def show_del():
    # Use DEL to remove an item at a specified index:
    print()
    print("Showing DEL:")

    example = [10, "hello", 3, 20, "ok", "hello", 3, 3, 3]
    print("  Before deleting:")
    print("     ", example)

    del example[4]
    print("  After deleting the item as index 4:")
    print("     ", example)

    del example[0]
    print("  After deleting the item as index 0:")
    print("     ", example)

    print("  Attempting to delete an item at an")
    print("  index beyond the end of the list (crashes):")
    del example[10]


def show_is_vs_equals():
    # Show the difference between the IS and == operators
    print()
    print("Showing IS vs ==:")

    example1 = [10, 3, 100, "hello"]
    example2 = [10, 3, 100, "hello"]
    example3 = example1
    example4 = example1.copy()

    print("Using IS: ", example1 is example2)
    print("Using ==: ", example1 == example2)

    print("Using IS again: ", example1 is example3)
    print("Using == again: ", example1 == example3)

    print("Using IS yet again: ", example1 is example4)
    print("Using == yet again: ", example1 == example4)


def show_in():
    # Use the IN operator to determine whether a given item is in a list.
    print()
    print("Showing IN:")

    example = [3, 1, 8, 3, 20, "hello", 2, 5, 7]
    print("  The example list is:")
    print("     ", example)

    print("  Is 20 in the list?     ", 20 in example)
    print("  Is 'hello' in the list?", 'hello' in example)
    print("  Is 99 in the list?     ", 99 in example)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
