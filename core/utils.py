import enum
from .big_number import BigNumber


class TokenType(enum.Enum):
    T_NUM = 0
    T_PLUS = 1
    T_MINUS = 2
    T_MULT = 3
    T_DIV = 4
    T_POW = 5
    T_SQRT = 6
    T_LPAR = 7
    T_RPAR = 8
    T_END = 9


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []


mappings = {'+': TokenType.T_PLUS, '-': TokenType.T_MINUS, '*': TokenType.T_MULT, '/': TokenType.T_DIV, '^': TokenType.T_POW,
            '~': TokenType.T_SQRT, '(': TokenType.T_LPAR, ')': TokenType.T_RPAR}

operations = {TokenType.T_PLUS: BigNumber.__add__, TokenType.T_MINUS: BigNumber.__sub__, TokenType.T_MULT: BigNumber.__mul__,  # here to add our operations
              TokenType.T_DIV: BigNumber.__truediv__, TokenType.T_POW: BigNumber.__xor__, TokenType.T_SQRT: BigNumber.__invert__}
