def fizz_buzz(begin, end):
    result = []
    for number in range(begin, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(number))
    return (result)
