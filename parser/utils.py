import enum
import operator
import math


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
            'sqrt': TokenType.T_SQRT, '(': TokenType.T_LPAR, ')': TokenType.T_RPAR}

operations = {TokenType.T_PLUS: operator.add, TokenType.T_MINUS: operator.sub, TokenType.T_MULT: operator.mul,  # here to add our operations
              TokenType.T_DIV: operator.truediv, TokenType.T_POW: operator.pow, TokenType.T_SQRT: math.sqrt}
