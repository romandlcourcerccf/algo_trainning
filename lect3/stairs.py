def stairs_min_cost(costs):
    dp = [0] * (len(costs) + 1)
    prev = [0] * (len(costs) + 1)

    dp[0] = 0
    for i in range(len(dp)):
        if i == 0:
            dp[i] = 0
            prev[i] = 0
        elif i == 1:
            dp[i] = costs[i - 1]
            prev[i] = i
        else:
            dp[i] = costs[i - 1] + max(dp[i - 1], dp[i - 2])
            prev[i] = i - 1 if dp[i - 1] > dp[i - 2] else i - 2

    path = []
    pos = len(prev) - 1
    c = 0
    while pos > 1:
        path.append(pos)
        pos = prev[pos]

    path.append(pos)

    print("dp   :", dp)
    print("prev :", prev)
    print("path :", path)


costs = [10, -5, -20, -10, 20, 30, -10, 10]

stairs_min_cost(costs)
