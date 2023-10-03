from math import sqrt


def get_square_roots(num):
    if num == 0:
        return [0]
    elif num < 0:
        return []
    else:
        return [sqrt(num)]


print(get_square_roots(9))
