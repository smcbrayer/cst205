#Lab 14

### There are 2 typos in the text: a 'd' by itself, and 'mot' instead of 'not' ###


def makeFile(): 
  #read a file as string

  file = pickAFile()

  text = open(file, "rt")

  myString = text.read()
  
  text.close
  
  return myString

def textStats():
  
  myString = makeFile()
  myString = myString.lower()
  myString = myString.replace("-", " ")

  eggCount = 0
  wordCount = {}
  wordList = []

  wordList = myString.split()

  for i in range(0, len(wordList)):
    word = wordList[i]
    if word not in wordCount:
      wordCount[word] = 1
    else:
      wordCount[word] += 1

  printNow("The total number of words used is " + str(len(wordCount)))
    
  printNow("The total number of times \'eggs\' is used is: " + str(wordCount['eggs']))

  printNow("The total number of words in the text is : " + str(len(wordList)))

  
  
