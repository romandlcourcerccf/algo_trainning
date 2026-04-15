import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    N = int(input(""))
    arr = list(map(int, input("").split()))
    q_num = int(input(""))
    init_x = int(input(""))

    pref_sum = [0] * (len(arr) + 1)

    for i in range(1, len(pref_sum)):
        pref_sum[i] = pref_sum[i - 1] + arr[i - 1]

    # print(pref_sum)

    queries = [0] * (q_num * 2)
    for i in range(len(queries)):
        if i == 0:
            queries[i] = init_x
        else:
            queries[i] = (11173 * queries[i - 1] + 1) % 1000000007

    # print(queries)

    res = 0

    for i in range(0, len(queries), 2):
        # print(queries[i], queries[i + 1])

        l = min(queries[i] % N, queries[i + 1] % N)
        r = max(queries[i] % N, queries[i + 1] % N)

        # print(f" l {l} r {r}. {pref_sum[r] - pref_sum[l]}")

        res += pref_sum[r + 1] - pref_sum[l]

    print(res)


if __name__ == "__main__":
    main()
