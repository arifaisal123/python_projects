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