"""
This project lets you practice NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the other functions to test them. """
    print()
    print("Un-comment and re-comment calls in MAIN one by one as you work.")

    # run_test_largest_number()
    # run_test_largest_negative_number()
    # run_test_first_is_elsewhere_too()
    # run_test_integers()
    # run_test_big_letters()
    # run_test_bigger_than_indices()


def run_test_largest_number():
    """ Tests the    largest_number    function. """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  largest_number  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    # -------------------------------------------------------------------------
    print()
    print("----------------------------------------")
    print("Testing the   largest_number   function:")
    print("----------------------------------------")

    format_string = "    largest_number( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 13
    print_expected_result_of_test([[(3, 1, 4),
                                    (13, 10, 11, 7, 10),
                                    [1, 2, 3, 4]]],
                                  expected, test_results, format_string)
    actual = largest_number([(3, 1, 4),
                             (13, 10, 11, 7, 10),
                             [1, 2, 3, 4]])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = -1111111111111111
    print_expected_result_of_test([([], [-1111111111111111], [])],
                                  expected, test_results, format_string)
    actual = largest_number(([],
                             [-1111111111111111],
                             []))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = None
    print_expected_result_of_test([[], [], [], [], [], []],
                                  expected, test_results, format_string)
    actual = largest_number([[], [], [], [], [], []])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 20
    print_expected_result_of_test([((),
                                    (),
                                    (10, 8, 20, 12, 19, 6, 20, 1, 2, 3),
                                    (1, 2, 3, 4, 5, 6),
                                    (19, 18, 3, 7),
                                    ())],
                                  expected, test_results, format_string)
    actual = largest_number(((),
                             (),
                             (10, 8, 20, 12, 19, 6, 20, 1, 2, 3),
                             (1, 2, 3, 4, 5, 6),
                             (19, 18, 3, 7),
                             ()))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 60
    print_expected_result_of_test([((),
                                    (),
                                    (10, 8, 20, 12, 19, 6, 20, 1, 2, 3),
                                    (1, 2, 3, 4, 5, 60),
                                    (19, 18, 3, 7),
                                    ())],
                                  expected, test_results, format_string)
    actual = largest_number(((),
                             (),
                             (10, 8, 20, 12, 19, 6, 20, 1, 2, 3),
                             (1, 2, 3, 4, 5, 60),
                             (19, 18, 3, 7),
                             ()))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 70
    print_expected_result_of_test([((),
                                    (),
                                    (10, 8, 20, 12, 19, 6, 20, 1, 2, 3),
                                    (1, 2, 3, 4, 5, 6),
                                    (19, 18, 3, 70),
                                    ())],
                                  expected, test_results, format_string)
    actual = largest_number(((),
                             (),
                             (10, 8, 20, 12, 19, 6, 20, 1, 2, 3),
                             (1, 2, 3, 4, 5, 6),
                             (19, 18, 3, 70),
                             ()))
    print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # TODO: 2 (continued): Add your ADDITIONAL test here:
    # -------------------------------------------------------------------------

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def largest_number(seq_seq):
    """
    Returns the largest number in the subsequences of the given
    sequence of sequences.  Returns None if there are NO numbers
    in the subsequences.

    For example, if the given argument is:
        [(3, 1, 4),
         (13, 10, 11, 7, 10),
         [1, 2, 3, 4]]
    then this function returns 13.

    As another example, if the given argument is:
      ([], [-1111111111111111], [])
    then this function returns -1111111111111111.

    As yet another example, if the given argument is:
      ([], [], [], [], [], [])
    then this function returns None.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences,
    where each subsequence contains only numbers.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  __
    #  IMPLEMENTATION RESTRICTION:  You may NOT use the builtin functions:
    #     max    min    or the list functions:   index_of   count   in
    #  since their use may defeat the goal of providing
    #  practice at loops within loops (within loops within ...)
    # -------------------------------------------------------------------------


def run_test_largest_negative_number():
    """ Tests the    largest_negative_number    function. """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement this TEST function as needed.
    #   It TESTS the  largest_negative_number  function defined below.
    #  __
    #  YOU decide whether or not you think that the tests below are adequate
    #  to give you confidence that your solution to this challenging
    #  problem is indeed correct.  Add more tests if you think you need more.
    # -------------------------------------------------------------------------
    print()
    print("-------------------------------------------------")
    print("Testing the   largest_negative_number   function:")
    print("-------------------------------------------------")

    format_string = "    largest_negative_number( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = -2.6
    print_expected_result_of_test([[(30, -5, 8, -20),
                                    (100, -2.6, 88, -40, -5),
                                    (400, 500)]],
                                  expected, test_results, format_string)
    actual = largest_negative_number([(30, -5, 8, -20),
                                      (100, -2.6, 88, -40, -5),
                                      (400, 500)])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = None
    print_expected_result_of_test([[(200, 2, 20), (500, 400)]],
                                  expected, test_results, format_string)
    actual = largest_negative_number([(200, 2, 20), (500, 400)])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -1111111111111111
    print_expected_result_of_test([([], [-1111111111111111], [])],
                                  expected, test_results, format_string)
    actual = largest_negative_number(([],
                                      [-1111111111111111],
                                      []))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = None
    print_expected_result_of_test([[], [], [], [], [], []],
                                  expected, test_results, format_string)
    actual = largest_negative_number([[], [], [], [], [], []])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = -2
    print_expected_result_of_test([((),
                                    (),
                                    (10, 8, -20, 12, 19, 6, 20, 1, 2, 3),
                                    (-2, -3, -4, -5, -6),
                                    (-19, 18, -3, -7),
                                    ())],
                                  expected, test_results, format_string)
    actual = largest_negative_number(((),
                                      (),
                                      (10, 8, -20, 12, 19, 6, 20, 1, 2, 3),
                                      (-2, -3, -4, -5, -6),
                                      (-19, 18, -3, -7),
                                      ()))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = -3
    print_expected_result_of_test([((),
                                    (),
                                    (10, 8, -20, 12, 19, 6, 20, 1, 2, 3),
                                    (2, 3, -4, -5, 0, -6, 10),
                                    (-19, 18, -3, -7),
                                    ())],
                                  expected, test_results, format_string)
    actual = largest_negative_number(((),
                                      (),
                                      (10, 8, -20, 12, 19, 6, 20, 1, 2, 3),
                                      (2, 3, -4, -5, 0, -6, 10),
                                      (-19, 18, -3, -7),
                                      ()))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = -1
    print_expected_result_of_test([((),
                                    (),
                                    (10, 8, -20, 12, 19, 6, 20, 1, 2, 3),
                                    (2, 3, -4, -5, 0, -6, 10),
                                    (-19, 18, -3, -1),
                                    ())],
                                  expected, test_results, format_string)
    actual = largest_negative_number(((),
                                      (),
                                      (10, 8, -20, 12, 19, 6, 20, 1, 2, 3),
                                      (2, 3, -4, -5, 0, -6, 10),
                                      (-19, 18, -3, -1),
                                      ()))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = -10000000000000000000000
    print_expected_result_of_test([((),
                                    (),
                                    (-10000000000000000000000,),
                                    (2, 3, 4, 5, 0, 6, 10),
                                    (19, 18, 3, 1),
                                    ())],
                                  expected, test_results, format_string)
    actual = largest_negative_number(((),
                                      (),
                                      (-10000000000000000000000,),
                                      (2, 3, 4, 5, 0, 6, 10),
                                      (19, 18, 3, 1),
                                      ()))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = -10000000000000000000000
    print_expected_result_of_test([((),
                                    (),
                                    (2, 3, 4, 5, 0, 6, 10),
                                    (19, 18, 3, 1),
                                    (),
                                    (-10000000000000000000000,))],
                                  expected, test_results, format_string)
    actual = largest_negative_number(((),
                                      (),
                                      (2, 3, 4, 5, 0, 6, 10),
                                      (19, 18, 3, 1),
                                      (),
                                      (-10000000000000000000000,)))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = None
    print_expected_result_of_test([((),
                                    (),
                                    (2, 3, 4, 5, 0, 6, 10),
                                    (19, 18, 3, 1),
                                    (),
                                    (10000000000000000000000,))],
                                  expected, test_results, format_string)
    actual = largest_negative_number(((),
                                      (),
                                      (2, 3, 4, 5, 0, 6, 10),
                                      (19, 18, 3, 1),
                                      (),
                                      (10000000000000000000000,)))
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def largest_negative_number(seq_seq):
    """
    Returns the largest NEGATIVE number in the given sequence of
    sequences of numbers.  Returns None if there are no negative numbers
    in the sequence of sequences.

    For example, if the given argument is:
        [(30, -5, 8, -20),
         (100, -2.6, 88, -40, -5),
         (400, 500)
        ]
    then this function returns -2.6.

    As another example, if the given argument is:
      [(200, 2, 20), (500, 400)]
    then this function returns None.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences,
    where each subsequence contains only numbers.
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  __
    #  IMPLEMENTATION RESTRICTION:  You may NOT use the builtin functions:
    #     max    min    or the list functions:   index_of   count   in
    #  since their use may defeat the goal of providing
    #  practice at loops within loops (within loops within ...)
    #  __
    #  CHALLENGE: Try to solve this problem with no additional sequences
    #    being constructed (so the SPACE allowed is limited to the
    #    give sequence of sequences plus any non-list variables you want).
    # -------------------------------------------------------------------------


def run_test_first_is_elsewhere_too():
    """ Tests the    first_is_elsewhere_too    function. """
    # -------------------------------------------------------------------------
    # We have supplied tests for you. No additional tests are required,
    # although you are welcome to supply more tests if you choose.
    # -------------------------------------------------------------------------
    print()
    print("------------------------------------------------")
    print("Testing the   first_is_elsewhere_too   function:")
    print("------------------------------------------------")

    format_string = "    first_is_elsewhere_too( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = True
    print_expected_result_of_test([[(3, 5, 1, 4),
                                    (13, 10, 11, 7, 10),
                                    [11, 12, 5, 10]]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([(3, 5, 1, 4),
                                     (13, 10, 11, 7, 10),
                                     [11, 12, 5, 10]])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = False
    print_expected_result_of_test([[(3, 1, 4),
                                    (13, 10, 11, 7, 10),
                                    [11, 2, 13, 14]]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([(3, 1, 4),
                                     (13, 10, 11, 7, 10),
                                     [11, 2, 13, 14]])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = False
    print_expected_result_of_test([[[], [1, 2], [1, 2]]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([[], [1, 2], [1, 2]])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = True
    print_expected_result_of_test([(("a", 9),
                                    (13, 10, 11, 7, "a"),
                                    (),
                                    (11, 12, 3, 10))],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too((("a", 9),
                                     (13, 10, 11, 7, "a"),
                                     (),
                                     (11, 12, 3, 10)))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = False
    print_expected_result_of_test([(("a", 9),
                                    (13, 10, 11, 7, "aa"),
                                    [11, 12, 3, 10])],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too((("a", 9),
                                     (13, 10, 11, 7, "999"),
                                     [11, 12, 3, 10]))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = False
    print_expected_result_of_test([[("a", "a", "b", "b", "a", "b")]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([("a", "a", "b", "b", "a", "b")])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = False
    print_expected_result_of_test([[()]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([()])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = True
    print_expected_result_of_test([[("a",), (), (), (), ("a",), ()]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([("a",), (), (), (), ("a",), ()])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = False
    print_expected_result_of_test([("a",), (), (), (), ("b",), ()],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too((("a",), (), (), (), ("b",), ()))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = False
    print_expected_result_of_test([[]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = True
    print_expected_result_of_test([["hello", "goodbye"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(["hello", "goodbye"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = False
    print_expected_result_of_test([["hello", "xxxxxxxxxxx"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(["hello", "xxxxxxxxxxx"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = True
    print_expected_result_of_test([["hello",
                                    "xxxxxxxx",
                                    "this",
                                    "is",
                                    "a",
                                    "test",
                                    "o"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(["hello",
                                     "xxxxxxxx",
                                     "this",
                                     "is",
                                     "a",
                                     "test",
                                     "o"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = True
    print_expected_result_of_test([["hello",
                                    "xxxxxxxx",
                                    "this",
                                    "is",
                                    "aoaoaoaoaoaoa",
                                    "test",
                                    "z"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(["hello",
                                     "xxxxxxxx",
                                     "this",
                                     "is",
                                     "aoaoaoaoaoaoa",
                                     "test",
                                     "z"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = True
    print_expected_result_of_test([["hello",
                                    "xxxxxxxx",
                                    "this",
                                    "is",
                                    "aaaaaaaaaaaaaa e aaaaaaaaa",
                                    "tEst",
                                    "z"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(["hello",
                                     "xxxxxxxx",
                                     "this",
                                     "is",
                                     "aaaaaaaaaaaaaa e aaaaaaaaa",
                                     "tEst",
                                     "z"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = True
    print_expected_result_of_test([["hello",
                                    "xxxxxxxx",
                                    "this",
                                    "is",
                                    "aaaaaaaaaaaaaa e aaaaaaaaa",
                                    "tEst",
                                    "z"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(["hello",
                                     "xxxxxxxx",
                                     "this",
                                     "is",
                                     "aaaaaaaaaaaaaa e aaaaaaaaa",
                                     "tEst",
                                     "z"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17:
    expected = False
    print_expected_result_of_test([["1234567890",
                                    "one two three",
                                    "i am free",
                                    "four five six",
                                    "get my sticks",
                                    "seven eight nine",
                                    "i am fine"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(["1234567890",
                                     "one two three",
                                     "i am free",
                                     "four five six",
                                     "get my sticks",
                                     "seven eight nine",
                                     "i am fine"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = True
    print_expected_result_of_test([[(1000 * "a") + "b" + (500 * "a"),
                                    (800 * "c") + "d" + 1200 * "c",
                                    "b"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([(1000 * "a") + "b" + (500 * "a"),
                                     (800 * "c") + "d" + 1200 * "c",
                                     "b"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19:
    expected = True
    print_expected_result_of_test([[(1000 * "a") + "b" + (500 * "a"),
                                    (800 * "c") + "d" + 1200 * "c",
                                    (700 * "eee") + "b" + (90 * "d"),
                                    (800 * "c") + "d" + 1200 * "c"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([(1000 * "a") + "b" + (500 * "a"),
                                     (800 * "c") + "d" + 1200 * "c",
                                     (700 * "eee") + "b" + (90 * "d"),
                                     (800 * "c") + "d" + 1200 * "c"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 20:
    expected = True
    print_expected_result_of_test([[(1000 * "b") + "acd" + (500 * "f"),
                                    (800 * "1") + "234a",
                                    "eeee"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([(1000 * "b") + "acd" + (500 * "f"),
                                     (800 * "1") + "234a",
                                     "eeee"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 21:
    expected = False
    print_expected_result_of_test([[(1000 * "b") + "cd" + (500 * "f"),
                                    (800 * "1") + "234a",
                                    "eeee",
                                    "hello",
                                    "none",
                                    "oopsie"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([(1000 * "b") + "cd" + (500 * "f"),
                                     (800 * "1") + "234a",
                                     "eeee",
                                     "hello",
                                     "none",
                                     "oopsie"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 22:
    expected = False
    print_expected_result_of_test([[[(1000 * "b") + "cda" + (500 * "f")],
                                    (800 * "b") + "234a",
                                    "eeee",
                                    "hello",
                                    "none",
                                    "oopsie"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([[(1000 * "b") + "cda" + (500 * "f")],
                                     (800 * "b") + "234a",
                                     "eeee",
                                     "hello",
                                     "none",
                                     "oopsie"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 23:
    expected = True
    print_expected_result_of_test([[(1000 * "b") + "acd" + (500 * "f"),
                                    "a" + (800 * "1") + "234",
                                    "123"]],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too([(1000 * "b") + "acd" + (500 * "f"),
                                     "a" + (800 * "1") + "234",
                                     "123"])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 24:
    expected = True
    test1 = [(1000 * "b") + "acd" + (500 * "f"),
             (800 * "1") + "234",
             "123"]
    for k in range(95):
        test1.append(k * chr(k))
    test2 = []
    for k in range(30):
        test2.append(k * chr(k))

    print_expected_result_of_test([test1 + ["a"] + test2],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(test1 + ["a"] + test2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 25 (continues the previous test):
    expected = False
    print_expected_result_of_test([test1 + test2],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(test1 + test2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 26 (continues the previous test):
    a_inside = (100 * "b") + "a" + (100 * "b")
    expected = True
    print_expected_result_of_test([test1 + [a_inside] + test2],
                                  expected, test_results, format_string)
    actual = first_is_elsewhere_too(test1 + [a_inside] + test2)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def first_is_elsewhere_too(seq_seq):
    """
    Given a sequence of subsequences:
      -- Returns True if any element of the first (initial) subsequence
           appears in any of the other subsequences.
      -- Returns False otherwise.

    For example, if the given argument is:
        [(3, 5, 1, 4),
         (13, 10, 11, 7, 10),
         [11, 12, 5, 10]]
    then this function returns True because 5 appears
    in the first subsequence and also in the third subsequence.

    As another example, if the given argument is:
        [(3, 1, 4),
         (13, 10, 11, 7, 10),
         [11, 2, 13, 14]]
    then this function returns False because:
      3 does not appear in any subsequence except the first,
      1 does not appear in any subsequence except the first, and
      4 does not appear in any subsequence except the first.

    As yet another example, if the given argument is:
      ([], [1, 2], [1, 2])
    then this function returns False since no element of the first
    subsequence appears elsewhere.

    Similarly,  if the given argument is:
      []
    then this function returns False since there are no subsequences.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences.
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Some tests are already written for you (above).
    #  __
    #  IMPLEMENTATION RESTRICTION:
    #   ** You may NOT use anything but comparison (==) in judging
    #      membership.  In particular, you may NOT use:
    #        -- the IN operator
    #              (example:  7 in [9, 6, 7, 9] returns True)
    #        -- the COUNT method
    #              (example:  [9, 6, 7, 9].count(9) returns 2)
    #        -- the INDEX method
    #              (example:  [9, 6, 7, 9, 6, 1].index(6) returns 1)
    #   in this problem, as doing so may defeat the goal of providing
    #   practice at loops within loops (within loops within ...)
    # -------------------------------------------------------------------------


def run_test_integers():
    """ Tests the    integers    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   integers   function:')
    print('--------------------------------------------------')

    format_string = '    integers( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4),
                             (10, 'hi', 10),
                             [1, 2.5, 3, 4],
                             'hello',
                             [],
                             ['oops'],
                             [[55], [44]],
                             [30, -4]
                             ]
    expected = [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = integers(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4, 'hmmm', [3, 1, 4], 55555555555),
                             'this is a string',
                             'ok',
                             [],
                             ['oops'],
                             [[55], 5555, [44], 4444, (4, 5), 4, 5],
                             (),
                             [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                             [1000],
                             (1, 2, 3, 4, 5, 1, 2, 3, 4, 5),
                             (1000,)
                             ]
    expected = [3, 1, 4, 55555555555, 5555, 4444, 4, 5, 1, 2, 3, 4, 5,
                1, 2, 3, 4, 5, 1000, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1000]
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = integers(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


# See the IMPORTANT HINT in the _TODO_ for the following problem.
def integers(sequence_of_sequences):
    """
    Returns a new list that contains all the integers in the subsequences
    of the given sequence, in the order that they appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [[55], [44]],
         [30, -4]
        ]
    then this function returns:
        [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]

    See the IMPORTANT HINT in the _TODO_ for this problem.

    Type hints:
      :type sequence_of_sequences: (list|tuple) of (list|tuple|string)
      :rtype: list of int
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #  HINT: The
    #           type
    #       function can be used to determine the type of
    #       its argument (and hence to see if it is an integer).
    #       For example, you can write expressions like:
    #         -- if type(34) is int: ...
    #         -- if type(4.6) is float: ...
    #         -- if type('three') is str: ...
    #         -- if type([1, 2, 3]) is list: ...
    #       Note that the returned values do NOT have quotes.
    #       Also, the   is   operator tests for equality (like ==)
    #       but is more appropriate than == in this situation.
    # -------------------------------------------------------------------------


def run_test_big_letters():
    """ Tests the    big_letters    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   big_letters   function:')
    print('--------------------------------------------------')

    format_string = '    big_letters( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4),  # not a string
                             'wHAS what?',  # HAS
                             ['oops'],  # not a string
                             'oops',  #
                             ['OOPS'],  # not a string
                             '1 THIS !',  # THIS
                             ]
    expected = 'HASTHIS'
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = big_letters(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4),  # not a string
                             'Ok what is ThiSSS?',  # OTSSS
                             (10, 'Ok what is ThiSSS?', 10),  # not a string
                             [],  # not a string
                             ['oops'],  # not a string
                             'oops',  #
                             ['OOPS'],  # not a string
                             '1 OOPS !',  # OOPS
                             'A',  # A
                             'ooPS $$&*#%&&',  # PS
                             'B',  # B
                             'oOpS',  # OS
                             'C',  # C
                             'OoPs'  # OP
                             'D',  # D
                             'OOps'  # OO
                             ]
    expected = 'OTSSSOOPSAPSBOSCOPDOO'
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = big_letters(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


# See the IMPORTANT HINT in the _TODO_ for the following problem.
def big_letters(sequence_of_sequences):
    """
    Returns a new STRING that contains all the upper-case letters
    in the subsequences of the given sequence that are strings,
    in the order that they appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),                          # not a string
        'Ok what is ThiSSS?',                # OTSSS
        (10, 'Ok what is ThiSSS?', 10),      # not a string
        [],                                  # not a string
        ['oops'],                            # not a string
        'oops',                              #
        ['OOPS'],                            # not a string
        '1 OOPS !',                          # OOPS
        'A',                                 # A
        'ooPS $$&*#%&&',                     # PS
        'B',                                 # B
        'oOpS',                              # OS
        'C',                                 # C
        'OoPs'                               # OP
        'D',                                 # D
        'OOps'                               # OO
         ]
    then this function returns:
        'OTSSSOOPSAPSBOSCOPDOO'

    See the IMPORTANT HINT in the _TODO_ for the following problem.
    
    Precondition:  the given argument is a sequence of sequences.
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #  HINTS: The  type   function can be used to identify strings,
    #         per the HINT in the previous problem.
    #  ALSO:
    #   There is a STRING METHOD that determines whether or not
    #   a string contains upper-case letters.  To find that method,
    #   somewhere in this file type:
    #           "".
    #   and pause after the dot.
    #   That will display ALL the STRING methods.
    #  __
    #   Look for a method whose name begins with
    #           is
    #   e.g. isalnum()  isdigit() ... [but find the one for upper-case letters]
    ###########################################################################


def run_test_bigger_than_indices():
    """ Tests the   bigger_than_indices   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   bigger_than_indices  function:')
    print('--------------------------------------------------')

    format_string = '    bigger_than_indices( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = ([5, 1],
               [0, 3, 4],
               [6, 3])
    expected = [5, 3, 4, 6]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    numbers = ([5, 1, 1, 1, 1],
               [1, 4, 4, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5])
    expected = [5, 4, 4, 6]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    numbers = ([5, 1, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = [5, 6, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    numbers = ([1, 2, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = [1, 2, 6, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    numbers = ([100, 200, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = [100, 200, 6, 5, 6, 5]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = ([100, 200, 99],
               [300])
    expected = [100, 200, 99, 300]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    numbers = ([98, 200, 99],
               [300])
    expected = [98, 200, 99, 300]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    numbers = ([100, 200, 99],
               [1, 3])
    expected = [100, 200, 99, 3]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = bigger_than_indices(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def bigger_than_indices(numbers):
    """
    What comes in:  A non-empty sequence of non-empty sequences
      of positive integers.
    What goes out:  Returns a list containing every number in the sub-sequences
      that is bigger than the sum of its indices.
      The numbers in the returned list should appear in the same order
      that the numbers appear in the subsequences.
    Examples:
      Suppose that  numbers  is:
          ([5, 1],
           [0, 3, 4],
           [6, 3])
         Then: bigger_than_indices(numbers) examines:
        -- 5: It is at numbers[0][0], so sum of indices is 0,
              so PUT 5 into the list to return.
        -- 1: It is at numbers[0][1], so sum of indices is 1,
              so do NOT put 1 into the list to return.
        -- 0: It is at numbers[1][0], so sum of indices is 1,
              so do NOT put 0 into the list to return.
        -- 3: It is at numbers[1][1], so sum of indices is 2,
              so PUT 3 into the list to return.
        -- 4: It is at numbers[1][2], so sum of indices is 3,
              so PUT 4 into the list to return.
        -- 6: It is at numbers[2][0], so sum of indices is 2,
              so PUT 6 into the list to return.
        -- 3: It is at numbers[2][1], so sum of indices is 3,
              so do NOT put 3 into the list to return.
        So on this example, bigger_than_indices returns [5, 3, 4, 6]

      ** ASK YOUR INSTRUCTOR FOR HELP **
      ** if this example and the above specification are not clear to you. **
     """
    ###########################################################################
    # TODO: 9. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=""):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
