class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        print(nums)
        self.pref_sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.pref_sums[i] = self.pref_sums[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sums[right + 1] - self.pref_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
