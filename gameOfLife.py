#todo: printboard function, neighbors function
#welcome message
print("Welcome to Conway's Game of Life. We start with a 30x60 grid of cells, either alive or dead. Here are the rules: \n  1) Any live cell with fewer than two live neighbors dies, as if by underpopulation. \n  2) Any live cell with two or three live neighbors lives on to the next generation. \n 3) Any live cell with more than three live neighbors dies, as if by overpopulation. \n  4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.")
#empty grid - 30x60
grid = []
for i in range(30):
  line = []
  for j in range(60):
    line.append(False)
  grid.append(line)


def printBoard(currentGen):
  for row in currentGen:
    for boolean in row:
      if not boolean:
        print("-", end = "")
      else:
        print("o", end = "")
        
    print("")
    



f = open("design1.txt")
text = f.readlines()
text = [item.strip() for item in text]
f.close()
  
coordinates = []
for coordinate in text:
  coordinates.append(coordinate.split())
  
for i in range(len(coordinates)):
  grid[int(coordinates[i][0])][int(coordinates[i][1])] = True


printBoard(grid)
#make coordinate points True from the files in the grid - done
#make the welcome message from instructions - done 
#try the neighbors functions from conways rules
#looping through every single value



def checkLiveCells(currentGrid, row, column):#function to check how many cells around are alive
  
  liveCellsAround = 0
  
  #top left
  if row - 1 >= 0 and column - 1 >= 0 and currentGrid[row - 1][column -1 ]:
    liveCellsAround += 1 
    
  #top middle
  if row - 1 >= 0 and currentGrid[row - 1][column]:
    liveCellsAround += 1

  #top right
  if row - 1 >= 0 and column + 1 < len(currentGrid[0]) and currentGrid[row - 1][column + 1]:
    liveCellsAround += 1

  #middle left
  if column - 1 >= 0 and currentGrid[row][column - 1]:
    liveCellsAround += 1 

  #middle right
  if column + 1 < len(currentGrid[0]) and currentGrid[row][column + 1]:
    liveCellsAround += 1

  #bottom left
  if row + 1 < len(currentGrid) and column - 1 >= 0 and currentGrid[row + 1][column - 1]:
    liveCellsAround += 1 
    
  #bottom middle
  if row + 1 < len(currentGrid) and currentGrid[row + 1][column]:
    liveCellsAround += 1

  #bottom right
  if row + 1 < len(currentGrid) and column + 1 < len(currentGrid[0]) and currentGrid[row + 1][column + 1]:
    liveCellsAround += 1
  return liveCellsAround



def neighbors(currentGrid, isAlive, row, column):

  amount = checkLiveCells(currentGrid, row, column)

  if isAlive:#if it is alive
    
    if amount < 2:
      return False
    elif amount > 3:
      return False
    else:
      return True
  
  else:#if it is dead
    
    if amount == 3:
      return True
    else:
      return False
'''
for i in range(len(grid)):
  for j in range(len(grid[0])):
    value = grid[i][j] #gives me if its true or false, alive or dead and stores it
    grid[i][j] = neighbors(grid, value, i, j)



print("\n")
printBoard(grid)
'''
#takes in a cells, and returns if it dies or lives (booleans)


while True:
  gen = 1
  
  cont = input("Continue to the next generation?(type yes or no) ")
  if cont == "yes":
    gen =+ 1
    for j in range(len(grid)):
      for l in range(len(grid[0])):
        value = grid[j][l]
        grid[i][j] = neighbors(grid, value, i, j)

    print("\n gen " + str(i+2))
    printBoard(grid)
  else:
    break
