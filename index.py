import random

print("Welcome to Rock Paper Scissors!")

# Keep playing until the player says no
while True:
    print("----------------------------------")

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
        print("----------------------------------")

        # Check who wins
        if player == computer:
            print("It's a tie!")

        elif player == "rock":
            if computer == "scissors":
                print("You win! Rock beats scissors.")
            else:
                print("You lose! Paper beats rock.")

        elif player == "paper":
            if computer == "rock":
                print("You win! Paper beats rock.")
            else:
                print("You lose! Scissors beats paper.")

        elif player == "scissors":
            if computer == "paper":
                print("You win! Scissors beats paper.")
            else:
                print("You lose! Rock beats scissors.")

    # Ask if they want to play again
    again = input("Do you want to play again? (yes or no): ")

    if again == "no":
        print("Thanks for playing! Goodbye!")
        break  # This stops the loop
