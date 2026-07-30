from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] <= nums[r]:
                return nums[l]

            if nums[l] <= nums[m] and nums[m + 1] <= nums[r]:
                return min(nums[l], nums[m + 1])
            elif nums[l] <= nums[m] and nums[m + 1] >= nums[r]:
                if nums[l] < nums[r]:
                    return nums[l]
                else:
                    l = m + 1
            elif nums[l] >= nums[m] and nums[m + 1] <= nums[r]:
                if nums[m + 1] < nums[m]:
                    return nums[m + 1]
                else:
                    r = m


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
# print(s.findMin([11]))
