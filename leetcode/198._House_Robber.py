class Solution:
    def rob(self, nums: List[int]) -> int:

        stash = [-1] * len(nums)

        def rob(nums, index): 

            if index > len(nums)-3:
                return max(nums[index:])
            else:
                if stash[index+2] == -1:
                    stash[index+2] = rob(nums, index+2)
                if stash[index+1] == -1: 
                    stash[index+1] = rob(nums, index+1)