# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0

#         for a in range(1, amount+1):
#             for c in coins:
#                 if a - c >= 0:
#                     dp[a] = min(dp[a], dp[a-c]+1)
        
#         return dp[amount] if dp[amount] < float('inf') else -1
    
    

# top down
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(amount)
        def helper(amount):

            if not amount:
                return []

            if amount < 0:
                return None
            
            optimal_result = None
            for coin in coins:
                part_result = helper(amount-coin)
                if part_result is None:
                    continue
                
                condidate = part_result + [coin]
                if optimal_result is None or len(condidate) < len(optimal_result):
                    optimal_result = condidate

            return optimal_result

        print('coins :',coins)
        print('amount :',amount)
        print('result :',helper(amount))

        result = helper(amount)
        if result == None: return -1
        if len(result) == 0: return 0
        
        return len(result) 
    
