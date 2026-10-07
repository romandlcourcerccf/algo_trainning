import sys
from collections import defaultdict


def merge(l1, l2):

    pos1 = pos2 = 0
    ln1, ln2 = len(l1), len(l2)

    res = []

    while pos1 < ln1 and pos2 < ln2:
        if l1[pos1][0] < l2[pos2][0]:
            res.append(l1[pos1])
            pos1 += 1
        elif l1[pos1][0] == l2[pos2][0]:
            res.append(l2[pos2])
            pos1 += 1
            pos2 += 1
        else:
            res.append(l2[pos2])
            pos2 += 1

    while pos2 < ln2:
        res.append(l2[pos2])
        pos2 += 1

    while pos1 < ln1:
        res.append(l1[pos1])
        pos1 += 1

    # print(f"pos1 {pos1} pos2 {pos2}")

    return res


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    lines = open("1.txt", "r").readlines()

    N = int(lines[0])

    ratings = []

    pos = 1
    for _ in range(N):
        r_size = int(lines[pos])
        _ratings = []
        for r in range(r_size):
            pos += 1
            rating = lines[pos].strip().split()
            r_pos, r_val = int(rating[0]), int(rating[1])
            _ratings.append((r_pos, r_val))
        ratings = merge(ratings, _ratings)
        pos += 1

    for r in ratings:
        print(f"{r[0]} {r[1]}")


if __name__ == "__main__":
    # l1 = [(1, 20), (2, 60), (3, 70)]

    # l2 = [(1, 21), (4, 61)]

    # print(merge(l1, l2))

    main()
