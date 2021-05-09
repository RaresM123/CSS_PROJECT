import unittest.mock
import sys, os
if os.name == 'posix':
    sep = '/'
else:
    sep = '\\'
sys.path.append(os.getcwd().rsplit(sep,1)[0])
from core.big_number import BigNumber


class BigNumberTest(unittest.TestCase):

    def test_big_number_repr(self):
        nr = BigNumber('3')
        self.assertEqual(nr.__repr__(), '3')

    def test_add(self):
        with unittest.mock.patch('core.operations.Operations.add_numbers') as op:
            nr1 = BigNumber('3')
            nr2 = BigNumber('2')
            nr1.__add__(nr2)
            op.assert_called_once_with('3', '2')

    def test_sub(self):
        with unittest.mock.patch('core.operations.Operations.difference_numbers') as op:
            nr1 = BigNumber('3')
            nr2 = BigNumber('4')
            nr1.__sub__(nr2)
            op.assert_called_once_with('3', '4')

    def test_mul(self):
        with unittest.mock.patch('core.operations.Operations.multiply_numbers') as op:
            nr1 = BigNumber('2')
            nr2 = BigNumber('4')
            nr1.__mul__(nr2)
            op.assert_called_once_with('2', '4')

    def test_div(self):
        with unittest.mock.patch('core.operations.Operations.divide_numbers') as op:
            nr1 = BigNumber('6')
            nr2 = BigNumber('2')
            nr1.__truediv__(nr2)
            op.assert_called_once_with('6', '2')


    def test_xor(self):
        with unittest.mock.patch('core.operations.Operations.power_numbers') as op:
            nr1 = BigNumber('5')
            nr2 = BigNumber('2')
            nr1.__xor__(nr2)
            op.assert_called_once_with('5', '2')

    def test_invert(self):
        with unittest.mock.patch('core.operations.Operations.sqrt_numbers') as op:
            nr1 = BigNumber('16')
            nr1.__invert__()
            op.assert_called_once_with('16')
