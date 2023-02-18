board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

# Winner or tie
winner = None

# Who's turn is it?
current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def check_rows():
    # Global variable
    global game_still_going

    # Check rows for same values.
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # Rows for win
    if row1 or row2 or row3:
        game_still_going = False

    # Return the winner.
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

    return


def check_columns():
    # Global variable
    global game_still_going

    # Check column for same values.
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    # Columns for win
    if column1 or column2 or column3:
        game_still_going = False

    # Return the winner.
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return


def check_diagonals():
    # Global variable
    global game_still_going

    # Check diagonals for same values.
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    # Diagonal for win
    if diagonal1 or diagonal2:
        game_still_going = False

    # Return the winner.
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return


def check_for_winner():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    # Get the winner.
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_if_game_over():
    check_for_winner()
    check_tie()


def handle_turn(player):

    print(player + "'s Turn.")

    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there, Go again.")
    board[position] = player

    display_board()


def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def play_game():
    print("Welcome to Tic Tac Toe.")
    display_board()
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # The game has ended.
    if winner == "X" or winner == "O":
        print(winner, " Won.")
    else:
        print("Its a Tie.")


play_game()
