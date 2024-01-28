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



