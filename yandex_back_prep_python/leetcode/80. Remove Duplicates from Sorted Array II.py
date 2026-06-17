class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 0

        while r < len(nums):
            d = 0
            while r < len(nums) - 1 and nums[r] == nums[r + 1]:
                r += 1
                d += 1

            if d < 1:
                nums[l] = nums[r]

                l += 1
                r += 1
            else:
                nums[l] = nums[r]
                nums[l + 1] = nums[r]
                l += 2
                r += 1

        return l
