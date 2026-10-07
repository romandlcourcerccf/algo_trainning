class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()

        return nums[0] *  nums[1] *  nums[-1] if nums[0] *  nums[1] *  nums[-1] > nums[-1] * nums[-2] * nums[-3] else nums[-1] * nums[-2] * nums[-3]