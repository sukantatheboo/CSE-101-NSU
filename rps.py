import random  # This is the only library we need (built into Python)

# Initialize scores (just like let userScore = 0; let compScore = 0;)
user_score = 0
comp_score = 0


def gen_cmp_choice():
    """Generates a random choice for the computer."""
    options = ["rock", "paper", "scissors"]
    # random.choice() does exactly what your Math.floor(Math.random() * 3) did
    return random.choice(options)


def play_game():
    """Main game loop holding your JavaScript logic."""
    # We use 'global' here so we can modify the score variables defined outside the function
    global user_score, comp_score

    print("--- Welcome to Rock Paper Scissors ---")

    # The while loop replaces your event listeners, letting you play multiple rounds
    while True:
        # Get user input and convert it to lowercase so it matches our logic exactly
        user_choice = input(
            "Enter rock, paper, or scissors (or type 'quit' to exit): "
        ).lower()

        # A way to break out of the loop
        if user_choice == "quit":
            print(f"\nFinal Score - You: {user_score} | Cmp: {comp_score}")
            print("Thanks for playing!")
            break

        # Check if the user typed a valid option
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.\n")
            continue

        # Get computer choice
        cmp_choice = gen_cmp_choice()
        print(f"Computer chose: {cmp_choice}")

        # --- THIS IS YOUR EXACT LOGIC FROM JAVASCRIPT ---
        if user_choice == cmp_choice:
            print("Game was Draw. Play again:)")
        else:
            user_win = True

            if user_choice == "rock" and cmp_choice == "paper":
                user_win = False
            elif user_choice == "rock" and cmp_choice == "scissors":
                user_win = True
            elif user_choice == "paper" and cmp_choice == "scissors":
                user_win = False
            elif user_choice == "paper" and cmp_choice == "rock":
                user_win = True
            elif user_choice == "scissors" and cmp_choice == "rock":
                user_win = False
            elif user_choice == "scissors" and cmp_choice == "paper":
                user_win = True

            # Determine winner and update score board
            if user_win:
                user_score += 1
                print(f"You Win:^) Your {user_choice} beats {cmp_choice}")
            else:
                comp_score += 1
                print(f"You Lose:| {cmp_choice} beats your {user_choice}")

        # Print the current scoreboard
        print(f"Scoreboard -> You: {user_score} | Cmp: {comp_score}\n")


# Start the game
play_game()
