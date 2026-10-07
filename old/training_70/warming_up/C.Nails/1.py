import sys

# https://www.youtube.com/watch?v=IRdz2GgnQwk


def main():
    import os

    dname = os.path.dirname(__file__)

    filename = os.path.join(dname, "input.txt")
    # filename = os.path.join(dname, '1.txt')

    with open(filename, "r") as f:
        nails = list(map(int, f.readlines()[1].split()))

    nails = sorted(nails)

    dp = [0] * len(nails)

    dp[1] = nails[1] - nails[0]
    dp[0] = nails[1] - nails[0]
    for i in range(2, len(dp)):
        dp[i] = min(
            dp[i - 2] + nails[i] - nails[i - 1], dp[i - 1] + nails[i] - nails[i - 1]
        )

    print(dp[-1])


if __name__ == "__main__":
    main()
