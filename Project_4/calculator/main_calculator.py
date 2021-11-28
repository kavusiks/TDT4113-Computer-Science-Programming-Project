"""Module: Calculator """
import numbers

from queue import Queue
from stack import Stack
import numpy
from function_methods import Function
from operator_methods import Operator


class Calculator:
    """The main class for this application"""

    def __init__(self):
        # Define the functions supported byt linking them to Python
        # functions. These can be made elsewhere in the program,
        # or imported (e.g., from numpy)
        self.functions = {'EXP': Function(numpy.exp),
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

    def evaluate_output_queue(self):
        """Method used to calculate a result from the output queue."""
        intermediate_stack = Stack()

        while not self.output_queue.is_empty():
            print(self.output_queue.is_empty())
            print(self.output_queue.peek())
            next_item = self.output_queue.peek()
            if isinstance(next_item, numbers.Number):
                intermediate_stack.push(self.output_queue.pop())
            elif isinstance(next_item, Function):
                intermediate_stack.push(
                    self.output_queue.pop().execute(intermediate_stack.pop()))
            elif isinstance(next_item, Operator):
                item1 = intermediate_stack.pop()
                print(item1)
                item2 = intermediate_stack.pop()
                print(item2)
                intermediate_stack.push(
                    self.output_queue.pop().execute(item2, item1))

        return intermediate_stack.pop()

    @staticmethod
    def shunting_yard(clean_input_list):
        """Method used to convert from "normal" notion to RPN.
        This method uses the logic from the shunting-yard algorithm. """
        operator_stack = Stack()
        output_queue = Queue()

        for elem in clean_input_list:
            if isinstance(elem, numbers.Number):
                output_queue.push(elem)
            elif isinstance(elem, Function):
                operator_stack.push(elem)
            elif elem == '(':
                operator_stack.push(elem)
            elif elem == ')':
                while operator_stack.peek() != '(':
                    output_queue.push(operator_stack.pop())
                    if operator_stack.is_empty():
                        break
                operator_stack.pop()
            elif isinstance(elem, Operator):
                while not operator_stack.is_empty():
                    peek_on_operator = operator_stack.peek()
                    if isinstance(peek_on_operator, Operator):
                        if peek_on_operator.get_strength() < elem.get_strength():
                            operator_stack.push(elem)
                            break
                        output_queue.push(operator_stack.pop())
                    elif peek_on_operator == '(':
                        operator_stack.push(elem)
                        break
                    else:
                        output_queue.push(operator_stack.pop())

                if operator_stack.is_empty():
                    operator_stack.push(elem)

        while not operator_stack.is_empty():
            output_queue.push(operator_stack.pop())

        print(output_queue)
        return output_queue

    def parse_text(self, input_text):
        """Method used to convert an input string to a list,
         containing each individual element from the string."""

        text_input_list = input_text.replace(
            "(", "( ").replace(")", " ) ").split()
        # print(text_input_list)
        for i in range(len(text_input_list)):
            if len(
                    text_input_list[i]) > 1 and not text_input_list[i].isnumeric():
                to_be_replaced = text_input_list[i].upper()
                if to_be_replaced in self.operators.keys():
                    text_input_list[i] = self.operators.get(to_be_replaced)
                if to_be_replaced in self.functions.keys():
                    text_input_list[i] = self.functions.get(to_be_replaced)
            elif text_input_list[i].isnumeric():
                text_input_list[i] = float(text_input_list[i])
        # print(text_input_list)
        return text_input_list

    def calculate_by_expression(self, txt: str):
        """Method used to calculate directly from input string.
        This method puts every part together."""
        self.output_queue = self.shunting_yard(self.parse_text(txt))
        return self.evaluate_output_queue()
