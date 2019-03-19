class Sudoku_Checker:
  def __init__(self,board):
    self.board = board

  def board_validater(self,board):
    return self.checkRows(board) == True and self.checkCols(board) == True and self.checkSquares(board) == True

  def compareAll(self,a):
      compare = range(1,10)
      return sorted(a) == compare
      
  def checkRows(self,board):
      for i in self.board:
          if not self.compareAll(i):
              return False
      return True

  def checkCols(self,board):
      for i in range(len(board)):
          hold = []
          for j in range(len(board[0])):
              hold.append(board[j][i])
          if not self.compareAll(hold):
              return False
      return True

  def checkSquares(self,board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not self.compareAll(nums):
                return False
    return True


board = [  [5, 3, 4, 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 9]]
s = Sudoku_Checker(board)
print s.board_validater(board)
