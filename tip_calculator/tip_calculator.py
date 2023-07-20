# Display the welcome message
print("Welcome to the tip calculator.")

# Take user input for total bill
total_bill = float(input("What was the total bill? $"))

# Take user input for tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Split the bill to X number of people
bill_split = int(input("How many people to split the bill? "))

# Calculate total tip
total_tip = total_bill * (tip_percentage / 100)

# Calculate total bill including tip
total_bill_with_tip = total_bill + total_tip

# Calculate individual bill rounded off to 2 decimal places
individual_bill = round(total_bill_with_tip / bill_split, 2)

# Display the individual bill to be paid
print(f"Each person should pay: ${individual_bill}")
