from libs import *
from random import randint
from art import tprint


# Store functions as dictionary values
libs_store = {
    1: macdonald,
    2: be_kind,
    3: hakuna_matata,
    4: fortune_cookies,
    5: jack_and_jill,
    6: harry_potter
}


# Main functionality
def main():
    # Display welcome message to the screen
    welcome_message()

    # Generate a random number between 1 and 6 inclusive
    random_libs_num = randint(1, 6)

    # Store the function randomly selected from libs_store dictionary
    libs_func = libs_store[random_libs_num]

    # Call the randomly selected function
    libs_func()


# Display welcome message
def welcome_message():
    print("---------------- Welcome to ----------------")
    tprint("MadLibs")
    print("Please follow the on-screen instructions.")


# When the program is run, main function is called
if __name__=="__main__":
    main()
