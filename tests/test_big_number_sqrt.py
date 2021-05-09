import unittest
import sys, os
if os.name == 'posix':
    sep = '/'
else:
    sep = '\\'
sys.path.append(os.getcwd().rsplit(sep,1)[0])
from core import operations
from core.big_number import BigNumber
from tests.util_decorators import timeout


class FunctionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.big_positive_number_1 = BigNumber("19884313212139312328923")
        self.big_positive_number_2 = BigNumber("2920193810920129831098230192830")

        self.result_sqrt_1 = "141011748489"
        self.result_object_1 = BigNumber("141011748489")

        self.result_sqrt_2 = "445918302070450053701435392"
        self.result_object_2 = BigNumber("445918302070450053701435392")

        self.big_positive_number_3 = BigNumber("10000000000000000000000000")
        self.big_positive_number_4 = BigNumber("90000000000000000000000000000000000000000000000000")
        self.result_sqrt_3 = "3162277660168"
        self.result_object_3 = BigNumber("3162277660168")

        self.result_sqrt_4 = "9486832980505138189828096"
        self.result_object_4 = BigNumber("9486832980505138189828096")

        self.small_positive_number_1 = BigNumber("73912873")
        self.small_positive_number_2 = BigNumber("831212")
        self.result_sqrt_5 = "8597"
        self.result_object_5 = BigNumber("8597")

        self.result_sqrt_6 = "911"
        self.result_object_6 = BigNumber("911")

        self.small_positive_number_3 = BigNumber("80201")
        self.small_positive_number_4 = BigNumber("932")
        self.result_sqrt_7 = "283"
        self.result_object_7 = BigNumber("283")

        self.result_sqrt_8 = "30"
        self.result_object_8 = BigNumber("30")

        self.very_big_positive_number_1 = BigNumber("123" * 100)
        self.very_big_positive_number_2 = BigNumber("256" * 101)
        self.result_sqrt_9 = "350889046741449513090370261896821460431366204398815744613012104413195285989994714981795379763041344264059369861848932278901636600533255224345738870784"
        self.result_object_9 = BigNumber("350889046741449513090370261896821460431366204398815744613012104413195285989994714981795379763041344264059369861848932278901636600533255224345738870784")

        self.result_sqrt_10 = "16008006005004378147459304662814995345845974925520761394248468111823221154193103041930767508186673397300985079832539886593967421696852061894109177053184"
        self.result_object_10 = BigNumber("16008006005004378147459304662814995345845974925520761394248468111823221154193103041930767508186673397300985079832539886593967421696852061894109177053184")

        self.negative_number_1 = BigNumber("-1329320320")
        self.negative_number_2 = BigNumber("-372392729")

        self.positive_number_1 = BigNumber("123903123312")
        self.positive_number_2 = BigNumber("2312931231233123")

        self.wrong_char_number_1 = BigNumber("dq3282023ds")
        self.wrong_char_number_2 = BigNumber("dsajdl3228320das")

    @timeout(3)
    def test_big_positive_numbers(self):
        self.assertEqual((~self.big_positive_number_1).number,
                         self.result_sqrt_1)

        self.assertEqual((~self.big_positive_number_1),
                         self.result_object_1)

        self.assertEqual((~self.big_positive_number_2).number,
                         self.result_sqrt_2)

        self.assertEqual((~self.big_positive_number_2),
                         self.result_object_2)

        self.assertEqual((~self.big_positive_number_3).number,
                         self.result_sqrt_3)

        self.assertEqual((~self.big_positive_number_3),
                         self.result_object_3)

        self.assertEqual((~self.big_positive_number_4).number,
                         self.result_sqrt_4)

        self.assertEqual((~self.big_positive_number_4),
                         self.result_object_4)

    @timeout(3)
    def test_small_positive_numbers(self):
        self.assertEqual((~self.small_positive_number_1).number,
                         self.result_sqrt_5)

        self.assertEqual((~self.small_positive_number_1),
                         self.result_object_5)

        self.assertEqual((~self.small_positive_number_2).number,
                         self.result_sqrt_6)

        self.assertEqual((~self.small_positive_number_2),
                         self.result_object_6)

        self.assertEqual((~self.small_positive_number_3).number,
                         self.result_sqrt_7)

        self.assertEqual((~self.small_positive_number_3),
                         self.result_object_7)

        self.assertEqual((~self.small_positive_number_4).number,
                         self.result_sqrt_8)

        self.assertEqual((~self.small_positive_number_4),
                         self.result_object_8)

    @timeout(3)
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            ~self.negative_number_1

        with self.assertRaises(ValueError):
            ~self.negative_number_2

    @timeout(3)
    def test_wrong_numbers(self):
        with self.assertRaises(ValueError):
            ~self.wrong_char_number_1

        with self.assertRaises(ValueError):
            ~self.wrong_char_number_2

    @timeout(3)
    def test_very_big_positive_numbers(self):
        self.assertEqual((~self.very_big_positive_number_1).number,
                         self.result_sqrt_9)

        self.assertEqual((~self.very_big_positive_number_1),
                         self.result_object_9)

        self.assertEqual((~self.very_big_positive_number_2).number,
                         self.result_sqrt_10)

        self.assertEqual((~self.very_big_positive_number_2).number,
                         self.result_object_10)


if __name__ == '__main__':
    unittest.main()