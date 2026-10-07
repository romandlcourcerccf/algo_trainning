def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    parenthesis = input("")
    stack = []

    left = ["(", "[", "{"]
    full = ["()", "[]", "{}"]

    for _, p in enumerate(parenthesis):
        if p in left:
            stack.append(p)
        else:
            if not stack:
                print("no")
                return
            else:
                _p = stack.pop()
                if _p + p not in full:
                    print("no")
                    return

    if not stack:
        print("yes")
    else:
        print("no")
