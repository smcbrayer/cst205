#Lab 13


s1 = "Missile and launch pluralNoun have been moved to the east coast of North Korea in the \"last few days,\" a U.S. official with direct knowledge of the information told CNN Thursday."
s2 = "The apparent deployment comes amid further adverb statements by North Korea and heightened tensions in the region -- a situation that \"does not need to get hotter,\" a U.S. State Department spokeswoman said."
s3 = "The move of the noun and launch equipment could mean that place, which unleashed another round of adverb rhetoric accusing the United States of pushing the region to the \"brink of war,\" may be planning a missile launch soon."
s4 = "The pluralNoun, the official said, are consistent with those of a propNoun missile, which has a 2,500-mile range, meaning it could threaten South Korea, Japan and Southeast Asia."
s5 = "N. Korea threatens \'adjective\' strikes North Korea's nuclear threats S. Koreans barred from N. Korean complex Does N. Korea have something to prove?"
s6 = "The United States has been looking for a hidden North Korean east coast noun site or mobile launchers, a concern because a launch from the east coast would go over propNoun, the official said."
s7 = "It is believed a noun launch would be a \"test\" launch rather than a targeted verb. That is because it appears the North Koreans have only moved the components so far. The United States is waiting to see whether North Korea issues a notice to its airmen and mariners to stay out of the region."
s =""

#s1 replacemnets: pluralNoun, 
#s2 replacements: adverb,
#s3 replacements: noun, place, adverb
#s4 replacements: pluralNoun, propNoun
#s5 replacements: adjective
#s6 replacements: noun, propNoun
#s7 replacements: noun, verb

def madLib():
  global s1, s2, s3, s4, s5, s6, s7, s
  userResponse = requestString("Enter a plural noun")
  s += s1.replace("pluralNoun", userResponse)  

  userResponse = requestString("Enter an adverb")
  s += s2.replace("adverb", userResponse)
  
  userResponse = requestString("Enter a noun")
  s += s3.replace("noun", userResponse)
  userResponse = requestString("Enter a place")
  s += s3.replace("place", userResponse)
  userResponse = requestString("Enter an adverb")
  s += s3.replace("adverb", userResponse)
  
  userResponse = requestString("Enter a plural noun")
  s += s4.replace("pluralNoun", userResponse)
  userResponse = requestString("Enter a proper noun")
  s += s4.replace("propNoun", userResponse)
  
  userResponse = requestString("Enter an adjective")
  s += s5.replace("adjective", userResponse)
  
  userResponse = requestString("Enter a noun")
  s += s6.replace("noun", userResponse)
  userResponse = requestString("Enter a proper noun")
  s += s6.replace("propNoun", userResponse)
  
  userResponse = requestString("Enter a noun")
  s += s7.replace("noun", userResponse)
  userResponse = requestString("Enter a verb")
  s += s7.replace("verb", userResponse)
  
  printNow(s)


