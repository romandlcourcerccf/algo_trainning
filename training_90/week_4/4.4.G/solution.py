def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    _ = input("")
    arr = list(map(int, input("").split()))

    stack = []
    res = [-1] * len(arr)

    for i, v in enumerate(arr):
        while stack and stack[-1][0] > arr[i]:
            res[stack[-1][1]] = i
            stack.pop()

        stack.append((arr[i], i))

    print(*res)
