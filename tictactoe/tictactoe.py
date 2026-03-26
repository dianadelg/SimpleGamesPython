import sys
import random

choices = ['x', 'o']

def generate_xo():
    # to be used to switch up who goes first
    return random.choice(choices)

def printBoard(board):
    # to be used to print the board in a readable format
    print("\n   1   2   3") 
    for i in range(3):
        print(str(i+1) + "  " + " | ".join(board[i]))
        if i < 2:
            print("  ---+---+---")


def takeTurn(currentTurn, turnsLeft):
    # called for each turn taken
    print(currentTurn + "s turn")
    row = int(input())
    flag = True
    
    while flag == True:
        row = -1
        col = -1
        while(row > 3 or row < 1):
            print("Please select a valid row number: 1, 2, or 3:")
            row = int(input())
        while(col > 3 or col < 1):
            print("Please select a valid col number: 1, 2, or 3:")
            col = int(input())
        if(board[row][col]!="_"):
            flag = False
            board[row][col] = currentTurn
        else:
            print("Spot already played, pick a new one")


def didTurnWin(board, currentTurn):
    #check to see if turn won
    # can combine these but for now...
    
    # check horizontals
    if (board[0][0] == currentTurn and board[0][1] == currentTurn and board [0][2] == currentTurn) or (board [1][0] == currentTurn and board[1][1] == currentTurn or board [1][2] == currentTurn) or (board [2][0] == currentTurn and board[2][1] == currentTurn and board[2][2] == currentTurn):
        print(currentTurn + " has won!")
        return True
    # check verticals
    elif (board[0][0] == currentTurn and board[1][0] == currentTurn and board [2][0] == currentTurn) or (board [0][1] == currentTurn and board[1][1] == currentTurn or board [2][1] == currentTurn) or (board [0][2] == currentTurn and board[1][2] == currentTurn and board[2][2] == currentTurn):
        print(currentTurn + " has won!")
        return True
    # check diagonals
    elif (board[0][0] == currentTurn and board[1][1] == currentTurn and board [2][2] == currentTurn) or (board [2][0] == currentTurn and board[1][1] == currentTurn or board [0][2] == currentTurn):
        print(currentTurn + " has won!")
        return True
    else:
        return False


#Initialize board and print current board
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
print("Welcome to Tic Tac Toe!")

def main():
    turnsLeft = 9
    hasWon = False
    currentTurn = (generate_xo())
    while(turnsLeft > 1):
        printBoard(board)
        takeTurn(currentTurn, turnsLeft)
        turnsLeft=turnsLeft-1
        #check if turn caused a win
        if(didTurnWin(board, currentTurn)):
            printBoard(board) # print to show win
            print("Game has been won by " + currentTurn)
        else:
            # switch to next player's turn based on current player
            if choices[0] != currentTurn:
                nextPlayer = choices[1]
            else:
                nextPlayer = choices[0]

if __name__ == "__main__":
    sys.exit(main())
