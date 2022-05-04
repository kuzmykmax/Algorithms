from pprint import pprint

import numpy as np

base_array = np.array([39, 99, 64, 92, 63, 94, 42, 20, 11, 20, 78, 96, 48, 29, 33, 30, 38,
       91, 94, 91, 67, 60, 60, 36, 41, 19, 49, 25, 41, 58, 49, 67, 67, 78,
       50, 75, 73, 89, 29, 19, 36,  4, 29, 47, 35, 73,  8, 12, 48, 69, 12,
       76, 20,  5, 72, 49, 59, 31,  9,  5, 76, 96, 26, 96, 63, 55, 32, 27,
       71, 97, 63, 70,  7, 67, 64, 85, 46, 57, 92, 41, 40, 92, 48,  7, 57,
       37, 61, 13, 65, 33, 22, 87, 62, 42, 22, 47, 15, 67, 58, 22])

def task1_ex1():
    print('Max element in array', max(base_array))
    print('Min element in array', min(base_array))
    sorted_array = sorted(base_array)
    print('Sorted array', sorted_array)
    print('Sorted reverse array', sorted(base_array, reverse=True))
    reversed_array = sorted(base_array, reverse=True)
    print(reversed_array)
    pprint(base_array)
    flag = True
    left_list = []
    right_list = []
    for i in sorted_array:
        if flag:
            left_list.append(i)
            flag = False
        else:
            right_list.append(i)
            flag = True

    my_list_max_inside = left_list + sorted(right_list, reverse=True)
    my_list_min_inside = left_list[::-1] + right_list
    print('List min element in the middle')
    print(my_list_min_inside)
    print('List max element in the middle')
    print(my_list_max_inside)


def task4():
    first_set = {10, 2, 33, 4, 5, 6}
    second_set = {4, 5, 6, 7, 8, 11}
    print('Union', first_set.union(second_set))
    print('Intersection', first_set.intersection(second_set))
    print('Dopovnennya', first_set.union(second_set) - first_set)
    print('Difference', first_set.difference(second_set))
    print('Symmetric difference', first_set.symmetric_difference(second_set))


def task1_ex2():
    our_array = base_array.tolist()
    our_list = []
    while True:
        max_elem = max(our_array)
        min_elem = min(our_array)
        if len(our_array) == 1:
            our_list.append(base_array[0])
            break
        our_list.extend([max_elem, min_elem])
        our_array.remove(max_elem)
        our_array.remove(min_elem)
        if len(our_array) == 0:
            break
    print('Task B pairs(max, min)')
    print(our_list)


def task1_exer3():
    even_list = []
    odd_list = []
    for index, value in enumerate(base_array):
        if index % 2 != 0:
            even_list.append(value)
        else:
            odd_list.append(value)
    my_list = sorted(even_list, reverse=True) + sorted(odd_list)
    print('Primary Array', base_array)
    print('Finally Array', my_list)



task1_ex1()
task1_ex2()
task4()
task1_exer3()
