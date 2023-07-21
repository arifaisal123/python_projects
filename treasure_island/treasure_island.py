# Display initial message on the screen
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Take user input for level 1
level_1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()

# When user input is "left"
if level_1 == "left":
    # Take user input for level 2
    level_2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    # When user input is "wait"
    if level_2 == "wait":
        # Take user input for level 3
        level_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? ").lower()
        # When user input is "yellow"
        if level_3 == "yellow":
            print("You Win!")
        # When user input is "red"
        elif level_3 == "red":
            print("Burned by fire. Game Over.")
        # When user input is "blue"
        elif level_3 == "blue":
            print("Eaten by beasts. Game Over.")
        # When user input is not "yellow", "red" or "blue"
        else:
            print("Game Over.")
    # When user input is not "wait"
    else:
        print("Attacked by trout. Game Over.")
# When user input is not "left"
else:
    print("Fall into a hole. Game Over.")
