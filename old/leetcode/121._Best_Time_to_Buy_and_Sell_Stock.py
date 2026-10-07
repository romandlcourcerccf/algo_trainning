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
    
     >>>>>>>>>>>>>>>>>
    
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0

        l, r = 0,1
        profit = float('-inf')

        while r <= len(prices)-1:
            _profit = prices[r] - prices[l]

            if _profit < 0:
                l +=1
            else:
                profit = max(_profit, profit)
                r +=1
        
        return profit