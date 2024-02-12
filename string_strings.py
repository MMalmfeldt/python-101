
def stringy(num1):
    if num1 == 1:
       return '1' 
    elif num1 % 2 == 0:
       return '10' * (int(num1/2))
    elif num1 % 2 != 0 and num1 != 1:
       return '10' * int((num1/2)) + '1'
  





print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
print(stringy(1))