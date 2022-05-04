from pprint import pprint

import numpy as np

basic_array = np.random.randint(100, size=(10, 10))
#pprint(basic_array)


def task_a():
    print("Max element in array", np.max(basic_array))
    print("Min element in array", np.min(basic_array))

    for row in basic_array:
        for elem in row:
            print(elem, end=" ")
        print(end="\n")


def task_b():
    for row in range(len(basic_array)):
        # print(basic_array[0])
        for elem in range(len(basic_array[0])):
            print(basic_array[elem][row], end=" ")
        print(end="\n")


# def task_b():
#     for row in range(len(basic_array)):
#         # print(basic_array[0])
#         for elem in range(len(basic_array[0])):
#             print(basic_array[elem][row], end=" ")
#         print(end="\n")



def spiralPrint(m, n, a):
    k = 0
    l = 0
    """ k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator """

    while k < m and l < n:

        # Print the first row from  the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
        print()
        k += 1
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        print()
        n -= 1
        if k < m:

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
        print()
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1
        print()


def spiralPrintCenter(m, n, a):
    k = 3
    l = 0
    """ k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator """

    while k < m and l < n:

        # Print the first row from  the remaining rows
        for i in range(l, n):
            print(a[i][l], end=" ")
        print()
        #k -=1
        for i in range(1,k+1):
            print(a[k][i], end=" ")
        print()
        n -= 1
        if k < m:
            for i in range(n - 1, (k - 1), -1):
                print(a[n - 1][i], end=" ")
            n -= 1
        print()
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1
        print()



def task_e():
    for number, rows in enumerate(basic_array):
        if number % 2 == 0:
            print(rows)
        else:
            print(list(reversed(rows)))


def task3(size):
    our_array = np.random.randint(20, size=(size,size,size))
    pprint(our_array)
    array_3d= our_array.flatten()

    print(min(array_3d))
    print(max(array_3d))
    print('OX axis:')
    print(np.sort(our_array,0))
    print('OY axis:')
    print(np.sort(our_array, 1))
    print('OZ axis:')
    print(np.sort(our_array, 2))


# pprint(basic_array)
#
# print('task A')
# task_a()
# print('Task b')
# task_b()
# print('Task Spiral')
# spiralPrint(10,10, basic_array)
# print('Task e')
# task_e()

print('Task 3')
task3(5)