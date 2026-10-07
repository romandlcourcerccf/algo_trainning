class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            _dp = set()
            for t in dp:
                _dp.add(t + nums[i])
                _dp.add(t)

            dp = _dp

        return True if target in dp else False
