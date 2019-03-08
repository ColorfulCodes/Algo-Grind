import unittest

from tobe import spiral


class TestSum(unittest.TestCase):
    def test_list_right(self):
        """
        Test that it can sum a list of integers
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
        Test that it can sum a list of integers
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
