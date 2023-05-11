import unittest
from src.exercise1 import *

class TestExercise1(unittest.TestCase):
    
    def test_APINotReturnEmpty(self):
        self.assertIsNotNone(get30Entries)
        self.assertIsNot(get30Entries(), [])

    def test_correctLength(self):
        self.assertEqual(len(get30Entries()),30)

if __name__ == '__main__':
    unittest.main()