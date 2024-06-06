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
        winner = check()
        if winner:
            print(winner)
            re = input("Do you want a Rematch(y/n)?")
            rematch(re)
        moves += 1
        x_turn = not x_turn
    return moves

def check():
   #check row
    for x in range (3):
        if boardMat[x][0] ==  boardMat[x][1] ==  boardMat[x][2] != "☐ ":
            return (f"Player {'1'if boardMat[x][0] == 'X ' else '2'} Win !!")

    #check column
    for Y in range (3):
        if boardMat[0][Y] == boardMat[1][Y] == boardMat[2][Y] != "☐ ":
            return (f"Player {'1' if boardMat[0][Y] == 'X ' else '2'} Win !!")
    #check diagonal
    if boardMat[0][0] == boardMat[1][1] == boardMat[2][2] != "☐ ":
        return (f"Player {'1' if boardMat[0][0] == 'X ' else '2'} Win !!")
    elif boardMat[0][2] == boardMat[1][1] == boardMat[2][0] != "☐ ":
        return (f"Player {'1' if boardMat[0][0] == 'X ' else '2'} Win !!")
    #Check draw
    allMove = []
    for x in range(3):
        for y in range(3):
            allMove.append(boardMat[x][y])
    if all(element != "☐ " for element in allMove):
        return "Match Tied !!!"
    return None

def rematch(re):
    re = re.lower()
    if re == "y":
        global boardMat

        boardMat = [["☐ ", "☐ ", "☐ "], ["☐ ", "☐ ", "☐ "], ["☐ ", "☐ ", "☐ "]]
        main()

    else:
        exit()

def main():
    start()
    print_board()
    move(moves)

main()
