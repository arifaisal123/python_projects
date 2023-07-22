import random

# Game art variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Game choices for players
options = [rock, paper, scissors]

# Take and display user input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(options[user_input])

# Take and display computer input
computer_input = random.randint(0, 2)
print("Computer chose:")
print(options[computer_input])

# Game Logic
if user_input == computer_input:
    print("Game draw!")
elif user_input == 0 and computer_input == 1:
    print("You lose!")
elif user_input == 0 and computer_input == 2:
    print("You win!")
elif user_input == 1 and computer_input == 0:
    print("You win!")
elif user_input == 1 and computer_input == 2:
    print("You lose!")
elif user_input == 2 and computer_input == 0:
    print("You lose!")
elif user_input == 2 and computer_input == 1:
    print("You win!")