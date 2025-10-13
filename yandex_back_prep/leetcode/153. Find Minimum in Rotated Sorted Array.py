from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def find_min(nums):
            print('nums :',nums)

            l, r = 0, len(nums)-1
            while l <= r:

                if nums[l] <= nums[r]:
                    return nums[l]
                
                m = (l+r) // 2

                print(f'l {l} r {r}')

                if nums[l] < nums[m] and nums[l] <= nums[r]:
                    return nums[l]
                elif  nums[l] < nums[m] and nums[l] > nums[r]:
                    l = m+1
                elif nums[m+1] <= nums[r] and nums[m+1] < nums[m]:
                    return nums[m+1]
                elif nums[m+1] <= nums[r] and nums[m+1] >= nums[m]:
                    r = m
        
        return find_min(nums)
    

s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([11,13,15,17]))
# print(s.findMin([11]))

