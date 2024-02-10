# multiples_3_5.py

def multisum(num1):
    list_1 = []
    for num in range(1,(num1 + 1)):
        if num % 5 == 0 or num % 3 == 0:  
            list_1.append(num)
            print(list_1)
        else: 
            continue
    print(list_1)
    return sum(list_1)
           

# These examples should all print True
print(multisum(3) == 3) 
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)