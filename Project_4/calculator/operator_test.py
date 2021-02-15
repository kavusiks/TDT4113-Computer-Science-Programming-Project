"""Module: Operator """
import unittest

import numpy
from operator_methods import Operator


class TestOperatorMethod(unittest.TestCase):
    """TestCase for 'Operator'"""

    def test_execute(self):
        """Testing execute() in operator."""
        add_op = Operator(numpy.add, 0)
        multiply_op = Operator(numpy.multiply, 1)
        self.assertEqual(
            7,
            add_op.execute(
                1,
                multiply_op.execute(
                    2,
                    3)),
            "Some error occurred in the execute function")
