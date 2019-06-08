import unittest
from Coins import coinChange
class TestSum(unittest.TestCase):
    def test_correctly(self):
        """
        Test there are a minimum of 3 coins for 11
        """

        result = coinChange([1, 2, 5],11)
        self.assertTrue(result == 3)


    def test_incorrectly(self):
        """
        Test failure: there are a minimum of 2 coins for 11.
        """

        result = coinChange([1, 2, 5],11)
        self.assertFalse(result == 2)

    def test_value_error(self):
        """
        Test Value Error gets thrown
        """
        with self.assertRaises(ValueError):
            coinChange([],11)


if __name__ == '__main__':
    unittest.main()
