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
localPath = ""

# global sounds
glass = ()
gunshot = ()
necksnap = ()
punchSound = ()
room = ()
secret = ()

# global pictures
roomPic = ()
player = ()
arctic = ()
egypt = ()
grandcanyon = ()
ocean = ()
rome = ()
sanfran = ()
tajmahal = ()
colt = ()
eye = ()
kali = ()
boom = ()
powPic = ()
zap = ()

########################
def chromaKey(player, location):
  #replace a green screen background with
  
  foreground = duplicatePicture(player)
  background = duplicatePicture(location)
  pixel = getPixel(foreground, 0, 0)
  colorGreen = getColor(pixel)
  for x in range(0, getWidth(foreground)):
    for y in range(0, getHeight(foreground)):
      pixel = getPixel(foreground, x, y)
      pixel2 = getPixel(background, x, y)
      color = getColor(pixel)
      color2 = getColor(pixel2)
      if distance(color, colorGreen) < 60:
        setColor(pixel, color2)
  return(foreground)

########################
# choose sounds
def picSound(localPath):
  """Pick and Make a sound"""
  global glass
  global gunshot
  global necksnap
  global punch
  global portal
  global secret
   
  
  glass = os.path.abspath(localPath + "/sounds/boss/glassbrk.wav")
  glass = makeSound(glass)
  
  gunshot = os.path.abspath(localPath + "/sounds/boss/gunshot.wav")
  gunshot = makeSound(gunshot)
  
  necksnap = os.path.abspath(localPath + "/sounds/boss/necksnap.wav")
  necksnap = makeSound(necksnap)
  
  punch = os.path.abspath(localPath + "/sounds/boss/punch.wav")
  punch = makeSound(punch)
  
  portal = os.path.abspath(localPath + "/sounds/room/portal.wav")
  portal = makeSound(portal)  
  
  secret = os.path.abspath(localPath + "/sounds/secret/secret.wav")
  secret = makeSound(secret)
  
########################
# choose pictures

def picPic(localPath):
  #Load all pictures to be used in the game
  
  global player
  global arctic
  global egypt
  global grandcanyon
  global ocean
  global rome
  global sanfran
  global tajmahal
  global colt
  global eye
  global kali
  global boom
  global powPic
  global zap
  
  player = os.path.abspath(localPath + "/image/char/solo.jpg")
  player = makePicture(player)
  
  arctic = os.path.abspath(localPath + "/image/room/arctic.jpg")
  arctic = makePicture(arctic)
 
  egypt = os.path.abspath(localPath + "/image/room/egypt.jpg")
  egypt = makePicture(egypt)
  
  grandcanyon = os.path.abspath(localPath + "/image/room/grandcanyon.jpg")
  grandcanyon = makePicture(grandcanyon)
  
  ocean = os.path.abspath(localPath + "/image/room/ocean.jpg")
  ocean = makePicture(ocean)
  
  rome = os.path.abspath(localPath + "/image/room/rome.jpg")
  rome = makePicture(rome)

  sanfran = os.path.abspath(localPath + "/image/room/sanfran.jpg")
  sanfran = makePicture(sanfran)
  
  tajmahal = os.path.abspath(localPath + "/image/room/tajmahal.jpg")
  tajmahal = makePicture(tajmahal)
  
  colt = os.path.abspath(localPath + "/image/secret/colt.jpg")
  colt = makePicture(colt)
  
  eye = os.path.abspath(localPath + "/image/secret/eye.jpg")
  eye = makePicture(eye)
  
  kali = os.path.abspath(localPath + "/image/secret/kali.jpg")
  kali = makePicture(kali)
  
  boom = os.path.abspath(localPath + "/image/boss/boom.jpg")
  boom = makePicture(boom)
  
  powPic = os.path.abspath(localPath + "/image/boss/pow.jpg")
  powPic = makePicture(powPic)

  zap = os.path.abspath(localPath + "/image/boss/zap.jpg")
  zap = makePicture(zap)
 

########################
# welcome message
def welcome():
  global localPath
  showInformation("Please select \"assets\" as your directory.")
  localPath = setMediaFolder()
  
  global userName
  
  userName = requestString("Please enter your name")
  while userName == "":
    userName = requestString("Please enter a valid name")
  
  showInformation("Welcome, " + userName)
  
  #init sound and pictures
  picSound(localPath)
  picPic(localPath)
  
  
  showInformation("In each room you will be told which directions you can go.")
  showInformation("You'll be able to go north, south, east or west by typing that direction.")
  showInformation("To display heatlh stats, enter \"health\".")
  showInformation("To display your current inventory, enter \"inventory\".")
  showInformation("To repeat the room description enter \"room\".")  
  showInformation("Type help to redisplay this introduction.")
  showInformation("Type exit to quit at any time.")
  

def map():
  if "map" in items:
    showInformation(""" 
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
def inventory():
  s = "Your inventory: "
  numBullets = items.count("bullet")
  if len(items) == 0:
    showInformation("You have nothing in your inventory.")
  else:
   for i in items:
    if i == 'bullet':
      s += ""
    else:
      s += i + ", "
  if numBullets == 0:
    s = s[0:len(s)-2]
    showInformation(s)
  elif numBullets == 1:
    s += str(numBullets) + " bullet"
    showInformation(s)
  else:
    s += str(numBullets) + " bullets"
    showInformation(s)
                 
########################
# room 1
# golden gate

def startingRoom():
  global sanfran
  global player
  global roomPic
  
  roomPic = chromaKey(player, sanfran)
  repaint(roomPic)
  
  weAreHere = 0
  
  # print description
  room = "You are in the starting room. There is a chest you can \"open\" in the corner..."
  showInformation(room)
  # print directions
  directions = "You can only go south to room 2"
  showInformation(directions)
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      weAreHere = 1
      global quitGame
      quitGame = 1
    elif userInput == "help":
      welcome()
      showInformation("")
      userInput = requestString("Please enter a choice")
    elif userInput == "room":
      showInformation(room)
      showInformation(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "inventory":
      inventory()
    elif userInput == "open":
      global items
      global secret     
      if 'map' not in items:       
        items.append('map')
        play(secret)
        showInformation("You found the map! You can view it by entering \"map\".")
      else:
        showInformation("There is nothing here.")
      userInput = requestString("Please enter a choice.")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "south":
      weAreHere = 1
      room2()
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")
   
########################
# room 2
# grand canyon

def room2():
  global portal
  global player
  global grandcanyon
  global roomPic
  
  play(portal)
  
  roomPic = chromaKey(player, grandcanyon)
  repaint(roomPic)
  
  weAreHere = 0
  
  # print description
  room = "You enter Room2 its under constuction debris is everywhere..."
  showInformation(room)
  # print directions
  directions = "You can go \"back\" \"east\" or \"south\""
  showInformation(directions)
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
      showInformation("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      showInformation(room)
      showInformation(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "inventory":
      inventory()
    elif userInput == "back":
      play(portal)
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
      showInformation("Your health =" + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")

########################
# room 3
# colosseum

def room3():
  weAreHere = 0
  global portal
  play(portal)
  
  # print description
  room = "You enter Room3 all the windows are boarded up..."
  showInformation(room)
  # print directions
  directions = "You can go \"back\"\"
  showInformation(directions)
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
      showInformation("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      showInformation(room)
      showInformation(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "inventory":
      inventory()
    elif userInput == "back":
      weAreHere = 1
      room2()
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    else:
      userInput = requestString("Please enter a valid choice!")
      
########################
# room 4
# ocean

def room4():
  weAreHere = 0
  global portal
  play(portal)
  
  # print description
  room = "You arrive at the Ocean there is an odd chest you can \"look\" at or you can go for a \"swim\"..."
  showInformation(room)
  # print directions
  directions = "You can go \"back\" \"north\" or \"east\""
  showInformation(directions)
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
      showInformation("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      showInformation(room)
      showInformation(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "inventory":
      inventory()
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
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")  
    else:
      userInput = requestString("Please enter a valid choice!")

########################
# room 5
# arctic

def room5():
  weAreHere = 0
  global portal
  play(portal)
  
  # print description
  room = "You enter Room5 the door slams shut behind you...a scary guy blocks your path"
  showInformation(room)
  bossFight()
  
########################
# secret room
# pyramid

def secretRoom():
  weAreHere = 0
  global portal
  play(portal)
  
  # print description
  room = "You enter a Secret Room from the bookcase in the center of the room you see a Gun you can  \"grab\" ..."
  showInformation(room)
  # print directions
  directions = "There are no other exits You can only go \"back\""
  showInformation(directions)
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
      showInformation("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      showInformation(room)
      showInformation(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "inventory":
      inventory()
    elif userInput == "back":
      weAreHere = 1
      room4()
    elif userInput == "grab":
      global items
      global secret
      if 'gun' not in items:
        play(secret)
        items.append('gun')
        for b in range(0, 6):
          items.append('bullet')
        showInformation("You grabbed it! Hope you wont need to use the \"gun\".")
      else:
        showInformation("There is nothing here.")
      userInput = requestString("Please enter a choice.")
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
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
  global portal
  play(portal)
  
  # print description
  room = "You find yourself at the tajmahal there is a miniture statue you can \"grab\"..."
  showInformation(room)
  # print directions
  directions = "There are no other exits You can only go \"back\""
  showInformation(directions)
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
      showInformation("")
      userInput = requestString("Please enter a valid choice!")
    elif userInput == "room":
      showInformation(room)
      showInformation(directions)
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "back":
      weAreHere = 1
      room4()
    elif userInput == "grab":
      global items
      global secret
      if 'idol' not in items:
        play(secret)
        items.append('idol')
        showInformation("You grabbed it! your health has been increased.")
        global myHealth
        myHealth += 50
      else:
        showInformation("There is nothing here.")
      userInput = requestString("Please enter a choice.")
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Please Enter a choice.")
    elif userInput == "inventory":
      inventory()
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
      showInformation(directions)
      userInput = requestString("Please enter a choice:")
      if userInput == "exit":
        weAreHere = 1
        quitGame = 1
      elif userInput == "gun":
        if "gun" in items:
          result = useGun()
          showInformation(result)
          if "Hit" in result:
            bossHealth -= 10
        else:
          showInformation("You don't have a gun!")
      elif userInput == "punch":
        result = punch()
        showInformation(result)
        if "Hit" in result:
          bossHealth -= 5
      elif userInput == "health":
        showInformation("Your health = " + str(myHealth))
        showInformation("Boss's health = " + str(bossHealth))    
      elif userInput == "inventory":
        inventory()
      else:
        userInput = requestString("Please enter a valid choice")
      if (userInput == 'gun' or userInput == 'punch') and bossHealth > 0 :
        i = random.random()
        if int(i * 100) >= 80:
          showInformation("Boss has hit you")
          myHealth -= 5
        else:
          showInformation("Boss swings and misses")
 
  if myHealth > 0:
    showInformation("You killed the boss.  Congratulations!")
    quitGame = 1
  else:
    showInformation("You are dead")
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
    showInformation("You awake in a dark room there is yelling in the distance...")
    startingRoom()

  # goodbye message
  showInformation("Thanks for playing " + userName)
  quit
     


