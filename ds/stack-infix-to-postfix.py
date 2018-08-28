from stack import Stack

OPERATORS_PRECEDENCE_ORDER = {
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 1,
}


def infix_to_postfix(infix_expression):
    operator_stack, postfix_result = Stack(), []
    token_list = infix_expression.split()

    for token in token_list:
        if token.isalnum():
            # The token is an operand
            postfix_result.append(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            # Pop the stack until ( is found and add to result
            top_token = operator_stack.pop()
            while top_token != "(":
                postfix_result.append(top_token)
                top_token = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) and \
                    (OPERATORS_PRECEDENCE_ORDER[operator_stack.peek()] >= OPERATORS_PRECEDENCE_ORDER[token]):
                postfix_result.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.is_empty():
        postfix_result.append(operator_stack.pop())

    return " ".join(postfix_result)


if __name__ == "__main__":
    print(infix_to_postfix(input()))
