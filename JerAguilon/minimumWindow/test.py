import unittest
from window import minWindow 


class TestSum(unittest.TestCase):
 
    def testIfSmallest(self):
        self.assertEquals(minWindow("ADOBECODEBANC","ABC"), "BANC")

    def testIfWindowExists(self):
        result = minWindow("KJKJUHDKS","IPR")
        self.assertEquals(result, "")

if __name__ == '__main__':
    unittest.main()
