import random

def play_game():
    """
    This function plays a number guessing game where the player has to guess a randomly generated number.
    """
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate a random number
    secret_number = random.randint(1, 100)
    
    # Keep track of the number of guesses
    num_guesses = 0
    
    while True:
        # Get a guess from the player
        guess = int(input("Enter your guess: "))
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number in", num_guesses, "guesses.")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()
