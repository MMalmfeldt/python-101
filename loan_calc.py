'''Loan calculator
'''

print("Welcome to this loan calculator, start by entering a loan amount in dollars and cents: ")

while True:
    amount = input()
    try:
        float(amount)
        break
    except ValueError:
        print('Please enter a value in whole dollars or dollars and cents as a decimal: ')

print("Please enter a loan term in months: ")

while True:
    duration = input()
    try:
        int(duration)
        break
    except ValueError:
        print('Please enter a number of months as a number value: ')

print("Please enter an interest rate in the following format, if the interest rate is 5.5%, enter 5.5 : ")
while True:
    int_rate = input()
    try:
        float(int_rate)
        break
    except ValueError:
        print('Please enter an integer or decimal value: ')
mon_int_rate = float(int_rate) / 100 / 12
pymt = float(amount) * (float(mon_int_rate) / (1 - (1 + float(mon_int_rate)) ** (-int(duration))))

final_pmt = '${:,.2f}'.format(pymt)

print(f"Your monthly payment would be {final_pmt}.")
