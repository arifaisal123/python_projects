"""
Developed by: Arif Faisal (arifaisal123@gmail.com)
This is a basic calculator with 7 features, as mentioned.
More features will be added in the future, if there is an upgraded release.
"""
# Imports math library
from math import *


# Main function of the program
def main():
    # The program will continue, until the users enters 'no' while prompted
    while True:
        # Prints the calculator usage technique for the user 
        info()
        
        # The loop will continue until the user enters a valid number
        while True:
            try:
                number = int(input("Please choose a feature(1-7): "))
                if number >= 1 and number <=7:
                    break
                else:
                    print("Please select a valid number!")
            except:
                print("Only integers are allowed!")
        
        # Checks the logic, and print answer
        answer = logic(number)
        print(f"The answer is: {answer}")
        
        # Prompts the user if they want to continue using calculator
        re_prompt = input("Do you want to continue using calculator? (Enter any key to continue or 'No' to quit!)")
        if re_prompt.lower() == "no":
            break


# Prints the calculator usage technique
def info():
    print("This is a basic calculator with the following features.")
    print(
        "Please select the number, associated with the feature that you want to use, and press Enter."
    )
    print(
        """
        1 - Addition
        2 - Subtraction
        3 - Multiplication
        4 - Division
        5 - Exponent
        6 - Square Root
        7 - Cube Root
    """
    )


# Adds two numbers
def addition():
    x = int(input("Please select a number for addition: "))
    y = int(input("Please select another number: "))
    return x + y


# Subtracts two numbers
def subtraction():
    x = int(input("Please select a number for subtraction: "))
    y = int(input("Please select another number: "))
    return x - y


# Multiplies two numbers
def multiplication():
    x = int(input("Please select a number for multiplication: "))
    y = int(input("Please select another number: "))
    return x * y


# Divides one number by another
def division():
    x = int(input("Please select a number for division: "))
    y = int(input("Please select another number: "))
    return x / y


# Returns x to the power of y
def exponent():
    x = int(input("Please select a base number: "))
    y = int(input("Please select the power: "))
    return x**y


# Returns square root of a number
def square_root():
    x = int(input("Please select a number for square root: "))
    return sqrt(x)


# Returns cube root of a number
def cube_root():
    x = int(input("Please select a number for cube root: "))
    return cbrt(x)


# Checks the logic, and returns the value
def logic(number):
    if number == 1:
        return addition()
    elif number == 2:
        return subtraction()
    elif number == 3:
        return multiplication()
    elif number == 4:
        return division()
    elif number == 5:
        return exponent()
    elif number == 6:
        return square_root()
    elif number == 7:
        return cube_root()


# If the program is called, then main() code is executed, and not on imports
if __name__ == "__main__":
    main()
