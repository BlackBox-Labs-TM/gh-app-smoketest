# simple tic tac toe game in python
# players take turns entering a number 1–9 to place X or O on the board

# create the board as a list of strings (positions 1–9)
board = [" "] * 9

def print_board():
    """print the current board layout"""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    """check all win combos to see if player won"""
    wins = [
        (0,1,2), (3,4,5), (6,7,8), # rows
        (0,3,6), (1,4,7), (2,5,8), # cols
        (0,4,8), (2,4,6)           # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full():
    """check if the board has no empty spaces"""
    return " " not in board

def play_game():
    """main game loop"""
    current = "X"  # X always starts
    while True:
        print_board()
        # ask for move
        move = input(f"player {current}, choose position (1-9): ")
        
        # make sure input is valid
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("invalid input, try again.")
            continue

        idx = int(move) - 1
        if board[idx] != " ":
            print("spot taken, try again.")
            continue

        # make the move
        board[idx] = current

        # check win
        if check_winner(current):
            print_board()
            print(f"player {current} wins!")
            break

        # check draw
        if board_full():
            print_board()
            print("it's a draw!")
            break

        # swap player
        current = "O" if current == "X" else "X"

# run it
if __name__ == "__main__":
    play_game()

