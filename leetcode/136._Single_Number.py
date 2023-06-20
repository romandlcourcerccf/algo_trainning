class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        cur = None
        for idx, num in enumerate(nums):
            if idx == 0:
                cur = num
            else:
                cur = cur ^ num
        
        return cur