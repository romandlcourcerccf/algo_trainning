import sys


def main():
    import os

    dname = os.path.dirname(__file__)

    # filename = os.path.join(dname, "input.txt")
    filename = os.path.join(dname, "10.txt")

    with open(filename, "r") as f:
        lines = f.readlines()

    dp = []
    coins = []

    dim = lines[0].split()
    rows, cols = int(dim[0]), int(dim[1])
    if rows == 0 and cols == 0:
        return
    
    dp.append([0] * (cols + 1))
    for row in lines[1:]:
        dp.append([0] * (len(row.split()) + 1))
        coins.append(list(map(int, row.split())))

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            dp[row][col] = coins[row - 1][col - 1] + max(
                dp[row - 1][col], dp[row][col - 1]
            )

    row, col = rows, cols
    track = []

    while row != 0 and col != 0:
        if dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
            track.append("D")
        else:
            col -= 1
            track.append("R")

    track = track[:-1][::-1]

    print(dp[rows][cols])
    print(*track)


if __name__ == "__main__":
    main()
