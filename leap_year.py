# leap_year.py

def is_leap_year(my_year):
    if (my_year == int(my_year)) and (my_year > 0):
        if my_year % 400 == 0 or (my_year % 4 == 0 and my_year % 100 != 0):
            return True
        else:
            return False
    else:
        print('You did not include a valid argument.')      


# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
print(is_leap_year('2025'))