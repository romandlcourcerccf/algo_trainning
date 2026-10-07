 class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        cur = 0
        for idx, num in enumerate(nums):
            cur = cur ^ num
        
        return cur