def longest_accs_series(arr):
    dp = [0] * len(arr)
    prev = [0] * len(arr)

    dp[0] = 1
    prev[0] = -1
    for i in range(1, len(arr)):
        max_diff = float("inf")
        max_diff_idx = -1

        for j in range(i):
            diff = arr[i] - arr[j]
            if diff > 0 and diff < max_diff:
                max_diff = diff
                max_diff_idx = j

        if max_diff > 0:
            dp[i] = dp[max_diff_idx] + 1
            prev[i] = max_diff_idx

    print("dp   :", dp)
    print("prev :", prev)

    max_ss = float("-inf")
    max_ss_idx = -1

    for i in reversed(range(len(dp))):
        if dp[i] > max_ss:
            max_ss = dp[i]
            max_ss_idx = i

    print("max_ss_idx ;", max_ss_idx)

    ss = []
    ss.append(max_ss_idx)
    pos = max_ss_idx
    while pos > 0:
        ss.append(prev[pos])
        pos = prev[pos]

    print(ss)


arr = [4, 10, 5, 12, 3, 24, 7, 8]
print(arr)

longest_accs_series(arr)
