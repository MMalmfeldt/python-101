# odd_list.py

def oddities(full_list):
    x = full_list[::2]
    return x
#print(oddities([2, 3, 4, 5, 6])) 
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == []) 