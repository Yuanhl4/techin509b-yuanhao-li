from logic import make_empty_board, get_winner, other_player, bot_move, game_start
import csv

def show_board(board):
    for row in board:
        print(row)
    print()


def log_game_result(game_data):
    with open('logs/game_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(game_data)

if __name__ == '__main__':
    player_num = input("Please enter the number of players: ")
    board = make_empty_board()
    winner = None

    if player_num != "1" and player_num != "2":
        print("Please enter the correct number")

    if player_num == "2":
        turn = 'X'
        turns = 1

        print("Game start!")

        while winner is None:
            show_board(board)
            print(f"Player {turn}, your turn!")

            row = input("Enter the row (1-3): ")
            col = input("Enter the column (1-3): ")

            if row.isdigit() and col.isdigit() and 1 <= int(row) <= 3 and 1 <= int(col) <= 3:
                row = int(row) - 1
                col = int(col) - 1
                
                last_position_x = row
                last_position_y = col

                if board[row][col] is None:
                    board[row][col] = turn
                    turns = turns + 1
                    winner = get_winner(board)
                    if winner is None:
                        turn = other_player(turn)

                    else:
                        show_board(board)
                        turn_num = turns + 1
                        turn_num = turns + 1
                        log_game_result([last_position_x, last_position_y, turn_num, winner])
                else:
                    print("Error! The position is already occupied.\n")
            else:
                print("Error! Invalid row or column. Try again.\n")

        if winner == 'draw':
            print(f"It's a {winner}!")
        else:
            print(f"Player {winner} wins!")
        turn_num = turns + 1
        log_game_result([last_position_x, last_position_y, turn_num, winner])
        


    if player_num == "1":

        #print("Game start!")

        turn = "X"
        turns = 1

        while winner is None:
            show_board(board)
            
            print(f"Player  {turn}'s turn!")

            row = input("Enter the row (1-3): ")
            col = input("Enter the column (1-3): ")

            if row.isdigit() and col.isdigit() and 1 <= int(row) <= 3 and 1 <= int(col) <= 3:
                row = int(row) - 1
                col = int(col) - 1

                last_position_x = row
                last_position_y = col

                if board[row][col] is None:
                    board[row][col] = turn
                    turns = turns + 1
                    show_board(board)
                    winner = get_winner(board)
                    if winner is None:
                        turn = other_player(turn)
                        print("Bot's turn!")
                        #time.sleep(3)
                        bot_row, bot_col = bot_move(board)
                        board[bot_row][bot_col] = turn
                        winner = get_winner(board)
                        #show_board(board)
                        turn = other_player(turn)
                        #winner = get_winner(board)
                    else:
                        show_board(board)
                        turns = turns + 1
                        turn_num = turns + 1
                        log_game_result([last_position_x, last_position_y, turn_num, winner])
                else:
                    print("Error! The position is already occupied.\n")
            else:
                print("Error! Invalid row or column. Try again.\n")
        if winner == 'draw':
            print(f"It's a {winner}!")
        else:
            print(f"Player {winner} wins!")