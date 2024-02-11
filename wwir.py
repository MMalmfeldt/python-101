your_age = input('What is your age? ')
ret_age = input('At what age would you like to retire? ')
time_diff = int(ret_age) - int(your_age)
ret_year = 2024 + time_diff
print(f"It's 2024. You will retire in {ret_year}.\nYou have only {ret_year} years of work to go!")