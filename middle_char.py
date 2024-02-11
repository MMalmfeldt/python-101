def center_of(str1):
    len1 = len(str1)
    
    new_str = ''
    if len1 % 2 == 0:
        print(len1)
        mid_even_calc = int((len1-2)/2)
        print(mid_even_calc)
        return str1[(mid_even_calc -1 ):(mid_even_calc + 1)]
    else:
        mid_even_calc = int((len1 - 1) / 2)
        return str1[mid_even_calc]
    
    
print(center_of('I Love Python!!!'))
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True