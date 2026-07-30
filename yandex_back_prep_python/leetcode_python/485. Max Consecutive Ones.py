 class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_len = float('-inf')

        part_len = 0
        for i, n in enumerate(nums):
            if n == 0:
                part_len = 0
            else:
                part_len += 1

            max_len = max(max_len, part_len)

        return max_len
    
    