class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        min_diff = float("inf")

        p1, p2 = 0, k - 1

        while p2 <= len(nums) - 1:
            min_diff = min(min_diff, nums[p2] - nums[p1])
            p1 += 1
            p2 += 1

        return min_diff
