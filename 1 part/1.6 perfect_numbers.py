def is_perfect(num):
    if num > 0:
        return sum([i for i in range(1, num) if num % i == 0]) == num
    else:
        return False


print(is_perfect(-2))
