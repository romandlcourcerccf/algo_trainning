import sys
import heapq


def naive(x, y, n, a, b, m):

    if n == 1:
        return y

    dp = [0] * (n + 1)

    dp[0] = x
    dp[1] = y

    for i in range(2, n + 1):
        dp[i] = a * dp[i - 1] + b * dp[i - 2]

    return dp[-1] % m


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    lines = open("4.txt", "r").readlines()

    a, b = tuple(map(int, lines[0].split()))
    M = int(lines[1])
    Q = int(lines[2])

    print(f"a {a} b {b}")
    print(f"M {M}")
    print(f"M {Q}")

    for q in range(Q):
        x, y, n = tuple(map(int, lines[q + 3].split()))
        print(naive(x, y, n, a, b, M))


if __name__ == "__main__":
    main()
