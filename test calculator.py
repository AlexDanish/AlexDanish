import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(3,6), 9)
    def test_subtruct(self):
        self.assertEqual(self.calculator.subtruct(6,3), 2)
    def test_muliply(self):
        self.assertEqual(self.calculator.muliply(3,6), 18)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(6,3), 2)
if name == "main":
    unittest.main()
                    