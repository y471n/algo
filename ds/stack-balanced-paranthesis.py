from stack import Stack


def paranthesis_check(symbols):
    balanced, s = True, Stack()

    for symbol in symbols:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
                break
            s.pop()

    if not s.is_empty():
        return False

    return balanced


if __name__ == "__main__":
    symbols = input()
    is_balanced = paranthesis_check(symbols)
    print(is_balanced)
