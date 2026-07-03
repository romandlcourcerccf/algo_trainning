import sys
from collections import defaultdict


def merge(l1, l2):
    p1, p2 = 0, 0

    print("l1")
    print(l1)

    print("l2")
    print(l2)

    res = []

    if len(l1) == len(l2) == 0:
        res = l1.copy()
    elif len(l1) > 0 and len(l2) == 0:
        res = l1.copy()
    elif len(l2) > 0 and len(l1) == 0:
        res = l2.copy()

    while p1 < len(l1) - 1 and p2 < len(l2) - 1:
        if l1[p1][0] <= l2[p2][0]:
            res.append(l1[p1].copy())
            p1 += 1
        else:
            res.append(l2[p2].copy())
            p2 += 1

    while p1 < len(l1) - 1:
        res.append(l1[p1])
        p1 += 1

    while p2 < len(l2) - 1:
        res.append(l2[p2])
        p2 += 1

    print("res")
    return res


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    lines = open("1.txt", "r").readlines()

    N = int(lines[0])

    print(f"N {N}")

    ratings = []

    pos = 1
    for i in range(N):
        r_size = int(lines[pos])
        for r in range(r_size):
            pos += 1
            _ratings = []
            rating = lines[pos].strip().split()
            r_pos, r_val = int(rating[0]), int(rating[1])
            _ratings.append((r_pos, r_val))

        print(_ratings)

        ratings = merge(ratings, _ratings)

        pos += 1

    print(ratings)

    for r in ratings:
        print(f"{r[0]} {r[1]}")


if __name__ == "__main__":
    main()
