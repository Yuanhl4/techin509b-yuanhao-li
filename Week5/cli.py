# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from Week2 import finalresult

# Reminder to check all the tests

def make_a_move(x,y,chess,board):
    # invalid decision and decide again
    if not 0 <= x <= 2 or not 0 <= y <= 2:
        print("Error! Check your position\n")
        return 1
    # valid decision
    
    else:
        board[x][y] = chess
        return 0
    
def show_board(board):
    for item in board:
        print(item)
        print("\n")
    
if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    turn = 0
    while winner == None:
        print("TODO: take a turn!")

        show_board(board)

        row = input("Enter the row (1-3): ")
        col = input("Enter the column (1-3): ")
        
        if row.isdigit() and col.isdigit() and 1 <= int(row) <= 3 and 1 <= int(col) <= 3:
            row = int(row) - 1
            col = int(col) - 1
     
            if not board[row][col]:
                if turn == 1:
                    board[row][col] = 'X'
                else:
                    board[row][col] = "O"
                turn = not turn 
                print("update board")
                show_board(board)
            else:
                print("Error! The position is already occupied.\n")
                continue
        else:
            print("Error! Invalid row or column.Try again\n")
            continue
    
        if turn == 1:
            print("User 1, your turn\n")
        else:
            print("User 2, your turn\n")
        # TODO: Show the board to the user. --- ok
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        res = week2.finalresult(board)
        if res == 'X':
            winner = 'X'  # FIXME
        elif res == 'O':
            winner = "O"
        elif res == 'draw':
            winner = 'draw'

