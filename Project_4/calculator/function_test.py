"""Module: Function """
import unittest

import numpy
from function_methods import Function


class TestFunctionMethod(unittest.TestCase):
    """TestCase for 'Function'"""

    def test_execute(self):
        """Testing execute() in function."""
        exponential_func = Function(numpy.exp)
        sin_func = Function(numpy.sin)
        self.assertEqual(
            1,
            exponential_func.execute(
                sin_func.execute(0)),
            "Some error occurred in the execute function")
