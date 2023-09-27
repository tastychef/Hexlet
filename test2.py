def has_char(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] != char:
            index = index + 1
        return True


print(has_char('Hello', 'q'))
