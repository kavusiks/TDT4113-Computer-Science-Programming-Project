import unittest
from Calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_execute(self):
        calc = Calculator()
        self.assertEqual(1096.63, round(calc.functions['EXP'].execute(calc.operators['PLUS'].execute(1, calc.operators['MULTIPLY'].execute(2, 3))), 2), "Some error occurred in the execute function")