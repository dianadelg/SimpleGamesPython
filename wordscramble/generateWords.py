import random

def getWord():
    with open('words.txt', 'r') as file:
        words = file.read().split()
        return random.choice(words)

def getScrambledWord(word):
    # given a word, return it scrambled
    # convert string to list
    tempList = list(word)
    # randomize list
    random.shuffle(tempList)
    # convert back to string, first convert chars to strings
    return "".join(map(str, tempList)) 