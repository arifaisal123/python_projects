""" 
Program developed by arifaisal
arifaisal123@gmail.com
"""
from art import *
from random_word import RandomWords
from lives import generate_image
import sys


def main():
    while True:
        # Variables
        life_count = 7
        guess=""
        word = generate_word()
        letters_shown = len(word) * "_"
        
        # Generates welcome message, and rules of game
        welcome_message()

        while True:
            # Prints the current status/ clue of the guess
            print(f"Guessed word: \n{letters_shown}")

            # Generates an image of the life left (hangman)
            print(generate_image(life_count))

            # Takes user guess; re-prompts if the user does not give one single valid letter 
            while True:
                guess = input("Guess a letter: ").lower()
                if len(guess) == 1 and guess.isalpha():
                    break
                else:
                    print("Please type a valid letter!")

            # Generates the output of the guess in a tuple, i.e. ("_pp__", true)        
            guess_output = show_letters(guess, word, letters_shown)

            # Stores the updated word blank list
            letters_shown = guess_output[0]

            # The program will end if all letters ofthe word is guessed, and no more blanks ("_") left
            if "_" not in letters_shown:
                tprint("Congratulations")
                print("You have guessed them all!")
                break

            # Checks if the guess is true or false
            is_guess_correct = guess_output[1]
            
            # Decreases life if guess is not correct
            if not is_guess_correct:
                print("Wrong Guess!")
                life_count -= 1
            else:
                print("Right Guess!")

            # The program ends if life_count gets to zero
            if life_count == 0:
                print((generate_image(life_count)))
                tprint("Game Over!")
                print("You have no more lives left. Better luck next time!")
                print(f"The word is {word}")
                break
        
        while True:
            play_again = input("Do you want to play again? (Type 'Yes' or 'No') ").lower()
            if play_again == "no":
                sys.exit()
            elif play_again == "yes":
                break
            else:
                print("Invalid Input!")


def welcome_message():
    """
    Prints the welcome message, and game rules as string of characters.
    Returns: none
    """
    print("---------------------------------------------------------------------------------------------------------")
    tprint("                       Hangman")
    print("         Welcome to the Game of Hangman! You will have a total of 7 lives to guess the word right.")
    print("---------------------------------------------------------------------------------------------------------")
    print("""
    You need to guess a word of n-th character, randomly generated. On each iteration, you will guess 
    a letter, and the blanks will be updated, if the letter is the correct one. You will win the game
    if you can guess the word right with remaining lives. You will lose the game if you do not have
    any more lives left!
    """)


def generate_word():
    """
    Uses the random_word module, and generates a random English word.
    Return: a word (string)
    """
    r = RandomWords()
    random_word = r.get_random_word()
    return random_word


def show_letters(guessed_letter, generated_word, letter_clue):
    """
    Takes the guessed_letter from the user, and updates the blanks
    Input: All strings
    Returns: string

    Example:
    show_letters("p", "apple", "_____")
    returns "_pp__"
    """
    change = 0

    # Converts string into list
    letter_clue_list = list(letter_clue)

    # Iterates through each letter of the random_word, and checks if matches with the guessed letter
    for i in range(len(generated_word)):
        if generated_word[i] == guessed_letter:
            letter_clue_list[i] = guessed_letter
            change += 1
    if change == 0:
        return ("".join(letter_clue_list), False)
    else:
        return ("".join(letter_clue_list), True)


# Runs the program, if the file is played (not on imports)
if __name__=="__main__":
    main()
