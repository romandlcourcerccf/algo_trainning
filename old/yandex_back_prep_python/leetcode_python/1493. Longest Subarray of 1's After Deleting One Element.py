class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        max_len = float('-inf')
        l = 0
        s = 0

        for r in range(len(nums)):
            s += nums[r]
            
            while l < r and s < r-l:
                s -= nums[l]
                l +=1

            max_len  = max(max_len, r-l)

        return max_len