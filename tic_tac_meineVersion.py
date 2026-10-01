COLUMNS = "ABC"
ROWS = "123"
# Function for X/O

def choose_x_o():
    #xo = input() --> 1. Vorschlag
    #ox = ""
    #if xo == "X":
        #ox = "O"
    #elif xo == "O":
        #ox = "X"
    #else:
        #print("Wrong character entered")
    
    while True:
        xo = input("Choose your symbol (X or O): ").strip().upper()
        if xo == "X":
            return "X", "O"
        elif xo == "O":
            return "O", "X"
        print("Wrong character entered")


# Function for Lists/Game Area
def play_area():
    # field = [("-", "-", "-"), ("-", "-", "-"), ("-", "-", "-")] --> 1. Vorschlag
    #field = [["-" for _ in range(3)] for _ in range(3)] --> 2. Vorschlag
    return [["-"] * 3 for _ in range(3)]
    
# Function for Output
def play_output(board):
    #print (field)
    # Row_1 = ("A1:A3"), Row_2 = ("B1:B3"), Row_3 = ("C1:C3") --> 1. Vorschlag
    
    #print("||| A1 = " + field[0][0] + " ||| A2 = " + field[0][1] + " ||| A3 = " + field[0][2] + " ||| ") --> 2. Vorschlag
    #print("||| B1 = " + field[1][0] + " ||| B2 = " + field[1][1] + " ||| B3 = " + field[1][2] + " ||| ")
    #print("||| C1 = " + field[2][0] + " ||| C2 = " + field[2][1] + " ||| C3 = " + field[2][2] + " ||| ")

    print()
    print("    A   B   C")
    for i, row in enumerate(board):
        print(f"{ROWS[i]}   " + " | ".join(row))
        if i < 2:
            print("   ---+---+---")
    print()


# Function for Gameplay
def play_input():
    #print("Where do you want to set your symbol?") --> 1. Vorschlag
    #move = input(f"Choose your move: ")
    #if len(move) != 2 or 

    while True:
        move = input("Your move (e.g. A1): ").strip().upper()
        if len(move) != 2 or move[0] not in COLUMNS or move[1] not in ROWS:
            print("Invalid input. Use a column A-C and a row 1-3, e.g. B2.")
            continue


     
# Function for PC Gameplay
def play_pc():
    pass

# Function for Checking the Play
def play_check(board, row=None, col=None):
    if row is not None and col is not None:
        return board[row][col] == "-"
    if play_check(board, row, col) is False:
        print("That spot is already taken.")
        continue
    
# Function for Reset
def play_reset():
    pass

# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

    player, pc = choose_x_o()
    board = play_area()
    while True:
     play_output(board)