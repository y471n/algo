from stack import Stack

REMAINDER_STRINGS = "0123456789ABCDEF"


def to_base(number, base):
    s = Stack()
    while number > 0:
        remainder = number % base
        stack_remainder = REMAINDER_STRINGS[remainder]
        s.push(stack_remainder)
        number = number // base
    return "".join(map(str, s[::-1]))


if __name__ == "__main__":
    number, base = int(input()), int(input())
    print(to_base(number, base))
