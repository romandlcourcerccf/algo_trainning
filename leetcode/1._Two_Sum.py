class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = {}

        for i in range(len(nums)):
            if target - nums[i] in h:
                return [i, h[target - nums[i]]]
            else:
                h[nums[i]] = i
                
from collections import defaultdict 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        stash = defaultdict(int)

        for i, n in enumerate(nums):
            if target-n in stash:
                return [i, stash[target-n]]
            else:
                stash[n] = i
