import unittest
from src.exercise1 import *

class TestExercise1(unittest.TestCase):
    
    def test_APINotReturnEmpty(self):
        self.assertIsNotNone(get30Entries)
        self.assertIsNot(get30Entries(), [])

    def test_correctLength(self):
        self.assertEqual(len(get30Entries()),30)

    def test_ArrayFilter(self):
        array = [{'by': 'nickwritesit', 'descendants': 77, 'id': 35886243, 'kids': [ 35897193, 35890438], 'score': 77, 'time': 1683720929, 'title': 'I have 4 words', 'type': 'story', 'url': 'https://tedgioia.substack.com/p/the-decline-and-fall-of-the-hit-instrumental'}, {'by': 'benbreen', 'descendants': 1, 'id': 35884305, 'kids': [35898728], 'score': 50, 'time': 1683700160, 'title': 'I have 5 words test', 'type': 'story', 'url': 'https://www.laphamsquarterly.org/roundtable/lower-your-expectations'}, {'by': 'nhourcard', 'id': 35893439, 'score': 1, 'time': 1683752410, 'title': 'I have 6 words test test', 'type': 'job', 'url': 'https://questdb.io/careers/technical-content-lead/'}]   
        self.assertEqual(len(filterByTitle(array)),1)

if __name__ == '__main__':
    unittest.main()