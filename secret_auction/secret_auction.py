import os
from art import *

# Store name of the bidder and bid amount
bid_records = {}

# Main functionality of the program
def main():
    # Display logo on the screen
    print(logo)

    # Continue loop until highest bidder is declared
    while True:
        # Record bidder name and bid amount
        record_new_bid()

        # Check for any more bidders
        has_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")

        # If there are more bidders in the auction
        if has_bidder == "yes":
            # Clear the messages in the console
            clear_console()
        # If no more bidder is available
        elif has_bidder == "no":
            # Clear the messages in the console
            clear_console()
            # Declare the highest bidder from bid records
            declare_highest_bidder()
            # Close the program
            exit()
            
# Record new bid in the bid_records
def record_new_bid():
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bid_records[name] = bid_amount

# Clear the messages in the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loop through the bid_records dictionary and declare the highest bidder
def declare_highest_bidder():
    # Loop through the key, value pair in bid_records dictionary
    for key, value in bid_records.items():
        # Check if the current value in the dictionary is maximum or not
        if value == max(bid_records.values()):
            # Display the winner of the auction
            print(f"The winner is {key} with a bid of ${value}.")

# When the program is run, main function is called
if __name__=="__main__":
    main()
