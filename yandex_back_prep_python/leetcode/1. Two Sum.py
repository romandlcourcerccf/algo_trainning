class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = {}

        
        for i, v in enumerate(nums):
            if target-v in h:
                return [i, h[target-v]]
            h[v] = i