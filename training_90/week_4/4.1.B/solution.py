import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    _ = int(input(""))
    vagons = list(map(int, input("").split()))

    end = []
    res = []

    for idx, val in enumerate(vagons):
        if idx < len(vagons) - 1:
            if val <= min(vagons[idx + 1 :]):
                res.append(val)
            elif not end or val <= end[-1]:
                end.append(val)
            else:
                print("NO")
                return
        else:
            res.append(val)

    res += end[::-1]
    print("YES")
