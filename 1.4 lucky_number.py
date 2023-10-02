def sum_of_square_digits(n):
    return sum(int(x) ** 2 for x in str(n))


def is_happy_number(n):
    visited = set()
    while True:
        if n == 1:
            return True

        n = sum_of_square_digits(n)

        if n in visited:
            return False

        visited.add(n)

print(is_happy_number(7))
