"""

|---------------------     Rock- Paper- Scissor Game     ---------------------|

"""

"""
Developed by arifaisal123

"""

"""

  i. Firstly, the game takes input from the user about the number of games to 
     be played. The total number of games can be 3, 5 or 7.
    
 ii. After taking the user input, the game prints out the number of games left 
     to be played. It subsequently asks the user for input for Rock, Paper, or 
     Scissor. After playing the game, the program prints out the number of 
     games left to be played, the score for the user, and the machine, and 
     prompting for the next user input. It will continue till the number of 
     games equal to 3, 5, or 7 as it was in the user input at the first.
    
iii. After the user input for rock, paper, or scissor, the program will check 
     the gameLogic function to decide who is the winner of that particular 
     match. It can have three results- user winner, draw, or machine winner.
     
 iv. After gameLogic, the program enters the pointCalc function to calculate 
     the point scored based on the match, and refreshes to the new score.
     
  v. After pointCalc function, the program will enter gameCounter function in 
     order to increase the match count. It will end the game once it matches 
     the total number of games to be played. When the program ends, it will 
     print out the winner, and score.

"""

import random

totalGameNum = 0
gameNum = 0
user_points = 0
machine_points = 0
user_input = ""
machine_input = ""

def startGame():
    
    """ 
    Takes user input for the number of games to be played.
    
    Returns: None.
    
    """

    global totalGameNum
    while True:
        user_input_totalGameNum = str(input("How many games you want to play? Enter 3, 5 or 7: "))
        if user_input_totalGameNum == "3":
            totalGameNum = 3
            break
        elif user_input_totalGameNum == "5":
            totalGameNum = 5
            break
        elif user_input_totalGameNum == "7":
            totalGameNum = 7
            break
        else:
            continue
        
def gameCounter():
    
    """
    Inreases the gameNum counter by 1 till the end of the game
    
    Returns: gameOver
    
    """
    global gameNum
    global totalGameNum
    
    if gameNum <= totalGameNum:
        gameNum += 1
    else:
        return gameOver    
        
def gameLogic():
    
    """
    Checks the logic before awarding the points to user or machine
    
    Returns: Winner of the particular game
    
    """
    
    if user_input == "rock":
        if machine_input == "scissor":
            return "user_winner"
        elif machine_input == "rock":
            return "draw"
        elif machine_input == "paper":
            return "machine_winner"
    
    if user_input == "paper":
        if machine_input == "scissor":
            return "machine_winner"
        elif machine_input == "rock":
            return "user_winner"
        elif machine_input == "paper":
            return "draw"
        
    if user_input == "scissor":
        if machine_input == "scissor":
            return "draw"
        elif machine_input == "rock":
            return "machine_winner"
        elif machine_input == "paper":
            return "user_winner"
        
def pointCalc(gameLogic):
    
    """ 
    Increases the point of the user or machine by 1
    
    Returns: updates the points of the players
    
    """
    global user_points 
    global machine_points 
    
    if gameLogic == "user_winner":
        user_points += 1
        return user_points
    elif gameLogic == "machine_winner":
        machine_points += 1
        return machine_points
    else:
        return None
        
def playGame():
    
    """
    Continues the game sequence.
    
    Takes user input of rock, paper, or scissor.
    
    """
    
    global user_input
    global machine_input
    global gameNum
    global totalGameNum
    global user_points
    global machine_points
    
    rps_list = ["rock", "paper", "scissor"]

    while gameNum < totalGameNum:
        user_input = str(input("Enter rock, paper, or scissor? ")).lower()
        machine_input = random.choice(rps_list)
        print("----------------------------------------")
        print("You entered:", user_input)
        print("Machine entered:", machine_input)
        print("----------------------------------------")
        if gameLogic() == "user_winner":
            print("Great! You just got 1 point.")
        elif gameLogic() == "machine_winner":
            print("Your opponent just got 1 point.")
        elif gameLogic() == "draw":
            print("It is a draw!")            
        pointCalc(gameLogic())
        print("----------------------------------------")
        print("Total Score: ")
        print("You =", user_points, "Computer =", machine_points)
        gameCounter()
        print("----------------------------------------")
        print("Total ", totalGameNum - gameNum, "Games left!")
        print("----------------------------------------")
        
    if user_points > machine_points:
        print("Congratulations! You are the winner!")
    elif user_points < machine_points:
        print("Alas! You have lost! Better luck next time!")
    elif user_points == machine_points:
        print("It is a DRAW!")    
                
def gameOver():
    
    """
    Checks if the total number of games has reached the expected level.
    
    Returns: printed output --> Game Over. Game Results. Players' Points.
    
    """
    
    if gameCounter() == gameOver:
        print("Game Over!")
        if user_points > machine_points:
            print("Result: Congratulations! You are the winner!")
            print(user_points)
            print(machine_points)
        elif user_points < machine_points:
            print("Result: You have lost. Better luck next time!")
            print(user_points)
            print(machine_points)
        elif user_points == machine_points:
            print("Result: Draw!")
            print(user_points)
            print(machine_points)
      
# Initiating Game        
startGame()
playGame()
    