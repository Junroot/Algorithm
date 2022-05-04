from itertools import permutations


def calculate_operation(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    return operand1 * operand2


def calculate(expression, op_priority):
    op_priority_dict = {op: i for i, op in enumerate(op_priority)}
    operand = ""
    operand_stack = []
    operator_stack = []
    for character in expression:
        if character not in op_priority_dict:
            operand += character
        else:
            operand_stack.append(int(operand))
            operand = ""
            priority = op_priority_dict[character]
            while len(operator_stack) > 0 and operator_stack[-1] <= priority:
                operand1 = operand_stack.pop()
                operand2 = operand_stack.pop()
                operator = op_priority[operator_stack.pop()]
                operand_stack.append(calculate_operation(operator, operand2, operand1))
            operator_stack.append(priority)

    operand_stack.append(int(operand))

    while len(operator_stack) > 0:
        operand1 = operand_stack.pop()
        operand2 = operand_stack.pop()
        operator = op_priority[operator_stack.pop()]
        operand_stack.append(calculate_operation(operator, operand2, operand1))
    return abs(operand_stack[-1])


def solution(expression):
    operators = {'+', '-', '*'}
    used_operators = set()
    result = -1
    for character in expression:
        if character in operators:
            used_operators.add(character)

    for op_priority in permutations(used_operators):
        result = max(result, calculate(expression, op_priority))
    return result


solution("100-200*300-500-20")
