import random

print("Welcome to Rock Paper Scissors!")
player_score = 0
computer_score = 0

# Keep playing until the player says no
while True:
    print("(-------------(< _ >)----------------)")

    # Ask the player for their choice
    player = input("Enter rock, paper, or scissors: ")

    # Check if the input is valid
    if player != "rock" and player != "paper" and player != "scissors":
        print("That's not a valid choice! Please type rock, paper, or scissors.")

    else:
        # Computer picks a random choice
        computer = random.choice(["rock", "paper", "scissors"])

        print("You chose:", player)
        print("Computer chose:", computer)

        # Check who wins
        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win! Rock beats scissors.")
            player_score = player_score + 1
        elif player == "paper" and computer == "rock":
            print("You win! Paper beats rock.")
            player_score = player_score + 1
        elif player == "scissors" and computer == "paper":
            print("You win! Scissors beats paper.")
            player_score = player_score + 1
        else:
            print("Computer wins!")
            computer_score = computer_score + 1

    # Ask if they want to play again
    again = input("Wanna play again? (yes or no): ")

    if again == 'no':
        print("-------------(< _ >)------------------")
        print("Game over!")
        print("Your score:", player_score)
        print("Computer score:", computer_score)
        print("He he he, Nice move boss")
        break  # This stops the loop
