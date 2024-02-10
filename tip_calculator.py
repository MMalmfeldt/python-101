# tip_calculator.py

the_bill = input('How much was the bill? ')

tip_perc = input('What percentage do you want to tip? ')

just_the_tip = float(the_bill) * (float(tip_perc)/100)

the_total = float(the_bill) + float(just_the_tip)

print(f'Just the tip is: ${just_the_tip}')

print(f'The total is: ${the_total}')

