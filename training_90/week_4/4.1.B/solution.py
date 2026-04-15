import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    _ = int(input(""))
    vagons = list(map(int, input("").split()))

    end_stack = []
    res_way = []

    for idx, v in enumerate(vagons):
        if idx < len(vagons) - 1:
            if v <= min(vagons[idx + 1 :]):
                res_way.append(v)
            elif not end_stack or v <= end_stack[-1]:
                end_stack.append(v)
            else:
                print("NO")
                return
        else:
            if not end_stack or v <= end_stack[-1]:
                end_stack.append(v)
            else:
                print("NO")

    if end_stack:
        res_way = res_way + end_stack[::-1]

    print("YES")


if __name__ == "__main__":
    main()
