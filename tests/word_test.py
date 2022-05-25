import unittest
from word import TextInfo


class TestWordMethods(unittest.TestCase):
    def setUp(self):
        self.wrd = TextInfo()
    
    def test_vowels(self):
        self.assertGreater(self.wrd.count_vowels('hello world'), True, 'there are vowels present')
        
    def test_cons(self):
        self.assertGreater(self.wrd.count_cons('hello world'), True, 'there are consonants present')
    
    
if __name__ == '__main__':
    unittest.main