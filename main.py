from guessing_game import guessing_game
from rockPaperScissors import rock_paper_scissors_game

def main():
    '''asks the user which game they would like to play between:
    1 - guessing game or 2 - rock-paper-scissors.
    the loop will keep running until the user chooses to quit.'''
    while True:
        print("\nWhich game would you like to play?")
        print("1. Guessing Game")
        print("2. Rock-paper-scissors")
        print("3. Quit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            guessing_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
