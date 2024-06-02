class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0

        for n in nums:
            tmp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2



class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums)+1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(len(nums)):
            dp[i+1] = max(dp[i],  dp[i-1] + nums[i])

        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        # prev2 prev curr
        # max(prev2+curr, prev)
        @cache
        def dp(i):
            # base
            if i < 0:
                return 0
            return max(dp(i-2)+nums[i], dp(i-1))
        
        return dp(len(nums)-1)



