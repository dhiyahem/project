#work in progress

print("Welcome to Conway's 2-Player Game of Life. We start with a 10x10 grid of cells, either alive or dead.\n Here are the rules:")
print(" Each player starts with a square. Each turn they get to pick a position to grow a cell and pick a position to kill an opponent cell. Each generation passes by following these rules:")
print(" 1) Any live cell with fewer than two live neighbors dies, as if by underpopulation. \n 2) Any live cell with two or three live neighbors lives on to the next generation. \n  3) Any live cell with more than three live nieghbors dies as if by overpopulation. \n  4) Any dead cell with exactly three live neighbors becomes a live cell as if by reproduction.")
print("Press Enter to continue: ")
grid = []#makes the grid
for i in range(10):
  line = []
  for i in range(10):
    line.append(False)
  grid.append(line)

def printBoard(currentGrid):#function to print the thing
  print("  0 1 2 3 4 5 6 7 8 9")
  for i in range(10):
    print(i, end = "")
    for j in range(len(currentGrid[i])):
      if currentGrid[i][j] == False:
        print(" -" , end = "")
      elif currentGrid[i][j] == 1:
        print(" O", end = "")
      elif currentGrid[i][j] == 2:
        print(" X", end = "")
    print("")


def replace(file, currentGrid, player):
  f = open(file)
  text = f.readlines()
  text = [item.strip() for item in text]
  f.close()
  
  coordinates = []
  for coordinate in text:
    coordinates.append(coordinate.split())
    
  for i in range(len(coordinates)):
    currentGrid[int(coordinates[i][0])][int(coordinates[i][1])] = player

replace("player1.in", grid, 1)
replace("player2.in", grid, 2)
printBoard(grid)

def count(currentGrid):
  player1Count = 0
  player2Count = 0
  for i in range(len(currentGrid)):
    for j in range(len(currentGrid[i])):
      if currentGrid[i][j] == 1:
        player1Count += 1
      elif currentGrid[i][j] == 2:
        player2Count += 1
  return player1Count, player2Count

player1, player2 = count(grid)

def countAlive(currentGrid, player, row, column):
  number = player
  aliveCellsAround = 0
  if row - 1 >= 0 and column - 1 >= 0 and currentGrid[row - 1][column -1 ] == number:
    aliveCellsAround += 1

  #top middle
  if row - 1 >= 0 and currentGrid[row - 1][column] == number:
    aliveCellsAround += 1

  #top right
  if row - 1 >= 0 and column + 1 < len(currentGrid[0]) and currentGrid[row - 1][column + 1] == number:
    aliveCellsAround += 1

  #middle left
  if column - 1 >= 0 and currentGrid[row][column - 1] == number:
    aliveCellsAround += 1
    
  #middle right
  if column + 1 < len(currentGrid[0]) and currentGrid[row][column + 1] == number:
    aliveCellsAround += 1

  #bottom left
  if row + 1 < len(currentGrid) and column - 1 >= 0 and currentGrid[row + 1][column - 1] == number:
    aliveCellsAround += 1
 
  #bottom middle
  if row + 1 < len(currentGrid) and currentGrid[row + 1][column] == number:
    aliveCellsAround += 1

  #bottom right
  if row + 1 < len(currentGrid) and column + 1 < len(currentGrid[0]) and currentGrid[row + 1][column + 1] == number:
    aliveCellsAround += 1

  return aliveCellsAround

#todo: finish for loop, finish while loop, hope it works lmao
def neighbors(currentGrid, ifAlive, row, column):
  player1Amount = countAlive(currentGrid, 1, row, column)
  player2Amount = countAlive(currentGrid, 2, row, column)
  if player1Amount > 2:
    print("The amount of amount around is: " + str(player1Amount) + "\nThe player number is: 1\nThe row and column are: " + str(row) + " " + str(column) + "\nThe status of this cell is " + str(ifAlive) + "\n")
  if player2Amount > 2:
    print("The amount of amount around is: " + str(player2Amount) + "\nThe player number is: 2\nThe row and column are: " + str(row) + " " + str(column) + "\nThe status of this cell is " + str(ifAlive) + "\n")
    
  if ifAlive == False:
    
    if player1Amount == 3:
      return 1
      print("hello")
    elif player2Amount == 3:
      return 2
      print("hello")
  elif ifAlive == 1 or ifAlive == 2:
    if player1Amount < 2:
      return False
    elif player2Amount < 2:
      return False
    
    elif player1Amount > 3:
      return False
    elif player2Amount > 3:
      return False
    else:
      if player1Amount < 4 and player1Amount > 1:
        return 1
      elif player2Amount < 4 and player2Amount >1:
        return 2
  return False

printBoard(grid)
start = input("Press Enter to Start")
for i in range(len(grid)):
    for j in range(len(grid[0])):
      value = grid[i][j]

      grid[i][j] = neighbors(grid, value, i, j)
      if grid[i][j]:
        print(grid[i][j])
      
printBoard(grid)
'''
while True:
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      value = grid[i][j]
      grid[i][j] = neighbors(grid, value, i, j)
  
      
  player1, player2 = count(grid)
  
  print()
'''
