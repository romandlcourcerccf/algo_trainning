class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        profit = 0

        while right <= len(prices)-1:

            if prices[left] < prices[right]:
                profit = max(prices[right] - prices[left], profit)
            else:
                left  = right

            right +=1
        
        return profit