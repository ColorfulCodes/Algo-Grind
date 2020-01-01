# This is the method I prefer most for DFS. Very Readable.

def floodfill(grid,row,col,newColor):
    oldColor= grid[row][col]
    if newColor == oldColor:
        return grid

    recurse(grid,row,col,newColor,oldColor)
    return grid

def recurse(grid,row,col,newColor,oldColor):
    if grid[row][col]!= oldColor:
        return

    grid[row][col] = newColor

    if row !=0:
        recurse(grid,row-1,col,newColor,oldColor)

    if col !=0:
        recurse(grid,row,col-1,newColor,oldColor)
    
    if row != len(grid)-1:
        recurse(grid,row+1,col,newColor,oldColor)

    if col != len(grid[0])-1:
        recurse(grid,row,col+1,newColor,oldColor)

    


floodfill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)

# Method 2 not done by me but using list comprehention 
# def floodfill(image,row,col,newColor):
#     oriCol = image[row][col]
#     if oriCol == newColor: return image
#     row, col, surs = len(image), len(image[0]), [(row, col)]
#     while surs:
#         for i, j in surs: image[i][j] = newColor
#         surs = [(x, y) for i, j in surs for x, y in 
#                  [(i+1, j), (i-1, j), (i, j-1), (i, j+1)] 
#                  if 0<=x<row and 0<=y<col 
#                  and image[x][y] == oriCol]
#     return image

# floodfill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)


# Method 3 also not done by me. 

# def floodfill(image,row,col,newColor):
#     r, c = len(image), len(image[0])
#     color = image[row][col]
#     def dfs(i, j):
#         if i < 0 or i>=r or j < 0 or j >= c:
#             return
#         if image[i][j] == newColor or image[i][j] != color:
#             return
#         image[i][j] = newColor
#         dfs(i+1, j)
#         dfs(i-1, j)
#         dfs(i,j+1)
#         dfs(i, j-1)
#     dfs(row, col)
#     return image
# floodfill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
