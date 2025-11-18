from calc import Calc
import unittest

class Test_Calc(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        return super().setUpClass()
    
    def setUp(self):
        self.calc = Calc(8)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(2),4)
    
    def test_mult(self):
        self.assertEqual(self.calc.multiply(2),16,"проверка ")

    def test_fail(self):
        self.assertEqual(self.calc.multiply(2),4,"фуууу не грамотный")
    
