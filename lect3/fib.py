def fib(n, dp):

    if dp[n] == -1:
        dp[n] = fib(n-1, dp) + fib(n-2, dp)

    return dp[n] 

n = int(input())
dp = [-1] * (n+1)
dp[0] = dp[1] = 1
print(fib(n, dp))
10

