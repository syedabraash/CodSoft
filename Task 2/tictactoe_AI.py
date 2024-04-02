import math

def print_board(board):
    print("Current State Of Board : \n")
    for i in range(0, 9):
        if (i > 0) and (i % 3) == 0:
            print("\n")
        if board[i] == 0:
            print("- ", end=" ")
        if board[i] == 1:
            print("O ", end=" ")
        if board[i] == -1:
            print("X ", end=" ")
    print("\n\n")


def get_user_move(board, player):
    while True:
        try:
            pos = int(input(f"Enter {player}'s position from [1...9]: "))
            if pos < 1 or pos > 9 or board[pos - 1] != 0:
                print("Invalid move! Please try again.")
            else:
                return pos - 1
        except ValueError:
            print("Invalid input! Please enter a number.")


def minimax(board, player):
    x = analyze_board(board)
    if x != 0:
        return x * player
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, player * -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value


def get_comp_move(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    return pos


def analyze_board(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]:
            return board[cb[i][2]]
    return 0


def main():
    choice = input("Enter 1 for single player, 2 for multiplayer: ")
    choice = int(choice)
    board = [0] * 9
    player = 1 if choice == 1 else -1
    print("Computer : O Vs. You : X") if choice == 1 else print("Player 1: X Vs. Player 2: O")
    print_board(board)
    while True:
        if analyze_board(board) != 0:
            break
        if choice == 1:
            if player == 1:
                pos = get_user_move(board, 'X')
                board[pos] = -1
            else:
                pos = get_comp_move(board)
                board[pos] = 1
            player *= -1
        else:
            pos = get_user_move(board, 'X' if player == 1 else 'O')
            board[pos] = player
            player *= -1
        print_board(board)
    result = analyze_board(board)
    if result == -1:
        print("X Wins!!! O Loose !!!")
    elif result == 1:
        print("X Loose!!! O Wins !!!!")
    else:
        print("Draw!!!")


if __name__ == "__main__":
    main()
