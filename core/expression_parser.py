import re
from .big_number import BigNumber
from .utils import TokenType, Node, mappings

class Parser:
    def __lexical_analysis(self, s, values):
        tokens = []
        i = 0
        while i < len(s):
            c = s[i]
            if c in mappings:
                token_type = mappings[c]
                token = Node(token_type, value=c)
            elif re.match(r'[a-z]', c):
                val = values.get(c)
                token = Node(TokenType.T_NUM, value=BigNumber(val))  # convert str to list of integers list(map(int, list(val)))
            elif re.match(r'[\d]+',c):
                current_string = ""
                while i < len(s) and re.match(r'[\d]+',s[i]):
                    current_string += s[i]
                    i += 1
                i -= 1
                token = Node(TokenType.T_NUM, value=BigNumber(current_string))  # convert str to list of integers list(map(int, list(val)))
            else:
                raise Exception('Invalid syntax: {}'.format(c))
            tokens.append(token)

            i += 1
        tokens.append(Node(TokenType.T_END))
        return tokens


    def __parse_exp(self, tokens):
        left_node = self.__parse_exp2(tokens)

        while tokens[0].token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
            node = tokens.pop(0)
            node.children.append(left_node)
            node.children.append(self.__parse_exp2(tokens))
            left_node = node

        return left_node


    def __parse_exp2(self,tokens):
        left_node = self.__parse_exp3(tokens)

        while tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV, TokenType.T_POW]:
            node = tokens.pop(0)
            node.children.append(left_node)
            node.children.append(self.__parse_exp3(tokens))
            left_node = node

        return left_node


    def __parse_exp3(self, tokens):
        if tokens[0].token_type == TokenType.T_NUM:
            return tokens.pop(0)

        if tokens[0].token_type == TokenType.T_SQRT:
            node = tokens.pop(0)
            self.__match(tokens, TokenType.T_LPAR)
            node.children.append(self.__parse_exp(tokens))
            self.__match(tokens, TokenType.T_RPAR)
            return node

        self.__match(tokens, TokenType.T_LPAR)
        expression = self.__parse_exp(tokens)
        self.__match(tokens, TokenType.T_RPAR)

        return expression


    def __match(self, tokens, token):
        if tokens[0].token_type == token:
            return tokens.pop(0)
        else:
            raise Exception('Invalid syntax {}'.format(tokens[0].token_type))


    def parse_expression(self, formula, values):  # format a+(b*a), {a:'1',b:'2'}
        tokens = self.__lexical_analysis(formula, values)
        exp = self.__parse_exp(tokens)
        self.__match(tokens, TokenType.T_END)
        return exp
