import sys
from collections import defaultdict


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    lines = open("2.txt", "r").readlines()

    N = int(lines[0])

    print(f"N {N}")

    ratings = defaultdict()

    pos = 1
    for i in range(N):
        r_size = int(lines[pos])
        # print(f"r_size {r_size}")
        for r in range(r_size):
            pos += 1
            rating = lines[pos].strip().split()
            r_num, r_val = int(rating[0]), int(rating[1])
            ratings[r_num] = r_val

        pos += 1

    for k in sorted(list(ratings.keys())):
        print(f"{k} {ratings[k]}")


if __name__ == "__main__":
    main()
