def xor(num1, num2):
    if (num1 == True and num2 == False) or (num1 == False and num2 == True):
         return True
    else:
         return False
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
print(xor(0, 0))
print(xor(0, 5))
print(xor(5, 5))