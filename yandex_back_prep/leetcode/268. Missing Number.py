#O(n) spase O(1) time
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        h = {}

        for n in nums:
            if n not in h:
                h[n] = 1
            else:
                h[n] += 1
        
        for i in range(len(nums)+1):
            if i not in h:
                return i
            
        return True