import sys


# n = int(input())
# a = [2, 4, 7]
# for i in range(3, 36):
#     a.append(a[i - 1] + a[i - 2] + a[i - 3])
# print(a[n - 1])


def main():
    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '4.txt')

    # with open(filename, 'r') as f:
    #     n = int(f.readline())

    n = int(sys.stdin.readline())

    dp = [2, 4, 7]

    for i in range(3, 36):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    print(dp[n - 1])


if __name__ == "__main__":
    main()
