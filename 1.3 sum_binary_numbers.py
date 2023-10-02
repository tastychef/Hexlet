def binary_sum(num1, num2):
    summ = int(num1, 2) + int(num2, 2)
    a = bin(summ)
    b = a[2:]
    return b