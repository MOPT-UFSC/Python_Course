def my_abs(x):
    if x < 0:
        x = -x
    return x


def my_pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result


def my_gcd(a, b):
    if b == 0:
        return a
    return my_gcd(b, a % b)


def my_sqrt(x, *, max_error=1e-6):
    y = x / 2

    while abs(y * y - x) > max_error:
        y = (y + x / y) / 2

    return y


def my_min_simple(*args):
    current_min = args[0]

    for val in args:
        if val < current_min:
            current_min = val

    return current_min


def my_min(*args, key=None):
    def default_key(x):
        return x

    if key is None:
        key = default_key

    current_min = args[0]

    for val in args:
        if key(val) < key(current_min):
            current_min = val

    return current_min


def my_naive_range(start, end, steps=1):
    sequence = []
    current = start

    while current < end:
        sequence.append(current)
        current += steps

    return sequence


def my_range(start, end=None, steps=1):
    if end is None:
        start, end = 0, start

    current = start
    while current < end:
        yield current
        current += steps


def add_point(x, y, /, z=0, *, merge_coincident=True): ...


if __name__ == "__main__":
    import math
    from random import randint
    import sys

    # naive = my_naive_range(0, 100_000)
    # iterator = my_range(0, 100_000)
    # original = range(0, 100_000)

    # print(sys.getsizeof(naive))
    # print(sys.getsizeof(iterator))
    # print(sys.getsizeof(original))

    # for i in range(0, 100):
    #     a = randint(0, 100)
    #     b = randint(0, 100)
    #     print(math.gcd(a, b), my_gcd(a, b))
    #     assert math.gcd(a, b) == my_gcd(a, b)
