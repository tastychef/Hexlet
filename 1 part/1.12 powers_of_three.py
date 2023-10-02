def is_power_of_three(n):
    if n == 1:
        return True
    if n < 1 or n % 3 != 0:
        return False
    return is_power_of_three(n // 3)
