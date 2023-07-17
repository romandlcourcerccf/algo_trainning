from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def get_profit(day, have_stock):

            if day < 0:
                if not have_stock:
                    return 0
                else:
                    return float('-inf')
                
            price = prices[day]
            if have_stock:
                buy = get_profit(day-1, False) - price
                hold = get_profit(day-1, True)
                return max(buy, hold)
            else:
                sell =  get_profit(day-1, True) + price
                hold =  get_profit(day-1, False)
                return max(sell, hold)
        
        return get_profit(len(prices)-1, False)