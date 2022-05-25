import unittest
import random
from calculator import Calculator

class TestCalculatorMethods(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(3,3), 6, "answer should be 6")
        
    def test_sub(self):
        self.assertEqual(self.calc.subtract(3,3), 0, "answer should be 0")
        
    def test_isPrime(self):
        self.assertTrue(self.calc.isPrime(2))
        self.assertFalse(self.calc.isPrime(25))
        self.assertTrue(self.calc.isPrime(11))
    
if __name__ == '__main__':
    unittest.main