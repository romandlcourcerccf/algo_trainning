import sys
import os


def main():
    # rows = sys.stdin.readlines()

    import os

    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, "1.txt")

    with open(filename, "r") as f:
        rows = f.readlines()

    n = tuple(map(int, rows[0].split()))[0]
    nums = list(map(int, rows[1].split()))

    res = []
    nums.sort()

    if len(nums) // 2 != 0:
        l, r = nums // 2 + 1, nums // 2 + 1


if __name__ == "__main__":
    main()
