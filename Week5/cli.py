from logic import make_empty_board, get_winner, other_player

def show_board(board):
    for row in board:
        print(row)
    print()

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    turn = 'X'

    while winner is None:
        show_board(board)
        print(f"Player {turn}, your turn!")

        row = input("Enter the row (1-3): ")
        col = input("Enter the column (1-3): ")

        if row.isdigit() and col.isdigit() and 1 <= int(row) <= 3 and 1 <= int(col) <= 3:
            row = int(row) - 1
            col = int(col) - 1

            if board[row][col] is None:
                board[row][col] = turn
                winner = get_winner(board)
                if winner is None:
                    turn = other_player(turn)
                else:
                    show_board(board)
            else:
                print("Error! The position is already occupied.\n")
        else:
            print("Error! Invalid row or column. Try again.\n")

    if winner == 'draw':
        print(f"It's a {winner}!")
    else:
        print(f"Player {winner} wins!")
