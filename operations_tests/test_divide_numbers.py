import unittest
import sys, os
if os.name == 'posix':
    sep = '/'
else:
    sep = '\\'
sys.path.append(os.getcwd().rsplit(sep,1)[0])
from core import operations
from operations_tests.util_decorators import timeout

class FunctionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.big_positive_number_1 = "19884313212139312328923"
        self.big_positive_number_2 = "2920193810920129831098230192830"
        self.result_divide_1 = "146859173"
        self.result_divide_2 = "0"

        self.big_positive_number_3 = "10000000000000000000000000"
        self.big_positive_number_4 = "90000000000000000000000000000000000000000000000000"
        self.result_divide_3 = "9000000000000000000000000"
        self.result_divide_4 = 0

        self.small_positive_number_1 = "73912873"
        self.small_positive_number_2 = "831212"
        self.result_divide_5 = "88"
        self.result_divide_6 = "0"

        self.small_positive_number_3 = "80201"
        self.small_positive_number_4 = "932"
        self.result_divide_7 = "86"
        self.result_divide_8 = "0"

        self.very_big_positive_number_1 = "123" * 100
        self.very_big_positive_number_2 = "256" * 101
        self.result_divide_9 = '2081'
        self.result_divide_10 = '0'
        self.very_big_positive_number_3 = "1938" * 10000
        self.very_big_positive_number_4 = "256" * 10101
        self.result_divide_11 = '7563498537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353735373537353'
        self.result_divide_12 = '0'

        self.negative_number_1 = "-1329320320"
        self.negative_number_2 = "-372392729"

        self.positive_number_1 = "123903123312"
        self.positive_number_2 = "2312931231233123"

        self.wrong_char_number_1 = "dq3282023ds"
        self.wrong_char_number_2 = "dsajdl3228320das"

        self.test_object = operations.Operations()

    @timeout(30)
    def test_small_positive_numbers(self):

        self.assertEqual(self.test_object.divide_numbers(first_number=self.small_positive_number_1,
                                                         second_number=self.small_positive_number_2),
                         self.result_divide_5)

        self.assertTrue(self.test_object.divide_numbers(first_number=self.small_positive_number_2,
                                                        second_number=self.small_positive_number_1),
                        self.result_divide_6)

        self.assertEqual(self.test_object.divide_numbers(first_number=self.small_positive_number_3,
                                                         second_number=self.small_positive_number_4),
                         self.result_divide_7)

        self.assertTrue(self.test_object.divide_numbers(first_number=self.small_positive_number_4,
                                                        second_number=self.small_positive_number_3),
                        self.result_divide_8)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            self.test_object.divide_numbers(first_number=self.big_positive_number_1,
                                            second_number='0')

        with self.assertRaises(ValueError):
            self.test_object.divide_numbers(first_number=self.big_positive_number_3,
                                            second_number='0')

    # def test_negative_numbers(self):
    #
    #     #aici neaparat de verificat
    #     try:
    #         self.test_object.divide_numbers(first_number=self.negative_number_1,
    #                                         second_number=self.negative_number_2)
    #     except Exception as e:
    #         print(e)
    #         print(type(e))
    #     with self.assertRaises(ValueError):
    #         self.test_object.divide_numbers(first_number=self.negative_number_1,
    #                                         second_number=self.negative_number_2)
    #
    #     with self.assertRaises(ValueError):
    #         self.test_object.divide_numbers(first_number=self.negative_number_1,
    #                                         second_number=self.positive_number_1)
    #
    #     with self.assertRaises(ValueError):
    #         self.test_object.divide_numbers(first_number=self.negative_number_2,
    #                                         second_number=self.positive_number_1)
    #
    #     with self.assertRaises(ValueError):
    #         self.test_object.divide_numbers(first_number=self.negative_number_1,
    #                                         second_number=self.positive_number_2)
    #
    #     with self.assertRaises(ValueError):
    #         self.test_object.divide_numbers(first_number=self.negative_number_2,
    #                                         second_number=self.positive_number_2)

    def test_wrong_numbers(self):

        #de facut si ceva aici ca ar fi trebuit sa arunce o eroare

        print(self.test_object.divide_numbers(first_number=self.wrong_char_number_1,
                                        second_number=self.wrong_char_number_2))

        with self.assertRaises(ValueError):
            self.test_object.divide_numbers(first_number=self.wrong_char_number_1,
                                            second_number=self.wrong_char_number_2)

        with self.assertRaises(ValueError):
            self.test_object.divide_numbers(first_number=self.wrong_char_number_1,
                                            second_number=self.positive_number_1)

        with self.assertRaises(ValueError):
            self.test_object.divide_numbers(first_number=self.wrong_char_number_2,
                                            second_number=self.positive_number_1)

        with self.assertRaises(ValueError):
            self.test_object.divide_numbers(first_number=self.wrong_char_number_1,
                                            second_number=self.positive_number_2)

        with self.assertRaises(ValueError):
            self.test_object.divide_numbers(first_number=self.wrong_char_number_2,
                                            second_number=self.positive_number_2)

    @timeout(30)
    def test_big_positive_numbers(self):

        self.assertEqual(self.test_object.divide_numbers(first_number=self.big_positive_number_2,
                                                         second_number=self.big_positive_number_1),
                         self.result_divide_1)

        self.assertTrue(self.test_object.divide_numbers(first_number=self.big_positive_number_1,
                                                        second_number=self.big_positive_number_2),
                        self.result_divide_2)

        self.assertEqual(self.test_object.divide_numbers(first_number=self.big_positive_number_4,
                                                         second_number=self.big_positive_number_3),
                         self.result_divide_3)

        self.assertTrue(self.test_object.divide_numbers(first_number=self.big_positive_number_3,
                                                        second_number=self.big_positive_number_4),
                        self.result_divide_4)

    @timeout(30)
    def test_very_big_positive_numbers(self):

        self.assertEqual(self.test_object.divide_numbers(first_number=self.very_big_positive_number_2,
                                                         second_number=self.very_big_positive_number_1),
                         self.result_divide_9)

        self.assertTrue(self.test_object.divide_numbers(first_number=self.very_big_positive_number_1,
                                                        second_number=self.very_big_positive_number_2),
                        self.result_divide_10)

        self.assertEqual(self.test_object.divide_numbers(first_number=self.very_big_positive_number_3,
                                                         second_number=self.very_big_positive_number_4),
                         self.result_divide_3)

        self.assertTrue(self.test_object.divide_numbers(first_number=self.very_big_positive_number_4,
                                                        second_number=self.very_big_positive_number_3),
                        self.result_divide_4)


if __name__ == '__main__':
    unittest.main()