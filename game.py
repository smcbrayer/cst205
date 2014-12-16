###################################################
# CorpsOfFour
# Final Game
# Written by:
#  Shawn McBrayer
#  Jeremy Fransen
#  Chris Smith
#  Maria Genitempo


# Final Game
# The game will begin after you hit load program.

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
mapImage = ()
mapSanFran = ()
mapGrandCanyon = ()
mapRome = ()
mapAtlantis = ()
mapArctic = ()
mapSecretWest = ()
mapSecretSouth = ()
currentRoom = ()

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
  global punchSound
  global portal
  global secret
   
  
  glass = os.path.abspath(localPath + "/sounds/boss/glassbrk.wav")
  glass = makeSound(glass)
  
  gunshot = os.path.abspath(localPath + "/sounds/boss/gunshot.wav")
  gunshot = makeSound(gunshot)
  
  necksnap = os.path.abspath(localPath + "/sounds/boss/necksnap.wav")
  necksnap = makeSound(necksnap)
  
  punchSound = os.path.abspath(localPath + "/sounds/boss/punch.wav")
  punchSound = makeSound(punchSound)
  
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
  global mapImage
  global mapSanFran
  global mapGrandCanyon
  global mapRome
  global mapAtlantis
  global mapArctic
  global mapSecretWest
  global mapSecretSouth
  
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
  
  mapImage = os.path.abspath(localPath + "/image/map/map.jpg")
  mapImage = makePicture(mapImage)
  
  mapSanFran = os.path.abspath(localPath + "/image/map/map_sanfran.jpg")
  mapSanFran = makePicture(mapSanFran)
  
  mapGrandCanyon = os.path.abspath(localPath + "/image/map/map_grandcanyon.jpg")
  mapGrandCanyon = makePicture(mapGrandCanyon)
  
  mapRome = os.path.abspath(localPath + "/image/map/map_rome.jpg")
  mapRome = makePicture(mapRome)
  
  mapAtlantis = os.path.abspath(localPath + "/image/map/map_atlantis.jpg")
  mapAtlantis = makePicture(mapAtlantis)
  
  mapArctic = os.path.abspath(localPath + "/image/map/map_arctic.jpg")
  mapArctic = makePicture(mapArctic)
  
  mapSecretWest = os.path.abspath(localPath + "/image/map/map_secretwest.jpg")
  mapSecretWest = makePicture(mapSecretWest)
  
  mapSecretSouth = os.path.abspath(localPath + "/image/map/map_secretsouth.jpg")
  mapSecretSouth = makePicture(mapSecretSouth)
 

########################
# welcome message
def welcome():
  global localPath
  global userName
  showInformation("""
WORLDS OF WONDER ADVENTURE GAME\n  
_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,\n
""")

  if localPath == "":
    showInformation("Before you start the game, please select the \"assets\" folder as your directory.")
    localPath = setMediaFolder()
  
  
  if userName == "":
    userName = requestString("Hello traveler, what is your name?")
    while userName == "":
      userName = requestString("Please enter a valid name")
  
    showInformation("Welcome, " + userName + ".")
  
  #init sound and pictures
  picSound(localPath)
  picPic(localPath)
  
  
  showInformation("In each room you will be told which directions you can go.")
  showInformation("You'll be able to go north, south, east or west by typing that direction.")
  showInformation("It can take some time to travel through the portals, so please be patient.")
  showInformation("To avoid any confusion, please close any open image or map in between teleportations.")
  showInformation("To display health stats, type \"health\".")
  showInformation("To display your current inventory, enter \"inventory\".")
  showInformation("If you forget where you are, type \"room\".")  
  showInformation("Type \"help\" to open the help menu.")
  showInformation("Type \"exit\" to end your adventure at any time.")

def helpMenu():
  showInformation("You'll be able to go north, south, east or west by typing that direction. " +
                  "(It can take some time to travel through the portals, so please be patient.) " +
                  "To display health stats, type \"health\". " +
                  "To display your current inventory, enter \"inventory\". " +
                  "If you forget where you are, type \"room\". " +  
                  "Type \"help\" to open the help menu. " +
                  "Type \"exit\" to end your adventure at any time.")

def map():
  global currentRoom
  if currentRoom == 'San Francisco':
    show(mapSanFran)
  elif currentRoom == 'Grand Canyon':
    show(mapGrandCanyon)
  elif currentRoom == 'Rome':
    show(mapRome)
  elif currentRoom == 'Atlantis':
    show(mapAtlantis)
  elif currentRoom == 'Arctic':
    show(mapArctic)
  elif currentRoom == 'Secret West':
    show(mapSecretWest)
  elif currentRoom == 'Secret South':
    show(mapSecretSouth)
  else:
    show(mapImage)

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
  if numBullets == 0 and len(items) > 0:
    s = s[0:len(s)-2]
    showInformation(s)
  elif numBullets == 1:
    s += str(numBullets) + " bullet"
    showInformation(s)
  elif numBullets > 0:
    s += str(numBullets) + " bullets"
    showInformation(s)
               
########################
# room 1
# golden gate

def startingRoom():
  global sanfran
  global player
  global roomPic
  global currentRoom
  
  currentRoom = 'San Francisco'
  
  roomPic = chromaKey(player, sanfran)
  repaint(roomPic)
  
  weAreHere = 0
  
  # print description
  showInformation("You look around the rocky beach... an old chest lies in the sand...")
  # print directions
  showInformation("To the south, there is a portal.")
  userInput = requestString("Would you like to: \n" +
                            "\"open\" the chest\n" +
                            "go \"south\"")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      weAreHere = 1
      global quitGame
      quitGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                                "\"open\" the chest\n" +
                                "go \"south\"")
    elif userInput == "room":
      showInformation("You are currently in " + currentRoom + ".")
      userInput = requestString("Would you like to: \n" +
                                "\"open\" the chest\n" +
                                "go \"south\"")
    elif userInput == "inventory":
      inventory()
      userInput = requestString("Would you like to: \n" +
                                "\"open\" the chest\n" +
                                "go \"south\"")
    elif userInput == "open":
      global items
      global secret     
      if 'map' not in items:       
        items.append('map')
        play(secret)
        showInformation("You found the map! You can view it anytime by typing \"map\".")
      else:
        showInformation("There is nothing here.")
      userInput = requestString("Would you like to: \n" +
                                "\"open\" the chest\n" +
                                "go \"south\"")
    elif userInput == "map":
      if 'map' not in items:
        showInformation("You do not have a map.")
      else:
        map()
      userInput = requestString("Would you like to: \n" +
                                "\"open\" the chest\n" +
                                "go \"south\"")
    elif userInput == "south":
      weAreHere = 1
      room2()
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Would you like to: \n" +
                                "\"open\" the chest\n" +
                                "go \"south\"")
    else:
      userInput = requestString("Please enter a valid choice!\n" +
                                "Would you like to: \n" +
                                "\"open\" the chest\n" +
                                "go \"south\"")
   
########################
# room 2
# grand canyon

def room2():
  global portal
  global player
  global grandcanyon
  global roomPic
  global currentRoom
  
  currentRoom = 'Grand Canyon'
  
  play(portal)
  
  roomPic = chromaKey(player, grandcanyon)
  repaint(roomPic)
  
  weAreHere = 0
  
  # print description
  showInformation("You were teleported to the Grand Canyon.\n" +
                  "(... be careful, it's a long way down...)")
  # print directions
  showInformation("You see portals to the east and south.")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "go \"east\"\n" +
                            "go \"south\"\n" +
                            "go \"back\"")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                                "go \"east\"\n" +
                                "go \"south\"\n" +
                                "go \"back\"")
    elif userInput == "room":
      showInformation("You are currently in " + currentRoom + ".")
      userInput = requestString("Would you like to: \n" +
                                "go \"east\"\n" +
                                "go \"south\"\n" +
                                "go \"back\"")
    elif userInput == "map":
      map()
      userInput = requestString("Would you like to: \n" +
                                "go \"east\"\n" +
                                "go \"south\"\n" +
                                "go \"back\"")
    elif userInput == "inventory":
      inventory()
      userInput = requestString("Would you like to: \n" +
                                "go \"east\"\n" +
                                "go \"south\"\n" +
                                "go \"back\"")
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
      userInput = requestString("Would you like to: \n" +
                                "go \"east\"\n" +
                                "go \"south\"\n" +
                                "go \"back\"")
    else:
      userInput = requestString("Please enter a valid choice!\n" +
                                "Would you like to: \n" +
                                "go \"east\"\n" +
                                "go \"south\"\n" +
                                "go \"back\"")

########################
# room 3
# colosseum

def room3():
  global player
  global rome
  global portal
  global roomPic
  global currentRoom
  
  currentRoom = 'Rome'
  
  weAreHere = 0
   
  play(portal)  
  
  roomPic = chromaKey(player, rome)
  repaint(roomPic)

  # print description
  showInformation("You were teleported to Rome...")
  # print directions
  showInformation("You've reached a dead end.\n" +
                  "You must go \"back\".")
  # get user input
  userInput = requestString("Please enter a choice: ")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Please enter a choice: ")
    elif userInput == "room":
      showInformation("You are currently in " + currentRoom + ".")
      userInput = requestString("Please enter a choice: ")
    elif userInput == "map":
      map()
      userInput = requestString("Please enter a choice.")
    elif userInput == "inventory":
      inventory()
      userInput = requestString("Please enter a choice: ")
    elif userInput == "back":
      weAreHere = 1
      room2()
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Please enter a choice:")
    else:
      userInput = requestString("Please enter a valid choice!")
      
########################
# room 4
# ocean

def room4():

  global player
  global ocean
  global portal
  global roomPic
  global currentRoom
  
  currentRoom = 'Atlantis'

  weAreHere = 0
  
  play(portal)  
  
  roomPic = chromaKey(player, ocean)
  repaint(roomPic)
  
  # print description
  showInformation("You were teleported to Atlantis.\n" +
                  "There is a treasure chest!")
  # print directions
  showInformation("Also, you see a portal to the east.")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "\"look\" in the treasure chest\n" +
                            "go for a \"swim\"\n" +
                            "go \"east\"\n" +
                            "go \"back\"")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                                "\"look\" in the treasure chest\n" +
                                "go for a \"swim\"\n" +
                                "go \"east\"\n" +
                                "go \"back\"")
    elif userInput == "room":
      showInformation("You are currently in " + currentRoom + ".")
      userInput = requestString("Would you like to: \n" +
                                "\"look\" in the treasure chest\n" +
                                "go for a \"swim\"\n" +
                                "go \"east\"\n" +
                                "go \"back\"")
    elif userInput == "map":
      map()
      userInput = requestString("Would you like to: \n" +
                                "\"look\" in the treasure chest\n" +
                                "go for a \"swim\"\n" +
                                "go \"east\"\n" +
                                "go \"back\"")
    elif userInput == "inventory":
      inventory()
      userInput = requestString("Would you like to: \n" +
                                "\"look\" in the treasure chest\n" +
                                "go for a \"swim\"\n" +
                                "go \"east\"\n" +
                                "go \"back\"")
    elif userInput == "back":
      weAreHere = 1
      room2()
    elif userInput == "east":
      weAreHere = 1
      room5()
    elif userInput == "swim":
      weAreHere = 1
      room6()
    elif userInput == "look":
      weAreHere = 1
      secretRoom()
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Would you like to: \n" +
                                "\"look\" in the treasure chest\n" +
                                "go for a \"swim\"\n" +
                                "go \"east\"\n" +
                                "go \"back\"") 
    else:
      userInput = requestString("Please enter a valid choice!\n" +
                                "Would you like to: \n" +
                                "\"look\" in the treasure chest\n" +
                                "go for a \"swim\"\n" +
                                "go \"east\"\n" +
                                "go \"back\"")

########################
# room 5
# arctic

def room5():
  
  global player
  global arctic
  global portal
  global currentRoom
  
  currentRoom = 'Arctic'
  
  weAreHere = 0
  
  play(portal)  
  
  roomPic = chromaKey(player, arctic)
  repaint(roomPic)
  
  # print description
  showInformation("You were teleported to Iceland.")
  showInformation("A glacier collapses in front of the portal.. you are trapped!")
  showInformation("... a scary guy appears before you and blocks your path...")
  showInformation("Prepare to fight!")
  bossFight()
  
########################
# secret room
# pyramid

def secretRoom():
  
  global player
  global egypt
  global portal
  global roomPic
  global currentRoom
  
  currentRoom = 'Secret West'
  
  weAreHere = 0
  
  play(portal)  
  
  roomPic = chromaKey(player, egypt)
  repaint(roomPic)
  
  # print description
  showInformation("Upon opening the treasure chest, you were teleported into a tomb inside the Great Pyramid!")
  showInformation("You see a golden gun on a golden shelf.")
  # print directions
  showInformation("You've reached a dead end.\n" +
                  "You must go back.")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "\"grab\" the golden gun\n" +
                            "go \"back\"")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the golden gun\n" +
                                "go \"back\"")
    elif userInput == "room":
      showInformation("You are currently in the Great Pyramid.")
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the golden gun\n" +
                                "go \"back\"")
    elif userInput == "map":
      map()
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the golden gun\n" +
                                "go \"back\"")
    elif userInput == "inventory":
      inventory()
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the golden gun\n" +
                                "go \"back\"")
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
        showInformation("You grabbed it! Hope you won't need to use the gun.")
      else:
        showInformation("There is nothing here.")
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the golden gun\n" +
                                "go \"back\"")
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the golden gun\n" +
                                "go \"back\"")
    else:
      userInput = requestString("Please enter a valid choice!\n" +
                                "Would you like to: \n" +
                                "\"grab\" the golden gun\n" +
                                "go \"back\"")

########################
# second secret room secret room
# tajmahal
# treasure chest or underground cave from room 4 (ocean)
# magic whirlpool

def room6():
  
  global player
  global tajmahal
  global portal
  global roomPic
  global currentRoom
  
  currentRoom = 'Secret South'
  
  weAreHere = 0
  
  play(portal)  
  
  roomPic = chromaKey(player, tajmahal)
  repaint(roomPic)
  
  # print description
  showInformation("You were sucked down a magic whirlpool and arrived at the Taj Mahal!")
  showInformation("There is a miniture statue sitting on a pedestal.")
  # print directions
  showInformation("You've reached a dead end.\n" +
                  "You must go back.")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "\"grab\" the statue\n" +
                            "go \"back\"")
  # while user input
  while weAreHere == 0:
    if userInput == "exit":
      global quitGame
      weAreHere = 1
      quitGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the statue\n" +
                                "go \"back\"")
    elif userInput == "room":
      showInformation("You are currently in the Taj Mahal.")
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the statue\n" +
                                "go \"back\"")
    elif userInput == "map":
      map()
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the statue\n" +
                                "go \"back\"")
    elif userInput == "back":
      weAreHere = 1
      room4()
    elif userInput == "grab":
      global items
      global secret
      if 'idol' not in items:
        play(secret)
        items.append('idol')
        showInformation("You grabbed it! Your health has been increased.")
        global myHealth
        myHealth += 50
      else:
        showInformation("There is nothing here.")
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the statue\n" +
                                "go \"back\"")
    elif userInput == "health":
      global myHealth
      showInformation("Your health = " + str(myHealth))
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the statue\n" +
                                "go \"back\"")
    elif userInput == "inventory":
      inventory()
      userInput = requestString("Would you like to: \n" +
                                "\"grab\" the statue\n" +
                                "go \"back\"")
    else:
      userInput = requestString("Please enter a valid choice!\n" +
                                "Would you like to: \n" +
                                "\"grab\" the statue\n" +
                                "go \"back\"")            


########################
#use gun
def useGun():
  global items
  global gunshot
  numBullets = items.count('bullet')
  if numBullets > 0:
    play(gunshot)
    items.remove('bullet')
    i = random.random()
    score = int(i * 100)
    if score <= 75:
      return 'Hit!'
    else:
      return 'You missed!'
  else:
    return 'You are out of bullets.'
    

########################
#boss fight
def bossFight():
  global bossHealth
  global myHealth
  global quitGame
  global items
  global gunshot
  global punchSound
  global necksnap
  
  weAreHere = 0
  while weAreHere == 0:
    if bossHealth <= 0 or myHealth <= 0:
      weAreHere = 1
    elif "gun" not in items:
      userInput = requestString("You can \"punch\"")
      if userInput == "gun":
        showInformation("You don't have a gun!") 
    else:
      userInput = requestString("Would you like to: \n" +
                                "use your \"gun\"\n" +
                                "or \"punch\"")
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
        if (userInput == 'gun' or userInput == 'punch') and bossHealth > 0 :
          i = random.random()
          if int(i * 100) >= 80:
            showInformation("Boss has hit you.")
            play(punchSound)
            myHealth -= 5
          else:
            showInformation("Boss swings and misses.")
      elif userInput == "punch":
        play(punchSound)
        result = punch()
        showInformation(result)
        if "Hit" in result:
          bossHealth -= 5
        if (userInput == 'gun' or userInput == 'punch') and bossHealth > 0 :
          i = random.random()
          if int(i * 100) >= 80:
            showInformation("Boss has hit you.")
            play(punchSound)
            myHealth -= 5
          else:
            showInformation("Boss swings and misses.")
      elif userInput == "health":
        showInformation("Your health = " + str(myHealth) + "\n"
                        + "Boss's health = " + str(bossHealth))    
      elif userInput == "inventory":
        inventory()
      else:
        showInformation("Please enter a valid choice!")
  if userInput == 'exit':
    quitGame = 1
  elif myHealth > 0:
    showInformation("You killed the boss. Congratulations!")
    play(necksnap)
    quitGame = 1
  else:
    showInformation("You are dead.")
    play(necksnap)
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
    showInformation("You awaken on a beach with the Golden Gate Bridge in the distance...")
    startingRoom()

  # goodbye message
  showInformation("Thanks for playing, " + userName)
  quit
  
game()