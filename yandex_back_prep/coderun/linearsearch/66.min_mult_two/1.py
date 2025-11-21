import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    arr = list(map(int, input().split()))
    arr.sort()

    if arr[-1] * arr[-2] > arr[0] * arr[1]:
        res = [arr[-2], arr[-1]]
    else:
        res = [arr[0], arr[1]]

    print(*res)


if __name__ == "__main__":
    main()
