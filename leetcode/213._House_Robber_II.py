class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
            
        def _rob(nums, index, stash): 
 
            if index > len(nums)-3:
                return max(nums[index:])
            else:
                if stash[index+2] == -1:
                    stash[index+2] = _rob(nums, index+2, stash)
                if stash[index+1] == -1: 
                    stash[index+1] = _rob(nums, index+1, stash)
            
                return max(nums[index] + stash[index+2], stash[index+1])

        r1 = _rob(nums[1:] ,0, [-1] * (len(nums)-1))
        r2 = _rob(nums[:len(nums)-1], 0, [-1] * (len(nums)-1))
       
        return max(r1, r2) 