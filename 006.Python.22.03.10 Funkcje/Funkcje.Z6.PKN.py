# Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

import random

def get_computer_action():
    possible_actions = ["r", "p", "s"]
    action = random.choice(possible_actions)
    return action

def get_user_action():
    action = input("enter a choice (rock - r, paper - p, scissors - s, end = end): ")
    return action


def is_tie(user, computer):
    return user == computer

def user_wins(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    else:
        return False


def main():

    number_of_rounds = input("How many times do you wont to play: ")
    number_of_rounds = int(number_of_rounds)

    for i in range(0, number_of_rounds):
        computer_action = get_computer_action()
        user_action = get_user_action()
    if user_action.lower() == 'end':


    if user_action not in ("r", "p", "s", "end"):
        print('Error - Bye, Bye')
        break

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if is_tie(user_action, computer_action):
        print(f"Both players selected {user_action}, It's tie!")
    if user_wins(user_action, computer_action):
        print(f"User winns! -> {user_action} " > {computer_action})
    else:
        print(f"Computer wins! -> {computer_action} > {user_action}")
        break
    print('Koniec')

    # i program nie działa???!!!!

