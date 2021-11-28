"""Module: Calculator """
import unittest

from main_calculator import Calculator


class TestCalculator(unittest.TestCase):
    """TestCase for 'Calculator'"""

    def test_execute(self):
        """Testing the execute method in 'Functions and 'Operator'. """
        calc = Calculator()
        self.assertEqual(
            1096.63,
            round(
                calc.functions['EXP'].execute(
                    calc.operators['PLUS'].execute(
                        1,
                        calc.operators['MULTIPLY'].execute(
                            2,
                            3))),
                2),
            "Some error occurred in the execute function")

    def test_evaluate_output_queue(self):
        """Testing evaluate output queue method"""
        calc = Calculator()
        rpn_notation = [
            1,
            2,
            3,
            calc.operators.get('MULTIPLY'),
            calc.operators.get('ADD'),
            calc.functions.get('EXP')]
        for elem in rpn_notation:
            calc.output_queue.push(elem)
        self.assertEqual(
            1096.63,
            round(
                calc.evaluate_output_queue(),
                2),
            "Some error occurred in the execute function")

        calc.output_queue = calc.shunting_yard(
            calc.parse_text("EXP (1 add 2 multiply 3)"))
        for i in range(calc.output_queue.size()):
            print(calc.output_queue.pop())
        # calc.calculate()

    def test_shunting_yard(self):
        """Testing shunting yard method"""
        calc = Calculator()
        # Test1
        print("Test1")
        test_output = calc.shunting_yard([calc.functions.get(
            'EXP'), '(', 1, calc.operators.get('ADD'), 2, calc.operators.get('MULTIPLY'), 3, ')'])
        test_check = [
            1,
            2,
            3,
            calc.operators.get('MULTIPLY'),
            calc.operators.get('ADD'),
            calc.functions.get('EXP')]
        for i in range(test_output.size()):
            error_message = "The element on index " + str(i) + " is worng"
            print("Expected:", test_check[i], "Actual", test_output.peek())
            self.assertEqual(test_check[i], test_output.pop(), error_message)

        # Test2
        print("")
        print("Test2")
        test_output = calc.shunting_yard(
            [2, calc.operators.get('MULTIPLY'), 3, calc.operators.get('ADD'), 1])
        test_check = [2, 3, calc.operators.get(
            'MULTIPLY'), 1, calc.operators.get('ADD')]
        for i in range(test_output.size()):
            error_message = "The element on index " + str(i) + " is worng"
            print("Expected:", test_check[i], "Actual", test_output.peek())
            self.assertEqual(test_check[i], test_output.pop(), error_message)
        #print(calc.shunting_yard(calc.text_parser("EXP (1 add 2 multiply 3)")))

    def test_parse_text(self):
        """Testing parse text method"""
        calc = Calculator()
        print(calc.parse_text("EXP (1 add 2 multiply 3)"))
        self.assertEqual([2, calc.operators.get("MULTIPLY"), 3, calc.operators.get(
            "ADD"), 1], calc.parse_text("2 multiply 3 add 1"))

    def test_calculate_by_expression(self):
        """Test calculate by expression method"""
        calc = Calculator()
        print(calc.calculate_by_expression("Tester: EXP (1 add 2 multiply 3)"))
        self.assertEqual(
            1096.63,
            round(
                calc.calculate_by_expression("EXP (1 add 2 multiply 3)"),
                2),
            "calculate_expression() failed")
        print("")
        self.assertEqual(
            5,
            calc.calculate_by_expression("((15 DIVIDE (7 SUBTRACT (1 ADD 1)))"
                                         " Multiply 3) Subtract (2 add (1 add 1))"),
            "calculate_expression() failed")
