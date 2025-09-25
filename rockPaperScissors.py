import random

def rock_paper_scissors_game():
  '''The computer will generate a random number from 1 - 3 and will ask the user to choose a number. Depending on the combination of the random number generated and the number the user chose, the program will decide on who won of if it is a tie.'''

player_score = 0
computer_score = 0

while True:
        player_choice = int(input("Enter your choice (1.rock, 2.paper, 3.scissors 4. quit "))

        

        if player_choice == 4:
            break
        elif player_choice == 1:
            choice = "rock"
        elif player_choice == 2:
            choice = "paper"
        elif player_choice == 3:
            choice = "scissors"

        else:
            print("Invalid choice. Please enter 1, 2, or 3")
            continue

        # Simulate computer's choice 
        computer_num = random.randint(1, 3)
        if computer_num == 1:
            computer_choice = "rock"
        elif computer_num == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"

        print(f"You chose: {choice}")
        print(f"Computer chose: {computer_choice}")

        if choice == computer_choice:
            print("It's a tie!")
        elif (choice == "rock" and computer_choice == "scissors") or \
             (choice == "paper" and computer_choice == "rock") or \
             (choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Scores: Player: {player_score}, Computer: {computer_score}\n")

print(f"Final Scores: Player: {player_score}, Computer: {computer_score}")
print("Thanks for playing!")

