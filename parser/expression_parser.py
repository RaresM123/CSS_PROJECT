import re

from utils import TokenType, Node, mappings


def lexical_analysis(s, values):
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in mappings:
            token_type = mappings[s[i]]
            token = Node(token_type, value=s[i])
            i += 1
        elif re.match(r'[a-z]', s[i]):
            if s[i] == 's' and s[i + 1] == 'q' and s[i + 2] == 'r' and s[i + 3] == 't':
                token_type = mappings[s[i:i + 4]]
                token = Node(token_type, value=s[i:i + 4])
                i += 4
            else:
                val = values.get(s[i])
                token = Node(TokenType.T_NUM, value=int(val))  # convert str to list of integers list(map(int, list(val)))
                i += 1
        else:
            raise Exception('Invalid syntax: {}'.format(s[i]))
        tokens.append(token)
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
