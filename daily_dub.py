def crunch(str1):
    index = 0
    crunched = ''

    while index < len(str1):
        if index == len(str1) - 1 or str1[index] != str1[index + 1]:
            crunched += str1[index]

        index += 1

    return crunched

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')