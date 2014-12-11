#Lab 15, Problem 1
#Jeremy Fransen, Shawn McBrayer, Maria Genitempo, Chris Smith

# Rules: If on the first roll, the sum of the dice is 7 or 11, the player wins.  If the sum is 2, 3, or, 12, the player loses.  
# Otherwise, the player will continue to roll until they match the previous score.  If they roll a 7, they lose.

import random

def craps():

  isInGame = true
  winningNums = [7, 11]
  losingNums = [2, 3, 12]
  
  while isInGame == true:
  
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
  
    score = die1 + die2
  
    if score in winningNums:
      showInformation("You rolled a " + str(score) + ".  You win!")
      isInGame = false
  
    elif score in losingNums:
      showInformation("You rolled a " + str(score) + ".  You lose!")
      isInGame = false    
   
    else: 
      showInformation("You rolled a " + str(score) + ".")
      point = score
      score = 0
    
      while score != 7 and score != point:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        score = die1 + die2
        showInformation("You rolled a " + str(score) + ".")
      
      if score == 7:
        showInformation("You rolled a 7.  You lose!")
        isInGame = false
      
      else:
        showInformation("You rolled a " + str(score) + ".  You win!")
        isInGame = false
    