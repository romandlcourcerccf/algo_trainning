def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    expression = input("")

    # print(expression)

    stack = []

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    for e in expression.split():
        # print(">> :", e)
        if e not in operations.keys():
            stack.append(int(e))
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            stack.append(operations[e](op2, op1))

    print(stack[0])
