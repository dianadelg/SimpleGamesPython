import random 
import sys

def main():
    
    users_choice = -1
    actions = ["rock", "paper", "scissors"]
    while(users_choice != 0):

        print("Pick rock: enter 1")
        print("Pick paper: enter 2")
        print("Pick scissors: enter 3")
        print("End game: enter 0")

        print()
        print("Rock...paper...scissors...shoot!")

        users_choice = int(input())
        
        computers_choice = random.choice(actions)

        if(computers_choice == "rock"):
            # check against rock
            if(users_choice == 1):
                #means computer = rock vs user = rock
                print("Tie! You both picked rock")
            elif(users_choice == 2):
                # means computer = rock, user = paper
                print("You win! Computer picked rock, you picked paper.")
            else:
                # means computer == rock, user = scissors
                print("Computer wins. Computer picked rock, you picked scissors.")
        elif(computers_choice == "paper"):
            # check against paper
            if(users_choice == 1):
                #means computer = paper vs user = rock
                print("Computer wins. Computer picked paper, you picked rock.")
            elif(users_choice == 2):
                # means computer = paper, user = paper
                print("Tie! You both picked paper")
            else:
                # means computer == paper, user = scissors
                print("You win! Computer picked paper, you picked scissors.")
        else:
            # means it is scissors
            if(users_choice == 1):
                #means computer = scissors vs user = rock
                print("You win! Computer picked scissors, you picked rock.")
            elif(users_choice == 2):
                # means computer = scissors, user = paper
                print("Computer wins. Computer picked scissors, you picked paper.")
            else:
                # means computer == scissors, user = scissors
                print("Tie! You both picked scissors")
        print()
    print("Goodbye!")






if __name__ == "__main__":
    sys.exit(main())