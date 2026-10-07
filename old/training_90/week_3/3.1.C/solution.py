import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    _ = input("")
    arr = list(map(int, input("").split()))

    prefix_sum = [0] * (len(arr) + 1)

    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    max_val = float("-inf")

    for pos1 in range(1, len(prefix_sum)):
        for pos2 in range(0, pos1):
            val = prefix_sum[pos1] - prefix_sum[pos2]
            max_val = max(max_val, val)

    print(max_val)


if __name__ == "__main__":
    main()
