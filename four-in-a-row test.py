def create_board():
    """Create an empty Connect Four board."""
    return [[" " for _ in range(7)] for _ in range(6)]

def display_board(board):
    """Display the game board in a user-friendly format using string concatenation."""
    for row in board:
        row_display = "|"
        for cell in row:
            row_display += cell + "|"
        print(row_display)
    column_numbers = " "
    for col_num in range(7):
        column_numbers += str(col_num) + " "
    print(column_numbers)

def get_player_input(player, board):
    """Get a valid column input from the player."""
    while True:
        try:
            column = int(input(f"Player {player}, choose a column (0-6): "))
            if 0 <= column < 7 and board[0][column] == " ":
                return column
            else:
                print("Invalid choice. Column is full or out of range.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")

def drop_disc(board, column, player_disc):
    """Place the player's disc in the selected column."""
    for row in reversed(board):  # Start from the bottom of the column
        if row[column] == " ":
            row[column] = player_disc
            return

def check_winner(board, player_disc):
    """Check if the given player has won the game."""
    # Check horizontal
    for row in board:
        for col in range(4):
            if all(cell == player_disc for cell in row[col:col + 4]):
                return True

    # Check vertical
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == player_disc for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player_disc for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == player_disc for i in range(4)):
                return True

    return False

def is_board_full(board):
    """Check if the board is completely full."""
    return all(cell != " " for row in board for cell in row)

def ask_replay():
    """Ask players if they want to play again."""
    while True:
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay in ("yes", "no"):
            return replay == "yes"
        print("Invalid input. Please enter 'yes' or 'no'.")

def play_game():
    """Main game loop."""
    print("Welcome to Connect Four!")
    while True:
        board = create_board()
        current_player, player_disc = 1, "X"  # Player 1 uses 'X', Player 2 uses 'O'

        while True:
            display_board(board)
            column = get_player_input(current_player, board)
            drop_disc(board, column, player_disc)

            if check_winner(board, player_disc):
                display_board(board)
                print(f"Player {current_player} ({player_disc}) wins!")
                break

            if is_board_full(board):
                display_board(board)
                print("It's a tie!")
                break

            # Switch players
            current_player = 2 if current_player == 1 else 1
            player_disc = "O" if player_disc == "X" else "X"

        if not ask_replay():
            print("Thanks for playing Connect Four! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
