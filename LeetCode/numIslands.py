def island(grid):
  if len(grid) == 0:
    return 0

  row= len(grid)
  col =len(grid[0])
  count = 0


  for i in range(row):
    for j in range(col):
      if grid[i][j] == 1:
        dfs(grid,row,col,i,j)
        count += 1
  return count

def dfs(grid,row,col,x,y):
  if grid[x][y] == 0:
    return
  grid[x][y] = 0

  if x != 0:
      dfs(grid,row,col,x-1,y)
  if x != row-1:
      dfs(grid,row,col,x+1,y)

  if y != 0:
      dfs(grid,row,col,x ,y-1)
  if y != col -1:
      dfs(grid,row,col,x,y+1)


island([[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]])
