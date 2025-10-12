from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def b_search(nums, l,r, t):
            while l <= r:
                m = (l+r) // 2
                if nums[m] == t:
                    return m
                elif nums[m] > t:
                    r = m-1
                else:
                    l = m+1
            
            return -1

        def r_search(nums, t):
            l, r = 0, len(nums)-1
           
            while l <= r:
            
                if l == r and nums[l] != t:
                    return -1
                

                m = (l+r) // 2 
                if nums[m] == t:
                    return m
                elif nums[m+1] <= nums[r] and nums[m+1] <= t <= nums[r]:
                    return  b_search(nums, m+1, r, t)
                elif nums[m+1] <= nums[r] and not nums[m+1] <= t <= nums[r]:
                    r = m
                elif nums[l] <= nums[m] and nums[l] <= t <= nums[m]:
                    return  b_search(nums, l, m, t)
                elif nums[l] <= nums[m] and not nums[l] <= t <= nums[m]:
                    l = m

            return -1

        return r_search(nums, target)






