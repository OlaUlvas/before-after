from data import first, against, logo
from data import happenings
import os
import random

def get_random_account():
    '''get data from random account.'''
    return random.choice(happenings)

def check_answer(guess, a_year, b_year):
    if a_year < b_year:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(first)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_b["year"] == account_a["year"]:
            account_b = get_random_account()

        print("Vilken händelse inträffade först?\n")
        print(f"A. {account_a['name']}\n")
        print("or\n")
        print(f"B. {account_b['name']}\n")
        user_input = input("Type 'A' or 'B': ").lower()
        account_a_year = account_a["year"]
        account_b_year = account_b["year"]
        is_correct = check_answer(user_input,account_a_year, account_b_year)

        print(logo)
        os.system('clear')


        if is_correct:
            score += 1
            print(f"You're right. Current score is: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()