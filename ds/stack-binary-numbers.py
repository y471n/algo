from stack import Stack


def to_binary(number):
    s = Stack()
    while number > 0:
        remainder = number % 2
        s.push(remainder)
        number = number // 2
    return "".join(map(str, s[::-1]))


if __name__ == "__main__":
    number = int(input())
    print(to_binary(number))
