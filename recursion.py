import os


def n_exp_m(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    n = n * (n_exp_m(n, m - 1))
    return n


def sum_of_digits(number):
    if number < 0:
        number = -number
    if number == 0:
        return 0
    sum = number % 10 + sum_of_digits(number // 10)
    return sum


def len_of_list(my_list):
    if not my_list:
        return 0
    if my_list:
        my_list.pop(0)
        return 1 + len_of_list(my_list)


def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] != word[-1]:
        return False
    is_palindrome(word[1: len(word) - 1])
    return True


def print_even_numb_from_list(my_list):
    if not my_list:
        return
    if my_list[0] % 2 == 0:
        print(my_list[0], end=' ')
    print_even_numb_from_list(my_list[1:])


def print_even_index_list(my_list):
    if not my_list:
        return
    print(my_list[0], end=' ')
    print_even_index_list(my_list[2:])


def second_max_in_list(my_list):
    if len(my_list) < 2:
        return None
    max_list = my_list[0]
    second_max_list = my_list[1]
    if my_list[1] > my_list[0]:
        max_list = my_list[1]
        second_max_list = my_list[0]

    def second_max(max, second, list):
        if not list:
            return max, second, list

        if list[0] >= max:
            second = max
            max = list[0]
        elif list[0] > second:
            second = list[0]
        list = list[1:]
        return second_max(max, second, list)

    return second_max(max_list, second_max_list, my_list[2:])[1]


def walk_directory(path):
    for i in os.listdir(path):
        if os.path.isfile(path + '\\' + i):
            print(i)
        elif os.path.isdir(path + '\\' + i):
            walk_directory(path + '\\' + i)

