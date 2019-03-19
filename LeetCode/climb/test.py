import unittest
from cs import climbStairs

class TestSum(unittest.TestCase):

    # This test should work fine
    def testwillWork(self):
        result = climbStairs(4)
        self.assertEquals(result, 5)

    # This test should fail as 5 equals 8 not 7
    def testwillNotWork(self):
        result = climbStairs(5)
        self.assertEquals(result, 7)

if __name__ == '__main__':
    unittest.main()
