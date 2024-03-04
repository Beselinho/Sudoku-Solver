import pygame

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
screenHeight = 815
borderColor = (0,0,0)
boardLength = 9
cellSize = 80
numbersDistance = 85
topPadding = 25
leftPadding = 30
font = pygame.font.Font(None, 80)





widthSquareLine = 10
widthCellLine = 5

screen = pygame.display.set_mode((screenWidth, screenHeight))

run = True

def drawCellsLines():
    for i in range(4):
        xSquareLine = i * 270 
        pygame.draw.line(screen, borderColor, (xSquareLine, 0), (xSquareLine, screenHeight), widthSquareLine) 

        ySquareLine = i * 270
        pygame.draw.line(screen, borderColor, (0, ySquareLine), (screenWidth, ySquareLine), widthSquareLine)

    for i in range(10):
        xCellLines = i * 90
        pygame.draw.line(screen, borderColor, (xCellLines, 0), (xCellLines, screenHeight), widthCellLine)
         
        yCellLines = i * 90   
        pygame.draw.line(screen, borderColor, (0, yCellLines), (screenWidth, yCellLines), widthCellLine)
        
        
def drawDefaultNumbers():
    for i in range(boardLength):
        for j in range(boardLength):
            if board[i][j] != 0:
                numberText = font.render(str(board[i][j]), True, borderColor)
                screen.blit(numberText, (leftPadding + j * numbersDistance + widthCellLine * j, topPadding + i * numbersDistance + widthCellLine * i))
    
while run:
    screen.fill((255,255,255))
    drawCellsLines()
    drawDefaultNumbers()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()


def checkKeyPress():
    key = pygame.key.get_pressed()
    if key[pygame.K_1] == True:
        #put 1 in the square
        return True


# def drawCells():
#     leftCoord = 0
#     topCoord = 0
#     for i in range(boardLength):
#         for j in range(boardLength):
#             pygame.draw.rect(screen, borderColor, pygame.Rect(leftCoord, topCoord, cellSize, cellSize), 2)
#             leftCoord += cellSize
#         topCoord += cellSize
#         leftCoord = 0