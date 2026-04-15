import random

def getWord():
    words = ["apple", "banana", "cherry", "date", "blueberry", "kiwi", "orange"]
    randomWord = random.choice(words)
    print(randomWord)
    return randomWord

def getScrambledWord(word):
    # given a word, return it scrambled
    # convert string to list
    tempList = list(word)
    # randomize list
    scrambledList = random.shuffle(tempList)
    # convert back to string, first convert chars to strings
    stringList="-".join(map(str, scrambledList)) 
    # now convert back to string
    scrambledWord = ", ".join(stringList)
    return scrambledWord