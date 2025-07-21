def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_idx = 0
    moves = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while moves < 9:
        player = players[current_player_idx]
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid row or column. Please enter a number between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue

            board[row][col] = player
            moves += 1
            print_board(board)

            if check_win(board, player):
                print(f"Player {player} wins!")
                break

            current_player_idx = 1 - current_player_idx # Switch player

        except ValueError:
            print("Invalid input. Please enter a number.")

    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
