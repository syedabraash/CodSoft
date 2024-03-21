import copy

# Define constants for empty, X, and O
EMPTY = 0
X = 1
O = -1

# Function to initialize the board
def initialize_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(["X" if cell == X else "O" if cell == O else " " for cell in row]))
        print("-" * 5)

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    # Base cases: check for terminal states
    if check_win(board, X):
        return 10 - depth
    elif check_win(board, O):
        return -10 + depth
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY  # Revert the move
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY  # Revert the move
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_move = None
    best_eval = float("-inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board_copy = copy.deepcopy(board)  # Create a copy of the board
                board_copy[i][j] = X  # Make the move on the copied board
                eval = minimax(board_copy, 0, False)  # Evaluate the copied board
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game():
    board = initialize_board()
    current_player = X
    while not is_board_full(board) and not check_win(board, X) and not check_win(board, O):
        print_board(board)
        print("Current player:", "AI" if current_player == X else "Human")
        if current_player == X:
            print("AI's turn:")
            ai_move = find_best_move(board)
            print("AI's move:", ai_move)
            board[ai_move[0]][ai_move[1]] = X
        else:
            print("Your turn (enter row and column numbers separated by space):")
            valid_move = False
            while not valid_move:
                try:
                    row, col = map(int, input().split())
                    if board[row][col] == EMPTY:
                        board[row][col] = O
                        valid_move = True
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Invalid input! Please enter row and column numbers separated by space.")
                except IndexError:
                    print("Invalid input! Row and column numbers should be between 0 and 2.")

        current_player *= -1

    print_board(board)
    if check_win(board, X):
        print("AI wins!")
    elif check_win(board, O):
        print("You win!")
    else:
        print("It's a draw!")

# Run the game
play_game()
