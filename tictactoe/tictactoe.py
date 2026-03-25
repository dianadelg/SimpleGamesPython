# algorithm: create 3x3 grid with cols and rows number
# print, player 1: take your turn. Ask them to enter as row, col 
# When they enter, make sure spot not already taken. If so, say "spot unavailable"
# otherwise, place element
# players 1 and 2 take turns until no spots exist on the board
# so it loops until all board spots are full (or 9 turns have happened) OR until someone has a vertical, 
# horizontal, or diagonal match

def printBoard(board):
    print("\n   1   2   3")  # column headers
    for i in range(3):
        print(str(i+1) + "  " + " | ".join(board[i]))
        if i < 2:
            print("  ---+---+---")


#Initialize board and print current board
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
print("Welcome to Tic Tac Toe!")
turnsLeft = 9
hasWon = False

while(turnsLeft > 1 and hasWon == False):
    print("X's turn:")
    row = -1
    col = -1
    while(row > 3 or row < 1 or row != "_"): ## meaning spot taken
        #maybe error handle better?
        print("Please select a valid row number: 1, 2, or 3:")
        row = int(input())
    while(col > 3 or col < 1):
        print("Please select a valid col number: 1, 2, or 3:")
        col = int(input())
    if(board[row-1][col-1] == "_"):
        print("Spot already played, pick new spots")
        # need to add the logic to pick new spots. Maybe write algo better
        while(row > 3 or row < 1 or row != "_"): ## meaning spot taken
        #maybe error handle better?
            print("Please select a valid row number: 1, 2, or 3:")
            row = int(input())
            while(col > 3 or col < 1):
                print("Please select a valid col number: 1, 2, or 3:")
                col = int(input())
    board[row-1][col-1] = "X"
    printBoard(board)
    turnsLeft=turnsLeft-1
    # need to check board for win -- tbd


    print("O's turn:")
    row = -1
    col = -1
    while(row > 3 or row < 1):
        print("Please select a valid row number: 1, 2, or 3:")
        row = int(input())
    while(col > 3 or col < 1):
        print("Please select a valid col number: 1, 2, or 3:")
        col = int(input())
        print("row :" + str(row) + " col: " + str(col))
    board[row-1][col-1] = "O"
    printBoard(board)
    turnsLeft=turnsLeft-1





