import random
import time

COLUMNS = "ABC"
ROWS = "123"
WIN_LINES = [
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # rows
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # columns
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)],                            # diagonals
]


# Function for X/O
def choose_x_o():
    while True:
        xo = input("Choose your symbol (X or O): ").strip().upper()
        if xo == "X":
            return "X", "O"
        elif xo == "O":
            return "O", "X"
        print("Wrong character entered")


# Function for Lists/Game Area
def play_area():
    return [["-"] * 3 for _ in range(3)]


# Function for Output
def play_output(board):
    print()
    print("    A   B   C")
    for i, row in enumerate(board):
        print(f"{ROWS[i]}   " + " | ".join(row))
        if i < 2:
            print("   ---+---+---")
    print()


# Function for Gameplay
def play_input(board, symbol):
    while True:
        move = input("Your move (e.g. A1, or 'reset'): ").strip().upper()
        if move == "RESET":
            play_reset(board)
            return False
        if len(move) != 2 or move[0] not in COLUMNS or move[1] not in ROWS:
            print("Invalid input. Use a column A-C and a row 1-3, e.g. B2.")
            continue
        row, col = ROWS.index(move[1]), COLUMNS.index(move[0])
        if play_check(board, row, col) is False:
            print("That spot is already taken.")
            continue
        board[row][col] = symbol
        return True


# Function for PC Gameplay
def play_pc(board, symbol):
    print("Computer is thinking...")
    time.sleep(1.5)
    free = [(r, c) for r in range(3) for c in range(3) if board[r][c] == "-"]
    row, col = random.choice(free)
    board[row][col] = symbol
    print(f"Computer plays {COLUMNS[col]}{ROWS[row]}")
    return row, col


# Function for Checking the Play
def play_check(board, row=None, col=None):
    if row is not None and col is not None:
        return board[row][col] == "-"
    for line in WIN_LINES:
        a, b, c = (board[r][k] for r, k in line)
        if a != "-" and a == b == c:
            return a
    if all(cell != "-" for r in board for cell in r):
        return "draw"
    return None


# Function for Reset
def play_reset(board):
    for row in board:
        row[:] = ["-"] * 3
    print("Board has been reset.")


def play_announce(result, player):
    if result == "draw":
        print("It's a draw!")
    elif result == player:
        print("You win!")
    else:
        print("The computer wins!")


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    player, pc = choose_x_o()
    board = play_area()

    while True:
        play_output(board)
        if not play_input(board, player):
            continue  # board was reset
        result = play_check(board)
        play_output(board)
        if result is None:
            play_pc(board, pc)
            result = play_check(board)
        if result is not None:
            play_announce(result, player)
            if input("Play again? (y/n): ").strip().lower() != "y":
                break
            play_reset(board)
