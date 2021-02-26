"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler, and many others before him.  February, 2014.
"""







def main():
    """ Calls the other functions to demonstrate them. """
    classic_example_1(3, 9)
    classic_example_2(4)
    classic_example_3(5, 9)


def foo1():  
    
    pass
def foo2():
    """ testing
    a funny commment """
    print('hi')

def foo3():
    """
    testing
    a funny commment """
    print('hi')

""" Testing this """
''' And this too '''
"""
"""

""" ''' xxxx """

''' xxx """ '''

def classic_example_1(n, m):
    """
    Prints a multiplication table for numbers from 1 to n multiplied
    by numbers from 1 to m, where n and m are the given parameters.

    Preconditions: n and m are positive integers.
    """
    
    
    
    
    
    print()
    print('-----------------------------------------------------------')
    header = 'Complete multiplication table for 1 x 1 through'
    print(header, n, 'x', m)
    print('-----------------------------------------------------------')

    for i in range(n):
        for j in range(m):
            print(i + 1, j + 1, '=', (i + 1) * (j + 1))
        print()


def classic_example_2(n):
    """
    Prints PART of a multiplication table.
    Precondition: n is a positive integer.
    """
    
    
    
    
    
    print()
    print('-----------------------------------------------------------')
    header = 'Partial multiplication table for 1 x 1 through'
    print(header, n, 'x', n)
    print('-----------------------------------------------------------')

    for i in range(n):  
        for j in range(i + 1):  
            print(i + 1, j + 1, '=', (i + 1) * (j + 1))
        print()


def classic_example_3(n, m):
    """
    Prints a multiplication table for numbers from 1 to n multiplied
    by numbers from 1 to m, where n and m are the given parameters.
    Prints only the products (unlike classic example 1),
    and prints each "chunk" of the table on a single row.

    Preconditions: n and m are positive integers.
    """
    
    
    
    
    print()
    print('-----------------------------------------------------------')
    """ Right in the middle
        of a wasteland.
        """
    header = 'Complete multiplication table for 1 x 1 through'
    print(header, n, 'x', m)
    print('but with just products shown')
    print('-----------------------------------------------------------')






    for i in range(n):
        for j in range(m):
            print((i + 1) * (j + 1), end=' ')
        print()





if __name__ == '__main__':
    main()
