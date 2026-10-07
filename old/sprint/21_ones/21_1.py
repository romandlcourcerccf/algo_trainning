def ones(N):
    if N == 1:
        return 2
    if N == 2:
        return 4
    if N == 3:
        return 7

    dp = [0] * N

    for i in range(N):
        if i == 0:
            dp[i] = 2
        elif i == 1:
            dp[i] = 4
        elif i == 2:
            dp[i] = 7
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[-1]


N = int(open("input.txt", "r").readline())

ans = ones(N)

open("output.txt", "w").write(str(ans))
