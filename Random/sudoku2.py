import unittest
def checkAll():
    return checkRows == True and checkCols == True and checkSquares == True

def checkRows(board):
    return True

def checkCols(board):
    return True
def checkSquares(board):
    return True

class TestStringMethods(unittest.TestCase):

    def testone(self):
        self.assertTrue(checkAll())


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
