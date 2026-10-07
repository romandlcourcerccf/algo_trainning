class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cash = [1] * len(nums)

        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    cash[i] = max(cash[i], cash[j] + 1)

        return max(cash)
