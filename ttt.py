moves = 0

boardMat = [["☐ ", "☐ ", "☐ "], ["☐ ", "☐ ", "☐ "], ["☐ ", "☐ ", "☐ "]]

def print_board():
    for row in range(3):
        for col in range(3):
            print(f"{boardMat[row][col]}", end="")
        print()

def start():
    print("Let's Start the Game")
    print("Player-1 = X AND Player-2 = 0")

def finished(moves):
    return moves >= 9

def move(moves):
    x_turn = True
    while not finished(moves):
        if x_turn:
            print("It's Player-1 Turn")
            row, col = input("Enter in x,y Form ").split(",")
            row, col = int(row), int(col)
            if boardMat[row][col] == "X " or boardMat[row][col] == "0 ":
                print("Already Done there")
                continue
            else:
                boardMat[row][col] = "X "
        else:
            print("It's Player-2 Turn")
            row, col = input("Enter in x,y Form ").split(",")
            row, col = int(row), int(col)
            if boardMat[row][col] == "X " or boardMat[row][col] == "0 ":
                print("Already Done there")
                continue
            else:
                boardMat[row][col] = "0 "
        print_board()
        moves += 1
        x_turn = not x_turn
    return moves

def main():
    start()
    print_board()
    move(moves)

main()
