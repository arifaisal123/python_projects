# Inspired by Al Sweigart's project "Bagels" https://inventwithpython.com/bigbookpython/
"""
The game takes an 3-digit user input for digits. Based on the inputs, the game tells if the user 
has given correct input or not. The user will get maximum 10 guesses to get towards the correct answer!
"""
# Imports random module for the game
import random


# Declares constant variables
NUM_DIGITS = 3
MAX_GUESSES = 10


# Main game function
def main():
    while True:
        # Prints out game rules for the user
        game_rules()
        
        # Generate NUM_DIGITS secret number
        secret_num = generate_secret_num()
        
        # Variables for guesses
        num_of_guesses = 0
        remaining_guesses = MAX_GUESSES - num_of_guesses

        # Main Game Logic
        while True:
            if remaining_guesses <= 1:
                print(f"You have {remaining_guesses} guess left!")
            else:
                print(f"You have {remaining_guesses} guesses left!")
            
            # Asks the user for guessing 
            while True:
                # Stores the user's guess, and strips off any whitespaces
                guess = input("Please choose your guess: ").strip()

                # If the number of digits entered is incorrect, then the program re-prompts the user
                if len(guess) != NUM_DIGITS:
                    print(f"Please guess a {NUM_DIGITS}-digit number!")
                
                # If the user gives alphabet as input, then the program re-prompts the user
                elif not guess.isdigit():
                    print("Please enter digits only!")
                
                # If the user correctly provides the input, then the guess is stored, and no. of guesses is reduced by 1
                else:
                    remaining_guesses -= 1
                    break

            # Evaluates the guess given by the user, and displays to the user
            eval_guess(guess, secret_num)

            # Checks if the guess matches with the secret number
            if guess == secret_num:
                print("Congrats! You have got the answer right!")
                break
            elif remaining_guesses > 0:
                print("Please try again!")
            else:
                print(f"Game Over! The correct answer is {secret_num}. Better luck next time!")
                break
        
        # Prompts the user for playing the game
        game_restart = input("Do you want to play again? Type Y for Yes or N for No. ")
        if game_restart == "N":
            break
    return


# Prints out game rules for the user
def game_rules():
    print(f"""
    Welcome to the game of the intellects- Yay or Nay!
    In this game, you need to guess a number of {NUM_DIGITS} digits. 
    But remember, the digits can also have a leading 0.
    
    Based on your answer, you will be given clues per below:
    
    Displayed Text                        Meaning of the Text
         Yay               You have 1 digit correctly guessed in the right position.
         Goo               You have 1 digit correctly guessed, but not in the right position.
         Nay               You have no digit correctly guessed.
         
    You will have a total of {MAX_GUESSES} guesses to get towards the correct answer.
    
    Can you do it?
    
    Let's Play!
    """)
    return


# Generate NUM_DIGITS secret number
def generate_secret_num():
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Shuffles the position of the numbers in num_list
    random.shuffle(num_list)
    secret_digits = ""
    i = 0

    # The loop will continue till all the secret digits are entered
    while len(secret_digits) != NUM_DIGITS:
        secret_digits += str(num_list[i])
        i += 1

    return secret_digits    


# Evaluates the guess given by the user
def eval_guess(str, secret_num):
    clues = []

    # Checks the user input, and matches with game rule
    for i in range(len(str)):
        if str[i] == secret_num[i]:
            clues.append("Yay")
        elif str[i] in secret_num:
            clues.append("Goo")
        
    if len(clues) == 0:
        clues.append("Nay")

    # Returns the clues in sorted order
    for clue in sorted(clues):
        print(clue, end= " ")
    print()
    return


# When the whole program is called, the main function runs
if __name__ == "__main__":
    main()
