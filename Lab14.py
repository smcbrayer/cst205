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

  
def getHeadlines():
  myFile = open('C:\\Users\\maria\\Documents\\Projects - School\\CST 205\\otterrealm.html', 'rt')
  news = myFile.read()
  myFile.close()
  
  headlines = ""
  
  #the column where the headlines are located, so we don't have to search the entire page.
  otterNewsStart = news.find('<div class="column mid-column">')

  headlineLocation = otterNewsStart  #Starting place to look for headlines

  if otterNewsStart <> -1: #make sure the center column exists
     # loop through links wrapping headlines, we want text only
     headlineLocation = news.find('rel="bookmark">\n',headlineLocation)
     while (headlineLocation <> -1):
       headlineStart = headlineLocation + 17 # characters in rel="bookmark>\n"
       headlineEnd = news.find("</a>",headlineStart+1) #find closing anchor tag
       headline = news[headlineStart:headlineEnd]
       #this replace characters is messy
       headline = news[headlineStart:headlineEnd].lstrip().replace("&nbsp;", " ").replace("\xE2\x80\x99","'").replace("&#8230;","...")
       headlines = headlines + headline + "\n" #create a list of the headlines
       headlineLocation = news.find('rel="bookmark"',headlineLocation+1) #find the next headline
  print headlines
