from stack import Stack

OPENING_SYMBOLS = "([{"
CLOSING_SYMBOLS = ")]}"


def matching_closing_symbol(opening_symbol, closing_symbol):
    return OPENING_SYMBOLS.index(opening_symbol) == CLOSING_SYMBOLS.index(closing_symbol)


def paranthesis_check(symbols):
    balanced, s = True, Stack()

    for symbol in symbols:
        if symbol in OPENING_SYMBOLS:
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
                break
            if matching_closing_symbol(s.peek(), symbol):
                s.pop()
                continue
            balanced = False
            break

    if not s.is_empty():
        balanced = False

    return balanced


if __name__ == "__main__":
    symbols = input()
    is_balanced = paranthesis_check(symbols)
    print(is_balanced)
