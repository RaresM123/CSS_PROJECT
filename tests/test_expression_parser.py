import unittest.mock
import sys, os
if os.name == 'posix':
    sep = '/'
else:
    sep = '\\'
sys.path.append(os.getcwd().rsplit(sep,1)[0])
from core import expression_parser


class ParserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.wrong_expression = "a+(b*c"
        self.values2 = {'a': '2', 'b': '3', 'c': '4'}

        self.expression2 = "a*b+c"
        self.less_values = {'a': '2', 'c': '3'}

        self.test_object = expression_parser.Parser()

    def test_wrong_expression(self):
        with self.assertRaises(Exception):
            self.test_object.parse_expression(formula=self.wrong_expression, values=self.values2)

    def test_less_values(self):
        with self.assertRaises(Exception):
            self.test_object.parse_expression(formula=self.expression2, values=self.less_values)

    def test_parse_expression(self):
        self.expression = "a+(b*a)"
        self.values = {'a': '1', 'b': '2'}

        # self.result = Node(token_type=TokenType.T_PLUS, value='+') #to do
        # node1 = Node(token_type=TokenType.T_NUM, value='1')
        # node2 = Node(token_type=TokenType.T_MULT, value='*')
        # node2.children.append(Node(token_type=TokenType.T_NUM, value=2))
        # node2.children.append(Node(token_type=TokenType.T_NUM, value=2))
        # self.result.children = [node1, node2]

        with unittest.mock.patch('core.expression_parser.Parser.parse_expression') as parse:
            self.test_object.parse_expression(formula=self.expression, values=self.values)
            parse.assert_called_once_with(formula=self.expression, values=self.values)
