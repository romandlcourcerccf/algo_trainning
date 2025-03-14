import sys
import os


def main():
    # rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '7.txt')

    # with open(filename, 'r') as f:
    #     rows = f.readlines()

    n = int(rows[0])
    nums = list(map(int, rows[1].split()))

    sum = 0
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                # print(f'i {i} j {j} k {k}')
                sum += nums[i] * nums[j] * nums[k]

    print(sum if sum < 1000000007 else sum % 1000000007)


if __name__ == "__main__":
    main()
