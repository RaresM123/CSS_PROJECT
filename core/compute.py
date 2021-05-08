from .expression_parser import Parser
from .utils import TokenType, operations, mappings

steps = []


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
        global steps
        steps = []
        parsed_formula = Parser().parse_expression(formula, parameters)
        try:
            result = self.__compute(parsed_formula)
        except ValueError as e:
            raise
        sentences = {}
        for i, step in enumerate(steps):
            op = operations[mappings.get(step[0])]
            if step[0] == '~':
                op_res = op(step[1])
                sentences['Step ' + str(i)] = step[0] + '(' + str(step[1]) + ')=' + str(op_res)
            else:
                op_res = op(step[1], step[2])
                sentences['Step ' + str(i)] = str(step[1]) + step[0] + str(step[2]) + '=' + str(op_res)

        sentences['Result'] = result
        return result, sentences
