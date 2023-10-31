def finalresult(board):

  for a in range(2):
    if board[a][0] == board[a][1] == board[a][2]:
      return board[a][1] + " won"
    if board[0][a] == board[1][a] == board[2][a]:
      return board[1][a] + " won"

  for a in range(2):
    if board[0][0] == board[1][1] == board[2][2]:
      return board[1][1] + " won"
    if board[0][2] == board[1][1] == board[2][0]:
      return board[1][1] + " won"

  return "draw"

board = [['O', 'X', 'X'], ['X', 'X', 'O'], ['O', 'X', 'X']]

result = finalresult(board)

print(result)