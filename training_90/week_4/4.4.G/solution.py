def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    _ = input("")
    arr = list(map(int, input("").split()))

    print(arr)

    stack = []
    res = [0] * len(arr)

    print("res", res)

    for i in range(len(arr) - 1, -1, -1):
        if i == len(arr) - 1:
            res[i] = -1
        else:
            _stack = []
            while stack and stack[-1][0] > arr[i]:
                _stack.append(stack.pop())
                # stack.pop()

            # pos = len(stack) - 1
            # while pos > 0 and stack[pos][0] > arr[i]:
            #     pos -= 1

            # print("pos", pos)

            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1][1]
                _stack.append(stack.pop())
                # stack.pop()

            if _stack:
                stack = stack + _stack[::-1]

        stack.append((arr[i], i))

    print(*res)
