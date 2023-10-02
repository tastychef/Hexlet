#Это задание не связано напрямую с уроком, это просто еще одно полезное упражнение по работе с функциями.
#Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку с разницей в возрасте в виде The age difference is 11.
HEX
def get_age_difference(year_one, year_two):
    difference = abs(year_one - year_two)
    return f"The age difference is {difference}"
MY_1
def dif_age(y1, y2):
    result = str(abs(y1 - y2))
    result2 = "The age difference is " + result
    return result2
MY_2
def dif_age(y1, y2):
    result = abs(y1 - y2)
    return f"The age difference is {result}"

# Реализуйте функцию has_char(). Она должна проверять, содержит ли строка указанную букву (вне зависимости от регистра). Функция принимает два параметра:
# Строка
# Буква для поиска
# И возвращает результат проверки – булево значение.
MY
def has_char(string, char):
    index = 0
    while index < len(string):
        if string[index] == (char.upper() or char.lower()):
            return True
        index += 1
    return False
HEX
def has_char(string, char):
    index = 0
    uppercase_char = char.upper()
    while index < len(string):
        if string[index].upper() == uppercase_char:
            return True
        index += 1
    return False

#Реализуйте функцию binary_sum(), которая принимает на вход два двоичных числа в виде строк и возвращает их сумму. Вычисленная сумма также должна быть бинарным числом в виде строки:
def binary_sum(num1, num2):
    summ = int(num1, 2) + int(num2, 2)
    a = bin(summ)
    b = a[2:]
    return b
