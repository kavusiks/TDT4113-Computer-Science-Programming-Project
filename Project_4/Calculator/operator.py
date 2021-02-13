import numbers


class Operator:
    def __init__(self, operation, strength: int):
        self.opr = operation
        self.strength = strength

    def execute(self, element1, element2, debug=True):
        # Check type
        if not (isinstance(element1, numbers.Number) or isinstance(element2, numbers.Number)):
            raise TypeError("The elements must be a number")
        result = self.opr(element1, element2)

        # Report
        if debug is True:
            print("Function: " + self.opr.__name__ + "({:f}) = {:f}".format(element1, element2, result))
            return result

    def get_strength(self):
        return self.strength
