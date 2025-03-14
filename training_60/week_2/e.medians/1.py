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

    if len(nums) % 2 != 0:
        l, r = int(len(nums) / 2), int(len(nums) / 2)
    else:
        l, r = int(len(nums) / 2), int(len(nums) / 2) - 1

    while len(nums[:l]) + len(nums[r:]) > 0:
        print("nums :", nums[:l] + nums[r:])
        print("res :", res)

        ln = len(nums[:l]) + len(nums[r:])
        if ln % 2 != 0:
            res.append(nums[l])
            l -= 1
        else:
            if nums[l] == nums[r]:
                res.append(nums[l])
                l -= 1
            elif nums[l] < nums[r]:
                res.append(nums[l])
                l -= 1
            else:
                res.append(nums[r])
                r += 1

    print(res)


if __name__ == "__main__":
    main()
