# Naive solution 

from collections import Counter
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        c = Counter(nums)
        f = math.floor(len(nums)/3)


        for k in c.keys():
            if c[k] > f:
                res += [k] 

        return res

# Naive solution 
# 
#       