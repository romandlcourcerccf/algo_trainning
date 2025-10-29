import os
from collections import defaultdict


def main():
    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, "1.txt")
    # filename = os.path.join(dname, "2.txt")
    # filename = os.path.join(dname, "3.txt")
    # filename = os.path.join(dname, "4.txt")
    # filename = os.path.join(dname, "5.txt")


    with open(filename, "r") as f:
        rows = f.readlines()
        rows = [r.rstrip() for r in rows]

    nums = list(map(int, rows[0].split()))
    nums.sort()

    res = [nums[0], nums[1]] if nums[0]*nums[1] > nums[-2]*nums[-1] else [nums[-2], nums[-1]]
    print(*res)
    

if __name__ == "__main__":
    main()
