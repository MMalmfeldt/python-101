

def clean_up(str1):
    new_str = ''

    for idx, char in enumerate(str1):
        if char.isalpha():
            new_str += char
        elif idx == 0 or new_str[-1] != ' ':
            new_str += ' '

    return new_str

print(clean_up("---what's my +*& line?") == " what s my line ")
# True