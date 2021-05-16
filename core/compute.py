from .expression_parser import Parser
from .utils import TokenType, operations, mappings

steps = []


def assert_preconditions(formula):
    assert len(formula) > 0, "empty expression"
    assert formula.count('(') == formula.count(')'), "incorrect parenthesis"


def assert_invariant(formula, parameters):
    assert type(formula) == str, "different type for expression"
    assert formula is not None, "expression is None"

    assert type(parameters) == dict, "different type for expression values"
    assert parameters is not None, "no values for expression"
    for keys, values in parameters.items():
        assert type(keys) == str and type(values) == str, 'Different type for parameters'


def assert_postconditions(result, operation, number_1, number_2):
    if operation == '/':
        assert str(eval(number_1.number + "//" + number_2.number)) == str(result), "different result"
    elif operation == "^":
        assert str(eval("pow(" + number_1.number + ',' + number_2.number + ")")) == str(result), "different result"
    elif operation == "~":
        assert str(int(eval("sqrt(" + number_1.number + ")"))) == str(result), "different result"
    else:
        assert str(eval(number_1.number + operation + number_2.number)) == str(result), "different result"


class Computation:

    def __compute(self, node):
        global steps
        step = []
        if node.token_type == TokenType.T_NUM:
            step.append(node.value)
            return node.value

        operation = operations[node.token_type]
        step.append([i for i, j in mappings.items() if j == node.token_type][0])  # get operator by token

        if node.token_type == TokenType.T_SQRT:
            left_result = self.__compute(node.children[0])
            step.append(left_result)
            steps.append(step)
            return operation(left_result)
        else:
            left_result = self.__compute(node.children[0])
            step.append(left_result)
            right_result = self.__compute(node.children[1])
            step.append(right_result)

        steps.append(step)
        try:
            result = operation(left_result, right_result)
        except ValueError as e:
            raise

        return operation(left_result, right_result)

    def get_result(self, formula, parameters):
        assert_preconditions(formula)
        global steps
        steps = []
        parsed_formula = Parser().parse_expression(formula, parameters)
        try:
            result = self.__compute(parsed_formula)
        except ValueError as e:
            raise
        assert_invariant(formula, parameters)
        sentences = {}
        for i, step in enumerate(steps):
            op = operations[mappings.get(step[0])]
            if step[0] == '~':
                op_res = op(step[1])
                sentences['Step ' + str(i)] = step[0] + '(' + str(step[1]) + ')=' + str(op_res)
            else:
                op_res = op(step[1], step[2])
                sentences['Step ' + str(i)] = str(step[1]) + step[0] + str(step[2]) + '=' + str(op_res)
            assert_postconditions(op_res, step[0], step[1], step[2])
        sentences['Result'] = result
        return result, sentences


# if __name__ == '__main__':
#     c = Computation()
#     print(c.get_result('a+(b*a)', {'a': '2', 'b': '2'}))
