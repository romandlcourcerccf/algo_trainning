import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    arr_num = input("")
    arr = list(map(int, input("").split()))
    pref_summ = [0] * (len(arr) + 1)

    for i in range(1, len(pref_summ)):
        pref_summ[i] = pref_summ[i - 1] + arr[i - 1]

    print(*pref_summ[1:])


if __name__ == "__main__":
    main()
