import sys
import os


def main():
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '2.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    n, k = tuple(map(int, rows[0].split()))
    days = list(map(int, rows[1].split()))

    days.sort()
    res = 0
    left, right = 0, 0
    while left < n and right < n:
        if days[right] - days[left] <= k:
            res = max(res, right - left + 1)
            right += 1
        else:
            left += 1

    print(res)


if __name__ == "__main__":
    main()
