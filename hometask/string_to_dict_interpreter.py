"""
StringInterpreter class takes a string as input during initialization
and provides a method to get a dictionary with the count of each unique character in the string.

Attributes:
    passed_string (str): The input string provided during initialization.

Methods:
    get_result() -> dict:
        Returns a dictionary with the count of each unique character in the input string.
"""


class StringInterpreter:
    def __init__(self, passed_string: str) -> None:
        """
        Initializes the StringInterpreter with the provided string.

        Parameters:
            passed_string (str): The input string to be processed.
        """
        self.passed_string = passed_string

    def get_result(self) -> dict:
        """
        Returns a dictionary with the count of each unique character in the input string.

        Returns:
            dict: A dictionary with characters as keys and their counts as values.
        """
        char_list = list(self.passed_string)
        char_set = set(char_list)

        return {character: char_list.count(character) for character in char_set}
