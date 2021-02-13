import unittest
import numpy
from Calculator.function import Function


class TestFunction(unittest.TestCase):

    def test_execute(self):
        exponential_func = Function(numpy.exp)
        sin_func = Function(numpy.sin)
        self.assertEqual(1, exponential_func.execute(sin_func.execute(0)), "Some error occurred in the execute function")