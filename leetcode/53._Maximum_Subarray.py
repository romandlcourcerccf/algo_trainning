# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         l, r = 0, len(nums)-1

#         while l < r:
#             if sum(nums[l+1:r]) > sum(nums[l:r]):
#                 l+=1
#             if sum(nums[l:r-1]) > sum(nums[l:r]):
#                 r-=1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = nums[0]
        mx = nums[0]

        for i in  range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            mx = max(cur, mx)

        return mx