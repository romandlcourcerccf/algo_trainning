class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float("-inf")
        n = len(nums)

        for i in range(0, n - k + 1):
            if i == 0:
                _sum = sum(nums[0:k])
            else:
                _sum -= nums[i - 1]
                _sum += nums[i + k - 1]

            max_sum = max(max_sum, _sum / k)

        return max_sum
