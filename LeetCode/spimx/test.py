import unittest

from spiralMatrix import spiral


class TestSum(unittest.TestCase):
    def test_list_right(self):
        """
        Test that the grid is not empty
        """
        grid = [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        result = spiral(grid)
        self.assertTrue(len(result)>0)

    def test_list_right2(self):
        """
        Test that result is equal to correct answer
        """
        grid = [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        result = spiral(grid)
        self.assertEqual(result,[1,2,3,6,9,8,7,4,5])

    def test_list_wrong(self):
        """
        Test should return with a failure
        """
        grid = [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        result = spiral(grid)
        self.assertEqual(result,[1,2,0,6,9,8,7,7,5])

if __name__ == '__main__':
    unittest.main()
