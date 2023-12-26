"""
TernaryInterpreter class interprets two values x and y using a ternary expression
to determine the result based on certain conditions.

Attributes:
    x (int): The first input value.
    y (int): The second input value.

Methods:
    get_result() -> int | str:
        Returns the result of the ternary expression based on the values of x and y.
"""


class TernaryInterpreter:
    def __init__(self, passed_x: int, passed_y: int):
        """
        Initializes the TernaryInterpreter with two input values.

        Parameters:
            passed_x (int): The first input value.
            passed_y (int): The second input value.
        """
        self.x = passed_x
        self.y = passed_y

    def get_result(self) -> int | str:
        """
        Returns the result of the ternary expression based on the values of x and y.

        Returns:
            int | str: The result of the ternary expression.
        """
        x = self.x
        y = self.y
        return ("game over" if (x == 0 and y == 0) else
                (x + y if x < y else
                 (x - y if x > y else 0)))
