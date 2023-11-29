import random

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_winner(board):
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] != None and board[x][1] != None and board[x][2]!= None:
            return board[x][0]
        if board[0][x] == board[1][x] == board[2][x] and board[0][x] != None and board[1][x] != None and board[2][x]!= None:
            return board[0][x]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None and board[1][1] != None and board[2][2]!= None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != None and board[1][1] != None and board[2][0]!= None:
        return board[0][2]
    if all(board[a][b] is not None for a in range(3) for b in range(3)):
        return "draw"
         
def other_player(player):
    if player == 'O' :
        return "X"
    else:
        return "O"
    
def bot_move(board):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] is None:
            return x, y