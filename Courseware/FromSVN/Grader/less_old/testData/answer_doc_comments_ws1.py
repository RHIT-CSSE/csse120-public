def main():
    classic_example_1(3, 9)
    classic_example_2(4)
    classic_example_3(5, 9)
def foo1():  
    pass
def foo2():
    print('hi')
def foo3():
    print('hi')
def classic_example_1(n, m):
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
    print()
    print('-----------------------------------------------------------')
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