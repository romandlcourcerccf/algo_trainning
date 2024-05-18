class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i, n in enumerate(nums):
            print(nums)
            if nums[i] == nums[n] and i != n:
                return n
            else:
                nums[i], nums[n] = nums[n], nums[i]
            
        return 1