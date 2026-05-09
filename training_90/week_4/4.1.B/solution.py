import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    tort_num = int(input(""))

    fair_torts_counter = 0

    for t in range(tort_num):
        t_sp = list(map(int, input("").split()))
        if sum(t_sp) <= tort_num - 1:
            fair_torts_counter += 1

    print(fair_torts_counter)


if __name__ == "__main__":
    main()
