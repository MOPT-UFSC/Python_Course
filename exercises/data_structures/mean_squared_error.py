from random import randint 


def create_random_list(n: int):
    random_list = []
    for i in range(n):
        random_list.append(randint(0, 100))
    return random_list


def mean_squared_error(list1: list, list2: list):
    total_error = 0
    size = len(list1)

    for i in range(size):
        value_error = list1[i] - list2[i]
        total_error += value_error ** 2

    return total_error
