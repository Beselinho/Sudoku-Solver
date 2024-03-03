boardLength = 9
squareSide = 3

board = [
        [0, 1, 0, 9, 0, 0, 0, 0, 5],
        [0, 0, 4, 6, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 4, 5, 2, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 9, 0, 8, 1, 0, 0, 2],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 2, 4, 0, 0, 1],
        ]


def checkRow(i, num):
    for col in range(boardLength):
        if board[i][col] == num:
            return False
    return True

def checkColumn(j, num):
    for row in range(boardLength):
        if board[row][j] == num:
            return False
    return True

def checkSquare(i, j, num):
    newI = int(i / squareSide) * squareSide
    newJ = int(j / squareSide) * squareSide
    for row in range(newI, newI + squareSide):
        for col in range(newJ, newJ + squareSide):
            if board[row][col] == num:
                return False 
    return True 



def findEmptyCell():
    for i in range(boardLength):
        for j in range(boardLength):
            if board[i][j] == 0:
                return i,j
    return -1,-1


def solve():
    row, col = findEmptyCell()
    if row == -1 and col == -1:
        return True
    else:
        for number in range(1, 10):
            if checkRow(row, number) and checkColumn(col, number) and checkSquare(row, col, number):
                board[row][col] = number
                if solve():
                    return True 
                board[row][col] = 0 
        return False 


def printBoard():
    for i in range(boardLength):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(boardLength):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


solve()        
printBoard()

                     




