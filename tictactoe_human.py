def main():
    board = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]

    turn = "X"
    win = False

    while not win:
        for row in board:
            for cell in row:
                print(f"{cell} ", end="")
            print()

        row = int(input("Row "))
        col = int(input("Col "))

        board[row][col] = turn

        turn = "O" if turn == "X" else "X"

        for row in board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != "-":
                print(f"WINNER! {row[0]}")
                win = True
                break

        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "-":
                print(f"WINNER! {board[0][i]}")
                win = True
                break

    pass

if __name__ == "__main__":
    main()
