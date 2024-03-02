''' Rock, Paper Scissors
'''
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'Spock', 'lizard']
OTHER_VALID_CHOICES = ['r', 's', 'p', 'S', 'l']

gg_w_counter = 0
bg_w_counter = 0

def prompt(message):
    '''for styling only'''
    print(f"==> {message}")

def display_winner(mc, cc):
    '''determines and displays winner'''
    if ((mc == "rock" and cc == "scissors" or cc == "lizard") or
        (mc == "paper" and cc == "rock" or cc ==  "spock") or
        (mc == "scissors" and cc == "paper" or cc == "lizard") or
        (mc == "lizard" and cc == "paper" or cc == "spock") or
        (mc == "spock" and cc == "rock" or cc == "scissors")):
        global gg_w_counter
        gg_w_counter += 1
        prompt("You win!")
    elif ((mc == "rock" and cc == "paper" or cc == "spock") or
        (mc == "paper" and cc == "scissors" or cc == "lizard") or
        (mc == "scissors" and cc == "rock" or cc == "spock") or
        (mc == "spock" and cc == "paper" or cc ==  "lizard") or
        (mc == "lizard" and cc == "rock" or cc == "scissors")):
        global bg_w_counter
        bg_w_counter += 1
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one (or enter first letter): {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in (VALID_CHOICES + OTHER_VALID_CHOICES):
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}")

    display_winner(choice, computer_choice)

    print(bg_w_counter)
    print(gg_w_counter)

    if gg_w_counter == 3:
        print("Good guy is the first to 3 wins!")
        break
    if bg_w_counter == 3:
        print("Bad guy is the first to 3 wins!")
        break

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break
