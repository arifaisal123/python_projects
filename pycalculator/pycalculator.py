import os
from art import *

# Main Functionality
def main():
    # Display the program logo
    print(logo)

    # Initiate calculator operations
    use_calculator()


# Add two numbers
def add(x1, x2):
    """
    Take two numbers as input, and return their addition as output 
    """
    return x1 + x2

# Subtract two numbers
def subtract(x1, x2):
    """
    Take two numbers as input, and return their subtraction as output 
    """
    return x1 - x2

# Multiply two numbers
def multiply(x1, x2):
    """
    Take two numbers as input, and return their multiplication as output 
    """
    return x1 * x2

# Divide two numbers
def divide(x1, x2):
    """
    Take two numbers as input, and return their division as output 
    """
    return x1 / x2

# Dictionary of operators
calc_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Calculator functionality
def use_calculator():
    should_continue = True
    first_num = int(input("What's the first number?: "))

    while should_continue:
        # Iterate through the operators' dictionary
        for operator in calc_operations:
            print(operator)

        operation_symbol = input("Pick an operation from the line above: ")
        next_num = int(input("What's the next number?: "))
        
        # Store the function name from operators' dictionary
        calculation_function = calc_operations[operation_symbol]

        # Use relevant function to calculate the numbers
        answer = calculation_function(first_num, next_num)

        # Display the calculation result
        print(f"{first_num} {operation_symbol} {next_num} = {answer}")

        # Take user input for continuing calculation
        user_input = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'CTRL + C' to exit: ").lower()

        # If user wants to continue with current calculation
        if user_input == "y":
            first_num = answer
        # If user wants to start a fresh calculation
        elif user_input == "n":
            should_continue = False
            # Clear the messages on the console screen
            clear_screen()
            use_calculator()


def clear_screen():
    # For Windows
    if os.name == 'nt':  
        os.system('cls')
    # For Unix/Linux/MacOS
    else:  
        os.system('clear')

# If the program is run, the main function is called
if __name__=="__main__":
    main()
