# One leetcode a day keeps unemployment away
class Sudoku_Checker:
  def __init__(self,board):
    self.board = board

  def board_validater(self):
    self.checkRows(self.board)
    self.checkCols(self.board)
    self.checkSquares(self.board)

    return checkRows() == True and checkCols() == True and checkSquares() == True

  def checkRows(self):
      # compare = [1,2,3,4,5,6,7,8,9]
      # for i in self.board:
      #     if i.sort() == compare:
      #         continue
      #     else:
      #         return False
      return True

  def checkCols(self):
      return False

  def checkSquares(self):
      return True
# s = Sudoku_Checker()
# s.board_validater([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ])
