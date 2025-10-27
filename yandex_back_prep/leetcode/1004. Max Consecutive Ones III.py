from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_len = float('-inf')

        l, r = 0, 1
        
        while r < len(nums):
            if nums[l:r].count(0) > k:
                l+=1
            else: 
                max_len = max(max_len, r-l+1)
                r +=1
            
        print(f'l : {l} r: {r}')
        return max_len
    

s = Solution()
# print(s.longestOnes([0,1,1], 2))
# print(s.longestOnes([0,0,1], 2))
# print(s.longestOnes([0,0,1], 1))
# print(s.longestOnes([1,1,1], 1))
assert s.longestOnes([1], 1) == 1
assert s.longestOnes([1], 0) == 1
# print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
# print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6 

# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
