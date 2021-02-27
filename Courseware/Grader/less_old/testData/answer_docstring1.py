
#-----------------------------------------------------------------------
# Students: READ and RUN this program.  There is nothing else for you
#           to do in here. But DO study these examples carefully,
#           and refer back to them as necessary.
#-----------------------------------------------------------------------


def main():
    
    classic_example_1(3, 9)
    classic_example_2(4)
    classic_example_3(5, 9)


def foo1():  # blah blah
    # blah blah
    pass
def foo2():
    
    print('hi')

def foo3():
    
    print('hi')









def classic_example_1(n, m):
    
    #-------------------------------------------------------------------
    # Classic nested-loops, type 1:
    #    The number of inner-loop iterations does NOT depend
    #    on the current value of the outer-loop variable.
    #-------------------------------------------------------------------
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
    
    #-------------------------------------------------------------------
    # Classic nested-loops, type 2:
    #    The number of inner-loop iterations DOES depend
    #    on the current value of the outer-loop variable.
    #-------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    header = 'Partial multiplication table for 1 x 1 through'
    print(header, n, 'x', n)
    print('-----------------------------------------------------------')

    for i in range(n):  # The ONLY difference from the previous
        for j in range(i + 1):  # example is   i+1   on this line.
            print(i + 1, j + 1, '=', (i + 1) * (j + 1))
        print()


def classic_example_3(n, m):
    
    #-------------------------------------------------------------------
    # Same as classic example 1, but shows how to keep successive
    # print statements on the same line, then go to the next line.
    #-------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    
    header = 'Complete multiplication table for 1 x 1 through'
    print(header, n, 'x', m)
    print('but with just products shown')
    print('-----------------------------------------------------------')

#     for i in range(n):
#         for j in range(m):
#             print((i + 1) * (j + 1), end=' ')
#         print()

    for i in range(n):
        for j in range(m):
            print((i + 1) * (j + 1), end=' ')
        print()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
