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
        
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(cur_sum, max_sum)

        return max_sum
