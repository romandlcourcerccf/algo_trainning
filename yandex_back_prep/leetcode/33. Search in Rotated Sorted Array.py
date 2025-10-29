class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while l <= r:
            m = (l + r) // 2

            if l == r and nums[l] != target:
                return -1

            if nums[m] == target:
                return m

            elif nums[l] <= nums[m] and nums[m + 1] <= nums[r]:
                if nums[m + 1] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            elif nums[l] <= nums[m] and nums[m + 1] >= nums[r]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1

            elif nums[l] >= nums[m] and nums[m + 1] <= nums[r]:
                if nums[m + 1] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m

        return -1
