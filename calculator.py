''' calculator.py
    calculator app
    '''

import json

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'MESSAGES' contains the loaded messages as a Python dictionary
    

def prompt(message):
    ''' message styling'''
    print(f'=> {message}')

def invalid_number(num1):
    ''' test if the number is valid'''
    try:
        int(num1)
    except ValueError:
        return True
    return False
global again
again = 'n'

prompt(MESSAGES["welcome"])

while True:
    prompt(MESSAGES["number1"])
    number1 = input()

    while invalid_number(number1):
        prompt('Hmm... that doesn\'t look like a valid number. Try again: ')
        number1 = input()

    prompt(MESSAGES["number2"])
    number2 = input()

    prompt(MESSAGES["operator"])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2': # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3': # 3 represents multiplication
            output = int(number1) * int(number2)
        case '4': # 4 represents division
            output = int(number1) / int(number2)

    prompt(f"The result is: {output}")

    prompt(MESSAGES["again"])
    again = input()
    break
    
