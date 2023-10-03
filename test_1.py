from math import sqrt


def get_square_roots(num):
    ls = []
    a = sqrt(num)
    ls.extend(a, abs(a))
    return ls


print(get_square_roots(9))
