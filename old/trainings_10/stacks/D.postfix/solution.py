def solution():
    exp = input()
    exp = exp.split()

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    stack = []

    for e in exp:
        if e in operations.keys():
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(operations[e](op2, op1))
        else:
            stack.append(int(e))

    print(stack[-1])


if __name__ == "__main__":
    solution()
