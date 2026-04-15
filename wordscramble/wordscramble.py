import random
import generateWords
import sys

# algo, provide a word for scrambling
# use random to move around letters
# user guesses until they either give up or get it
def main():
    word = generateWords.getWord() # replace with word from list
    generateWords.getScrambledWord(word)
    hasWon = False
    while(hasWon == False):
        print("Scrambled word is: " + word)
        print("Enter guess:")
        guess = input()
        #check if turn caused a win
        if(guess.capitalize == word.capitalize):
            print("You guessed the word!    " + word)
            break;

if __name__ == "__main__":
    sys.exit(main())