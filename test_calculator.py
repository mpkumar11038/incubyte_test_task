import unittest
from custom_calculator import string_calculator


class TestStringCalculator(unittest.TestCase):

    def test_string_calculator(self):
        input_string = "1,2,3,4,5"
        self.assertEqual(string_calculator(input_string), 15)

    def test_string_calculator_with_empty_input(self):
        input_string = ""
        self.assertEqual(string_calculator(input_string), 0)

    def test_string_calculator_with_new_lines(self):
        input_string = "1\n2\n3\n"
        self.assertEqual(string_calculator(input_string), 6)