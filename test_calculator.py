import unittest
from custom_calculator import string_calculator


class TestStringCalculator(unittest.TestCase):

    def test_string_calculator(self):
        input_string = "1,2,3,4,5"
        self.assertEqual(string_calculator(input_string), 15)
