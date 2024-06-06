import unittest
from custom_calculator import sum_of_string


class TestSumOfString(unittest.TestCase):

    def test_sum_of_string(self):
        input_string = "1,2,3,4,5"
        self.assertEqual(sum_of_string(input_string), 15)
