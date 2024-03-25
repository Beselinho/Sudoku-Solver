import pygame
import threading
import time

pygame.init()

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Screen dimensions
screenWidth = 815
screenHeight = 930
lineHeight = 815

# Other constants
borderColor = (0, 0, 0)
boardLength = 9
cellSize = 80
numbersDistance = 85
topPadding = 25
leftPadding = 30
font = pygame.font.Font(None, 80)
squareSide = 3
widthSquareLine = 10
widthCellLine = 5

timeFormat = ""
topTimeCoord = 850
leftTimeCoord = 600
seconds = 0
minutes = 0

run = True


screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Sudoku Solver")


#Solver Functions
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
                return i, j
    return -1, -1

def drawSelectCell(left, top):
    rectWidth = 80
    rectHeight = 80
    thickness = 3
    pygame.draw.rect(screen, (255, 0, 0), (left, top, rectWidth, rectHeight), thickness)
    pygame.display.update()
    

def drawCellsLines():
    for i in range(4):
        xSquareLine = i * 270 
        pygame.draw.line(screen, borderColor, (xSquareLine, 0), (xSquareLine, lineHeight), widthSquareLine) 

        ySquareLine = i * 270
        pygame.draw.line(screen, borderColor, (0, ySquareLine), (screenWidth, ySquareLine), widthSquareLine)

    for i in range(10):
        xCellLines = i * 90
        pygame.draw.line(screen, borderColor, (xCellLines, 0), (xCellLines, lineHeight), widthCellLine)
         
        yCellLines = i * 90   
        pygame.draw.line(screen, borderColor, (0, yCellLines), (screenWidth, yCellLines), widthCellLine)

def drawDefaultNumbers():
    for i in range(boardLength):
        for j in range(boardLength):
            if board[i][j] != 0:
                numberText = font.render(str(board[i][j]), True, borderColor)
                screen.blit(numberText, (leftPadding + j * numbersDistance + widthCellLine * j,  topPadding + i * numbersDistance + widthCellLine * i))


def checkEvents():
    global run
    solve_thread = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if solve_thread is None or not solve_thread.is_alive():
                    solve_thread = threading.Thread(target=solve_puzzle)
                    solve_thread.start()
        if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = pygame.mouse.get_pos()
                if clicked:
                    #ok = True
                    drawSelectCell(clicked[0], clicked[1])
                    
                    

def solve():
    row, col = findEmptyCell()
    if row == -1 and col == -1:
        return True
    else:
        for number in range(1, 10):
            if checkRow(row, number) and checkColumn(col, number) and checkSquare(row, col, number):
                drawSelectCell(widthCellLine + col * numbersDistance + widthCellLine * col, widthCellLine + row * numbersDistance + widthCellLine * row)
                
                board[row][col] = number
                numberText = font.render(str(board[row][col]), True, borderColor)
                screen.blit(numberText, (leftPadding + col * numbersDistance + widthCellLine * col,  topPadding + row * numbersDistance + widthCellLine * row))
                pygame.display.update()
                pygame.time.delay(300)
                
                if solve():
                    return True  
                
                board[row][col] = 0
                pygame.draw.rect(screen, (255, 255, 255), (6 + col * numbersDistance + widthCellLine * col, 6 + row * numbersDistance + widthCellLine * row, cellSize, cellSize))
                pygame.display.update()
                pygame.time.delay(200)
                
        return False 

def solve_puzzle():
    solve()

while run:
    screen.fill((255,255,255))   
    drawCellsLines()
    checkEvents()
    drawDefaultNumbers()
    #drawClock(minutes, seconds)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if seconds == 59:
        minutes += 1
        seconds = 0 
    else:
        seconds += 1
    time.sleep(1)

pygame.quit()
