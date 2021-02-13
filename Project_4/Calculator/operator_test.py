import unittest
import numpy
from Calculator.operator import Operator


class TestOperator(unittest.TestCase):

    def test_execute(self):
        add_op = Operator(numpy.add, 0)
        multiply_op = Operator(numpy.multiply, 1)
        self.assertEqual(7, add_op.execute(1, multiply_op.execute(2, 3)), "Some error occurred in the execute function")