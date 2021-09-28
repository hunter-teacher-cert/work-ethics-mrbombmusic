import random

def createGrid(rows, cells):
    grid = []
    for i in range(rows):
        row = [' ']*cells
        grid.append(row)
    return grid

def printGrid(grid):
    for row in range(len(grid)):
        for cell in range(len(grid[0])):
            print(grid[row][cell], end="")
        print("")

def setCell(grid, row, cell, val):
    grid[row][cell] = val


def setGrid(grid, numCells):
    for cell in range(numCells):
        randomRow = random.randint(0, len(grid) - 1)
        randomCell = random.randint(0, len(grid[0]) - 1)
        while grid[randomRow][randomCell] == "X":
            randomRow = random.randint(0, len(grid) - 1)
            randomCell = random.randint(0, len(grid[0]) - 1)
        grid[randomRow][randomCell] = "X"
    return grid

def checkNeighbor(grid, r, c):
    cellToCheck = grid[r][c]
    numOfLiveCells = 0
    for rowOffset in range(-1, 2):
        for cellOffset in range(-1, 2):
            if rowOffset != 0 or cellOffset != 0:
                numOfLiveCells += isCellDead(grid, r + rowOffset, c + cellOffset)
    return numOfLiveCells


def isCellDead(grid, r, c):
    if r < 0 or r > len(grid) - 1:
        return 0
    elif c < 0 or c > len(grid[r]) - 1:
        return 0
    elif grid[r][c] == 'X':
        return 1
    else:
        return 0

def getNextGenCell(grid, r, c):
    cellValue = checkNeighbor(grid, r, c)
    newCellValue = ''
    if grid[r][c] == 'X':
        if cellValue <= 1:
            newCellValue = ' '
        elif cellValue >= 4:
            newCellValue = ' '
        elif cellValue == 2 or cellValue == 3:
            newCellValue = 'X'
    else:
        if cellValue == 3:
            newCellValue = 'X'
        else:
            newCellValue = ' '
    return newCellValue

def generateNewGrid(grid):
    newGrid = createGrid(len(grid), len(grid[0]))
    for row in range(len(grid)):
        for cell in range(len(grid[0])):
            newGrid[row][cell] = getNextGenCell(grid, row, cell)
    return newGrid


grid = createGrid(10, 10)
setGrid(grid, 20)
# setCell(grid, 2,2, "X")
# setCell(grid, 2,3, "X")
# setCell(grid, 2,4, "X")
printGrid(grid)
print("--------------------------")
for i in range(20):
    print("Generation " + str(i) +": ")
    grid = generateNewGrid(grid)
    printGrid(grid)
    print("--------------------------")
