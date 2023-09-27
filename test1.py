def filter_string(text, sym):
    result = ''
    for char in text:
        if char.lower() != sym.lower():
            result += char

    return result.strip()


print(filter_string('     I love you     ', 'w'))
