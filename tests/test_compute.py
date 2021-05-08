import unittest
from core import compute


class ComputationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.simple_exp = "a+b"
        self.simple_values = {'a': '2', 'b': '3'}
        self.result1 = '5'

        self.big_expression = "a+(b*c*((d^2)/a)-~(e))"
        self.values2 = {'a': '2', 'b': '3', 'c': '4', 'd': '8', 'e': '64'}
        self.result2 = '378'

        self.big_numbers = "((a-b)+c)*d"
        self.values3 = {'a': '2920193810920129831098230192830', 'b': '19884313212139312328923', 'c': '34434545456', 'd': '32423452343456'}
        self.result3 = '94682764217305909120730682857046426186178528'

        self.wrong_expression = "a+(b*c"
        self.values4 = {'a': '2', 'b': '3', 'c': '4'}

        self.wrong_expression2 = "~a"
        self.values5 = {'a': '4'}

        self.expression = "a+b"
        self.wrong_values = {'a': '4', 'b': '4f5'}

        self.expression2 = "a*b+c"
        self.less_values = {'a': '2', 'c': '3'}

        self.test_object = compute.Computation()

    def test_simple_expression(self):
        self.assertEqual(self.test_object.get_result(formula=self.simple_exp, parameters=self.simple_values)[0].number, self.result1)
        self.assertTrue(self.test_object.get_result(formula=self.simple_exp, parameters=self.simple_values)[0].number, self.result1)

    def test_big_expression(self):
        self.assertEqual(self.test_object.get_result(formula=self.big_expression, parameters=self.values2)[0].number, self.result2)
        self.assertTrue(self.test_object.get_result(formula=self.big_expression, parameters=self.values2)[0].number, self.result2)

    def test_big_numbers_expression(self):
        self.assertEqual(self.test_object.get_result(formula=self.big_numbers, parameters=self.values3)[0].number, self.result3)
        self.assertTrue(self.test_object.get_result(formula=self.big_numbers, parameters=self.values3)[0].number, self.result3)

    def test_wrong_expression(self):
        with self.assertRaises(Exception):
            self.test_object.get_result(formula=self.wrong_expression, parameters=self.values4)

    def test_wrong_expression2(self):
        with self.assertRaises(Exception):
            self.test_object.get_result(formula=self.wrong_expression2, parameters=self.values5)

    def test_wrong_values(self):
        with self.assertRaises(ValueError):
            self.test_object.get_result(formula=self.expression, parameters=self.wrong_values)

    def test_less_values(self):
        with self.assertRaises(Exception):
            self.test_object.get_result(formula=self.expression2, parameters=self.less_values)
