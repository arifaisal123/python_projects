import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Display welcome message
print("Welcome to the PyPassword Generator!")

# Ask user input for total letters
pg_letters= int(input("How many letters would you like in your password?\n")) 

# Ask user input for total symbols
pg_symbols = int(input(f"How many symbols would you like?\n"))

# Ask user input for total numbers
pg_numbers = int(input(f"How many numbers would you like?\n"))

generated_password = []

# Pick a random letter from list and append it to generated_password list
for _ in range(pg_letters):
    random_letter = random.choice(letters)
    generated_password.append(random_letter)

# Pick a random symbol from list and append it to generated_password list
for _ in range(pg_symbols):
    random_symbol = random.choice(symbols)
    generated_password.append(random_symbol)

# Pick a random number from list and append it to generated_password list
for _ in range(pg_numbers):
    random_number = random.choice(numbers)
    generated_password.append(random_number)

# Shuffle the elements of the generated_password  list
random.shuffle(generated_password)

# Convert the generated password list to string
shuffled_password = "".join(generated_password)

# Display the shuffled password
print(f"Here is your password: {shuffled_password}")
