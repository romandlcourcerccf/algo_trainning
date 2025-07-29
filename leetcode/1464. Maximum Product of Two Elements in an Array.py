class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums.sort()

        print(nums)

        return (nums[-2]-1) * (nums[-1]-1)  if  nums[-2] * nums[-1] >  nums[0] * nums[1] else (nums[0]-1) * (nums[1]-1) 