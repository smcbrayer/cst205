# Game
# start game with game()

# lab 11 strategy game
#You should display a welcome message when the game starts. 
#If the user types help at any time, you should redisplay the welcome message
#If the user types exit at any time they should be able to quit the game
#In each room, you should:
#Print a description of the room
#Give the user the directions that they are allowed to move
#Ask the user (via requestString) which direction they would like to go
#Process the answer and respond accordingly

import random
# needed for getting current working directory
import os


########################
# Global variables

quitGame = 0
items = []
bossHealth = 50
myHealth = 50
userName = ""


########################
# welcome message
def welcome():
  global userName
  userName = requestString("Please enter your name")
  
  showInformation("Welcome, " + userName)
  printNow("\nIn each room you will be told which directions you can go.")
  printNow("You'll be able to go north, south, east or west by typing that direction.")
  printNow("To display heatlh stats, enter \"health\".")
  printNow("To repeat the room description enter \"room\".")  
  printNow("Type help to redisplay this introduction.")
  printNow("Type exit to quit at any time.\n")

def map():
  if "map" in items:
    printNow(""" 
                 N
               W   E
                 S
                 _______
                |_Start_|
                 _|_____     _________
                |_room2_| -  |_room3_|
                 _|_____      ______
         (S)-   |_room4_| -  |_boss_|\n""")
    return
              
               
########################
# room 1
# golden gate

def startingRoom():
  weAreHere = 0
  printNow("\n-----------------\n")
  # print description
  room = "You are in the starting room. There is a chest you can \"open\" in the corner..."
  printNow(room)
  # print directions
  directions = "\nYou can only go south to room2\n"
  printNow(directions)
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      weAreHere = 1
      global quitGame
      quitGame = 1
    elif userInput == "help":
      welcome()
      printNow("")
      userInput = requestString("Please enter a choice")
    elif userInput == "room":
      printNow(room)
      printNow(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "open":
      global items
      if 'map' not in items:       
        items.append('map')
        printNow("You found the map! You can view it by entering \"map\".")
      else:
        printNow("There is nothing here.")
      userInput = requestString("Please enter a choice.")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "south":
      weAreHere = 1
      room2()
    elif userInput == "health":
      global myHealth
      printNow("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")
   
########################
# room 2
# grand canyon

def room2():
  weAreHere = 0
  printNow("\n-----------------\n")
  # print description
  room = "You enter Room2 its under constuction debris is everywhere..."
  printNow(room)
  # print directions
  directions = "You can go \"back\" \"east\" or \"south\"\n"
  printNow(directions)
  # get user input
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      welcome()
      printNow("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      printNow(room)
      printNow(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "back":
      weAreHere = 1
      startingRoom()
    elif userInput == "east":
      weAreHere = 1
      room3()
    elif userInput == "south":
      weAreHere = 1
      room4()
    elif userInput == "health":
      global myHealth
      printNow("Your health =" + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")

########################
# room 3
# colosseum

def room3():
  weAreHere = 0
  printNow("\n-----------------\n")
  # print description
  room = "You enter Room3 all the windows are boarded up..."
  printNow(room)
  # print directions
  directions = "You can go \"back\"\n"
  printNow(directions)
  # get user input
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      welcome()
      printNow("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      printNow(room)
      printNow(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "back":
      weAreHere = 1
      room2()
    elif userInput == "health":
      global myHealth
      printNow("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")
      
########################
# room 4
# ocean

def room4():
  weAreHere = 0
  printNow("\n-----------------\n")
  # print description
  room = "You arrive at the Ocean there is an odd chest you can \"look\" at or you can go for a \"swim\"..."
  printNow(room)
  # print directions
  directions = "You can go \"back\" \"north\" or \"east\" \n"
  printNow(directions)
  # get user input
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      welcome()
      printNow("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      printNow(room)
      printNow(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "back":
      weAreHere = 1
      room2()
    elif userInput == "east":
      weAreHere = 1
      room5()
    elif userInput == "north":
      weAreHere = 1
      room2()
    elif userInput == "swim":
      weAreHere = 1
      room6()
    elif userInput == "look":
      weAreHere = 1
      secretRoom()
    elif userInput == "health":
      global myHealth
      printNow("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")  
    else:
      userInput = requestString("Please enter a valid choice!")

########################
# room 5
# arctic

def room5():
  weAreHere = 0
  printNow("\n-----------------\n")
  # print description
  room = "You enter Room5 the door slams shut behind you...a scary guy blocks your path"
  printNow(room)
  bossFight()
  
########################
# secret room
# pyramid

def secretRoom():
  weAreHere = 0
  printNow("\n-----------------\n")
  # print description
  room = "You enter a Secret Room from the bookcase in the center of the room you see a Gun you can  \"grab\" ..."
  printNow(room)
  # print directions
  directions = "There are no other exits You can only go \"back\"\n"
  printNow(directions)
  # get user input
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      welcome()
      printNow("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      printNow(room)
      printNow(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "back":
      weAreHere = 1
      room4()
    elif userInput == "grab":
      global items
      if 'gun' not in items:
        items.append('gun')
        for b in range(0, 6):
          items.append('bullet')
        printNow("You grabbed it! Hope you wont need to use the \"gun\".")
      else:
        printNow("There is nothing here.")
      userInput = requestString("Please enter a choice.")
    elif userInput == "health":
      global myHealth
      printNow("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")

########################
# second secret room secret room
# tajmahal
# reasure chest or underground cave from room 4 (ocean)
# magic whirlpool

def room6():
  weAreHere = 0
  printNow("\n-----------------\n")
  # print description
  room = "You find yourself at the tajmahal there is a miniture statue you can \"grab\"..."
  printNow(room)
  # print directions
  directions = "There are no other exits You can only go \"back\"\n"
  printNow(directions)
  # get user input
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      welcome()
      printNow("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      printNow(room)
      printNow(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "back":
      weAreHere = 1
      room4()
    elif userInput == "grab":
      global items
      if 'idol' not in items:
        items.append('idol')
        printNow("You grabbed it! your health has been increased.")
        global myHealth
        myHealth += 50
      else:
        printNow("There is nothing here.")
      userInput = requestString("Please enter a choice.")
    elif userInput == "health":
      global myHealth
      printNow("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")            


########################
#use gun
def useGun():
  global items
  numBullets = items.count('bullet')
  if numBullets > 0:
    items.remove('bullet')
    i = random.random()
    score = int(i * 100)
    if score <= 75:
      return 'Hit!'
    else:
      return 'You missed!'
  else:
    return 'You are out of bullets'
    

########################
#boss fight
def bossFight():
  global bossHealth
  global myHealth
  global quitGame
  global items
  weAreHere = 0
  while weAreHere == 0:
    if bossHealth == 0 or myHealth == 0:
      weAreHere = 1
    else:
      directions = "You can use your \"gun\" or \"punch\"."
      printNow(directions)
      userInput = requestString("Please enter a choice:")
      if userInput == "exit":
        weAreHere = 1
        quitGame = 1
      elif userInput == "gun":
        if "gun" in items:
          result = useGun()
          printNow(result)
          if "Hit" in result:
            bossHealth -= 10
        else:
          printNow("You don't have a gun!")
      elif userInput == "punch":
        result = punch()
        printNow(result)
        if "Hit" in result:
          bossHealth -= 5
      elif userInput == "health":
        printNow("Your health = " + str(myHealth))
        printNow("Boss's health = " + str(bossHealth))    
      else:
        userInput = requestString("Please enter a valid choice")
      if (userInput == 'gun' or userInput == 'punch') and bossHealth > 0 :
        i = random.random()
        if int(i * 100) >= 80:
          printNow("Boss has hit you")
          myHealth -= 5
        else:
          printNow("Boss swings and misses")
 
  if myHealth > 0:
    printNow("You killed the boss.  Congratulations!")
    quitGame = 1
  else:
    printNow("You are dead")
    quitGame = 1
    
  
########################
#punch
def punch():
  i = random.random()
  if int(i * 100) < 85 :
    return "Hit!"
  else:
    return "Missed"  

  
########################
# main game
def game():
  # display Welcome message
  welcome()
  global quitGame
  quitGame = 0
  while quitGame == 0:
    printNow("You awake in a dark room there is yelling in the distance...")
    startingRoom()

  # goodbye message
  showInformation("Thanks for playing " + userName)
  quit
     


