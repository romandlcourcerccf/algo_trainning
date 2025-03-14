import sys
import os


def main():
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '2.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    n = tuple(map(int, rows[0].split()))[0]
    nums = list(map(int, rows[1].split()))

    res = []

    nums.sort()

    left = n // 2 - 1
    right = n // 2

    while len(res) < n:
        if (n - len(res)) % 2 == 1:
            res.append(nums[right])
            right += 1
        else:
            res.append(nums[left])
            left -= 1

    print(*res)


if __name__ == "__main__":
    main()
