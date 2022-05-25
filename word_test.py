import unittest
from word import TextInfo


class TestWordMethods(unittest.TestCase):
    def setUp(self):
        self.wrd = TextInfo()
    
    def test_vowels(self):
        self.assertEqual(self.wrd.count_vowels('hello world'), 3, 'there should be 2 vowels.')
        
    def test_cons(self):
        self.assertEqual(self.wrd.count_cons('hello world'), 7, 'there should be 7 consonants.')
    
    
if __name__ == '__main__':
    unittest.main