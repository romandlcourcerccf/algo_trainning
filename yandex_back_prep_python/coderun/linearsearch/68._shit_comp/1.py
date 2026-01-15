import os
from collections import defaultdict


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "7.txt")
    filename = os.path.join(dname, "8.txt")

    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    nums = list(map(int, rows[1].split()))

    # print(nums)

    # find max value
    max_val, max_pos = -1, -1

    for i, v in enumerate(nums):
        if nums[i] >= max_val:
            max_val = nums[i]
            max_pos = i

    # print(f"max_val {max_val} max_pos {max_pos}")

    max_score = float("inf")
    is_exist = False
    # get candidate
    for i in range(len(nums) - 1):
        if (i > max_pos and i > 0) and nums[i] % 10 == 5 and nums[i] > nums[i + 1]:
            is_exist = True
            count_better = 0
            for j in range(0, i):
                if nums[j] > nums[i]:
                    count_better += 1

            max_score = min(max_score, count_better + 1)

    # print(f"max_score {max_score}")
    if not is_exist:
        print(0)
    else:
        print(max_score)


if __name__ == "__main__":
    main()
