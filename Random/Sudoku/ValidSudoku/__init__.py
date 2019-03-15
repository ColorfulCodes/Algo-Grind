# One leetcode a day keeps unemployment away
class Sudoku_Checker:
  def __init__(self,board):
    self.board = board

  def board_validater(self,board):
    # self.checkRows(board)
    # self.checkCols(board)
    self.checkSquares(board)

    return self.checkRows(board) == True and self.checkCols(board) == True and self.checkSquares(board) == True

  def checkRows(self,board):
    #   compare = [1,2,3,4,5,6,7,8,9]
    #   for i in self.board:
    #       print sorted(i)
    #       if sorted(i) == compare:
    #           continue
    #       else:
    #           return False
       return True

  def checkCols(self,board):
    #   compare = [1,2,3,4,5,6,7,8,9]
    #   hold = []
    #   for i in range(len(board)):
    #       for j in range(len(board[0])):
    #           hold.append(board[j][i])
    #       if sorted(hold) == compare:
    #           hold = []
    #           continue
    #       else:
    #           return False
      return True

  def checkSquares(self,board):
      hold = []
      t = 3
      p=0
      for i in range(p,t):
          for j in range(p,t):
              hold.append(board[j][i])
          p +=3
          t+=3

      return True

board = [  [5, 3, 4, 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 0],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 9]]
s = Sudoku_Checker(board)
s.board_validater(board)
