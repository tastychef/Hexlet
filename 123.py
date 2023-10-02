def squared(n):
    result = 0
    while n > 0:
        last = n % 10
        result += last * last
        n = n // 10
    return result


print(squared(7))
