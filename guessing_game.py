import random

def guessing_game():
    '''A random number is selected between 1 and 100. The user has 5 tries to guess the number.
    After each guess, the user will be told if the guess is too low, too high, or correct.
    If the guess is correct, they win.
    If they use all 5 tries without guessing correctly, they lose and the correct number is shown.
    At the end, the user can choose to play again or stop.
    Author: Justin Barros'''
    play_again = 'Y'

    while play_again.upper() == 'Y':
        secret_number = random.randint(1, 100)
        tries_left = 5

        print("I'm thinking of a number between 1 and 100.")
        guess = int(input(f"Guess what it is. You have {tries_left} tries: "))

        while tries_left > 1:
            if guess == secret_number:
                print("You got it!")
                break
            elif guess < secret_number:
                tries_left -= 1
                guess = int(input(f"Nope! Too low. Try again ({tries_left} {'try' if tries_left == 1 else 'tries'} left): "))
            else:
                tries_left -= 1
                guess = int(input(f"Nope! Too high. Try again ({tries_left} {'try' if tries_left == 1 else 'tries'} left): "))

        else:
            if guess == secret_number:
                print("You got it!")
            else:
                print(f"Nope! You lost. The number was {secret_number}")

        play_again = input("Do you want to play again? (Y/N): ")
