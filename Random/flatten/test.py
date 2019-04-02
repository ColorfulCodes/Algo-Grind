import unittest
from flat import flatter

class TestDict(unittest.TestCase):

    def testifworks(self):
        dict = {
                "key1":1,
                "key2": {
                    'a': 2,
                    'b': 3,
                    'c': {
                        'd': 3,
                        'e': '1'
                }
            }
        }
        result = flatter(dict)
        self.assertTrue(result)
