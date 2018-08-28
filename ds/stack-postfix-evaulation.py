from stack import Stack
import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.itruediv
}


def do_math(token, op1, op2):
    return OPS[token](int(op1), int(op2))


def calculate_postfix(input_expression):
    token_list, operand_stack = input_expression.split(), Stack()

    for token in token_list:
        if token.isalnum():
            operand_stack.push(token)
        else:
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            result = do_math(token, operand_1, operand_2)
            operand_stack.push(result)

    return operand_stack.pop()


if __name__ == "__main__":
    print(calculate_postfix(input()))
