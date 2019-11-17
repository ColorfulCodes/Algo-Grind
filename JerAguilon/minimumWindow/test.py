import unittest
from window import minWindow 


class TestSum(unittest.TestCase):
 
    def testIfSmallest(self):
        self.assertEquals(minWindow("ADOBECODEBANC","ABC"), "BANC")

    def testIfNotSmallest(self):
        self.assertFalse(minWindow("ADOBECODEBANC","ABC") == "ADOBEC")

    def testIfSmallestSame(self):
        result = minWindow("KJKJUHDKS","KJKJUHDKS")
        self.assertEquals(result, "KJKJUHDKS")
    
    def testIfWindowExists(self):
        result = minWindow("KJKJUHDKS","IPT")
        self.assertEquals(result, "")

    

if __name__ == '__main__':
    unittest.main()
