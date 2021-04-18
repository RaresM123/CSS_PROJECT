import re
from big_number import BigNumber
from utils import TokenType, Node, mappings


def lexical_analysis(s, values):
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


def parse_exp(tokens):
    left_node = parse_exp2(tokens)

    while tokens[0].token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_exp2(tokens))
        left_node = node

    return left_node


def parse_exp2(tokens):
    left_node = parse_exp3(tokens)

    while tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV, TokenType.T_POW]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_exp3(tokens))
        left_node = node

    return left_node


def parse_exp3(tokens):
    if tokens[0].token_type == TokenType.T_NUM:
        return tokens.pop(0)

    if tokens[0].token_type == TokenType.T_SQRT:
        node = tokens.pop(0)
        match(tokens, TokenType.T_LPAR)
        node.children.append(parse_exp(tokens))
        match(tokens, TokenType.T_RPAR)
        return node

    match(tokens, TokenType.T_LPAR)
    expression = parse_exp(tokens)
    match(tokens, TokenType.T_RPAR)

    return expression


def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise Exception('Invalid syntax {}'.format(tokens[0].token_type))


def parse_expression(formula, values):  # format a+(b*a), {a:'1',b:'2'}
    tokens = lexical_analysis(formula, values)
    exp = parse_exp(tokens)
    match(tokens, TokenType.T_END)
    return exp
