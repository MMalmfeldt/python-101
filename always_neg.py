def negative(num1):
    if num1 > 0:
        return -(num1)
    else:
        return num1
    
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True