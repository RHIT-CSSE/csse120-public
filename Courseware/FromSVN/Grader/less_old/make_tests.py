"""
<describe what this module has/does>

Created on Sep 23, 2016.
Written by: david.
"""

TESTFILE = 'problem1.py'

def main():
    """ Calls the   TEST   functions in this module. """
    make_tests()


def make_tests():
    with open(TESTFILE, 'r') as f:
        lines = f.read().split('\n')

    for line in lines:
        if line.startswith('def test_'):
            function = line.split('_')[1].split('(')[0]
            print('@', TESTFILE, function)
        if line.strip().startswith('expected'):
            expected = line.split()[2]
        if line.strip().startswith('answer'):
            start_index = line.index('(') + 1
            end_index = len(line) - 1
            answer = line[start_index:end_index]
            print('[' + answer + ']')
            print(expected)
            print()


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
