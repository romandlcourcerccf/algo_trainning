import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    lines = open("1.txt", "r").readlines()

    n, m = lines[0].split()[0], lines[0].split()[1]

    print(f"n {n} m {m}")


if __name__ == "__main__":
    main()
