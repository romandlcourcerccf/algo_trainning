class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [0] * len(prices):

        for i in range(len(dp)):
            if i == 0:
                dp[i] = ['b', dp[i]-prices[i], 1]
            else:
                if  prices[i-1] >= prices[i]:
                    if dp[i-1][0] != '`s':
                        dp[i] = ['b', dp[i]-prices[i], 1]
                    else:
                         dp[i] = ['c', dp[i-1][1], dp[i-1][2]]
                else:


