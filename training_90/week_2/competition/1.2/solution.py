import sys
from collections import Counter


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    with open("1.txt", "r") as reader:
        rows = reader.readlines()
        rows = [r.strip() for r in rows]

    leaps, tests = tuple(map(int, rows[0].split()))

    print(f" leaps : {leaps} tests {tests}")

    left_min = float("inf")
    right_max = float("-inf")

    for l in range(1, leaps + 1):
        leap = tuple(map(int, rows[l].split()))
        left_min = min(left_min, leap[0])
        right_max = max(right_max, leap[0] + leap[1])

    print("left_min :", left_min)
    print("right_max :", right_max)

    scale = [0] * right_max

    for l in range(1, leaps + 1):
        leap_interval = tuple(map(int, rows[l].split()))
        leap = leap_interval[2]
        print("leap_interval :", leap_interval, " leap :", leap)
        count = 0
        for i in range(leap_interval[0], leap_interval[0] + leap_interval[1]):
            if count % 2 == 0:
                scale[i] = scale[i] + leap
            else:
                scale[i] = scale[i] - leap
            count += 1

    for r in range(leaps + 1, leaps + tests + 1):
        print(r, " : ", scale[int(rows[r])])


if __name__ == "__main__":
    main()
