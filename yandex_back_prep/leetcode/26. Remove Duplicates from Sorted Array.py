class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        l, r = 0,0

        print(nums)

        while r < len(nums):
            nums[l] = nums[r]

            while r < len(nums) and nums[l] == nums[r]:
                r +=1
            l+=1
            
        print(nums)