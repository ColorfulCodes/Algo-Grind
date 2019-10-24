import unittest
from pyCode import move_zeros

class TestSum(unittest.TestCase):

    # This test should return True and the list
    def testWillMoveZerosandFalse(self):
        result = move_zeros([False,1,0,1,2,0,1,3,"a"])
        self.assertEquals(result, [False,1,1,2,1,3,"a",0,0])

    # This test will only move Zeros and equate False to Zero
    def testOnlyMoveZeros(self):
        self.assertFalse(move_zeros([False,1,0,1,2,0,1,3,"a"])==[1,1,2,1,3,"a",0,0,0])

    # If length is zero return empty brackets
    def testEmptyList(self):
        result = move_zeros([])
        self.assertEquals(result, [])
        
    # If not a list return error
    def test_afunction_throws_error(self):
        with self.assertRaises(ValueError):
            move_zeros('3')

    # This test should assert False for just being wrong
    def testwillNotMoveZeros(self):
        a_list = [False,1,0,0,2,0,1,3,True, 'hello']
        self.assertFalse(move_zeros(a_list) == [1,2,34,5,'hello'])


if __name__ == '__main__':
    unittest.main()
