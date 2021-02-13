import numpy
from Calculator.queue import Queue
from Calculator.function import Function
from Calculator.operator import Operator


class Calculator:

    def __init__(self):
        # Define the functions supported byt linking them to Python
        # functions. These can be made elsewhere in the program,
        # or imported (e.g., from numpy)
        self.functions = { 'EXP': Function(numpy.exp),
                           'LOG': Function(numpy.log),
                           'SIN': Function(numpy.sin),
                           'COS': Function(numpy.cos),
                           'SQRT': Function(numpy.sqrt)}

        # Define the operators supported.
        # Link them to Python functions (here: from numpy)
        self.operators = {'ADD': Operator(numpy.add, 0),
                          'MULTIPLY': Operator(numpy.multiply, 1),
                          'DIVIDE': Operator(numpy.divide, 1),
                          'SUBTRACT': Operator(numpy.subtract, 0),
                          'PLUS': Operator(numpy.add, 0),
                          'TIMES': Operator(numpy.multiply, 1),
                          'MINUS': Operator(numpy.subtract, 0)
                          }

        # Define the output-queue.
        # The parse_text method fills this with RPN.
        # The evaluate_output_queue method evaluates it
        self.output_queue = Queue()

