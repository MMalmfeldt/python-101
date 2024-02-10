#str_value.py

def utf16_value(str_1):
    value = 0
    for let in str_1:
        value += ord(let)
    return value


# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)
