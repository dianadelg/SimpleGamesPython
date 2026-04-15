import random
import generateWords
import sys

# algo, provide a word for scrambling
# use random to move around letters
# user guesses until they get it OR give up

def main():
    word = generateWords.getWord() # replace with word from list
    scrambledWord=generateWords.getScrambledWord(word)
    hasWon = False
    tries=0
    while(hasWon == False):
        print("Scrambled word is: " + scrambledWord)
        print("Enter guess. If giving up, type X:")
        guess = input()
        if guess != "X":
            tries+=1
        else:
            print("Better luck next time! Word was: " + word + ". Number of guesses: " + str(tries))
            break
        #check if turn caused a win
        if(guess.capitalize() == word.capitalize()):
            print("Congrats! You guessed the word in " + str(tries) + " tries")
            break;

if __name__ == "__main__":
    sys.exit(main())