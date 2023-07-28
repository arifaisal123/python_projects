from art import logo
from random import randint

# Main game functionality
def main():
    # Display game logo on the screen
    print(logo)

    # Display welcome message
    print("Welcome to the Number Guessing Game!")

    # Store the number of attempts based on easy or hard difficulty
    TOTAL_ATTEMPTS = set_difficulty()

    # Start the game
    start_game(TOTAL_ATTEMPTS)


def set_difficulty():
    """
    Take user input for game difficulty, and return the total number
    of attempts based on that.
    """
    # Continue the loop till the user gives a valid input
    while True:
        # User input for easy (10 guesses) or hard difficulty (5 guesses)
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

        # Set number of attempts based on difficulty chosen by user
        if difficulty == "easy":
            number_of_attempts = 10
            break
        elif difficulty == "hard":
            number_of_attempts = 5
            break
        else:
            print("Invalid input!")

    return number_of_attempts


def start_game(TOTAL_ATTEMPTS):
    """
    Start the game, and continue till the user gets the correct
    answer or runs out of guesses.
    """
    # Variable for counting attempts made
    attempt_counter = 0
    
    # Store a random number between 1 and 100 inclusive
    random_guess = randint(1, 100)

    # Continue game loop till the user gets the correct answer or runs out of guesses
    while attempt_counter <= TOTAL_ATTEMPTS:
        # Store the number of guesses remaining
        guesses_remaining = TOTAL_ATTEMPTS - attempt_counter

        # Display the number of guesses remaining
        print(f"You have {guesses_remaining} attempts remaining to guess the number.")
        
        # Increase attempt counter by 1 after each guess
        attempt_counter += 1

        # Take user input for guess
        current_guess = int(input("Make a guess: "))

        # If the current user guess is low than the random guess
        if current_guess < random_guess:
            print("Too low.")
            print("Guess again.")
        # If the current user guess is high than the random guess
        elif current_guess > random_guess:
            print("Too high.")
            print("Guess again.")
        # If the current user guess matches with the random guess
        elif current_guess == random_guess:
            print(f"You got it! The answer was {random_guess}.")
            exit()
    
    # Display message when user runs out of guesses
    print("You have run out of guesses, you lose.")

# When the program is run, main function is called
if __name__=="__main__":
    main()
    