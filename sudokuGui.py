import pygame
import time

pygame.init()

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

screenWidth = 815
screenHeight = 930
lineHeight = 815
timeFormat = ""
borderColor = (0,0,0)
boardLength = 9
cellSize = 80
numbersDistance = 85
topPadding = 25
leftPadding = 30
font = pygame.font.Font(None, 80)
squareSide = 3

topTimeCoord = 850
leftTimeCoord = 600
seconds = 0
minutes = 0

widthSquareLine = 10
widthCellLine = 5

screen = pygame.display.set_mode((screenWidth, screenHeight))

ok = True
run = True


#Sudoku Solving Functions
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

def drawClock(minutes, seconds):
    tensMins = int(minutes / 10)
    mins = int(minutes % 10)
    tensSec = int(seconds / 10)
    sec = int(seconds % 10)
    timeFormat = str(tensMins) + str(mins) + ":" + str(tensSec) + str(sec)
    timeText = font.render(timeFormat, True, borderColor)
    screen.blit(timeText, (leftTimeCoord, topTimeCoord))


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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve()
                
            
    
    
while run:
    screen.fill((255,255,255))
    drawCellsLines()
    checkEvents()
    drawDefaultNumbers()
    drawClock(minutes, seconds)
    pygame.display.flip()
    pygame.display.update()

    if seconds == 59:
        minutes += 1
        seconds = 0 
    else:
        seconds += 1
    time.sleep(1)

pygame.quit()





# def drawCells():
#     leftCoord = 0
#     topCoord = 0
#     for i in range(boardLength):
#         for j in range(boardLength):
#             pygame.draw.rect(screen, borderColor, pygame.Rect(leftCoord, topCoord, cellSize, cellSize), 2)
#             leftCoord += cellSize
#         topCoord += cellSize
#         leftCoord = 0