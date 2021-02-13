import numbers

import numpy

from Calculator.function import Function
from Calculator.operator import Operator
from Calculator.queue import Queue
from Calculator.stack import Stack


class Calculator:

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

    def calculate(self):
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

    def shunting_yard(self, clean_input_list):
        # shunting_queue = Queue()
        operator_stack = Stack()
        output_queue = Queue()
        # for char in input_string.strip():
        #   shunting_queue.push(char)

        # print(input_string.replace("(", "( ").replace(")", " ) ").split())
        # input_string.replace("(", "( ").replace(")", " ) ").split():

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

    def text_parser(self, input_text):

        text_input_list = input_text.replace("(", "( ").replace(")", " ) ").split()
        #print(text_input_list)
        for i in range(len(text_input_list)):
            if len(text_input_list[i]) > 1 and not text_input_list[i].isnumeric():
                to_be_replaced = text_input_list[i].upper()
                if to_be_replaced in self.operators.keys():
                    text_input_list[i] = self.operators.get(to_be_replaced)
                if to_be_replaced in self.functions.keys():
                    text_input_list[i] = self.functions.get(to_be_replaced)
            elif text_input_list[i].isnumeric():
                text_input_list[i] = float(text_input_list[i])
        #print(text_input_list)
        return text_input_list

    def calculate_expression(self, txt: str):
        self.output_queue = self.shunting_yard(self.text_parser(txt))
        return self.calculate()
