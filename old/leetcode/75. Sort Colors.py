class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        clrs = [0] * 3

        for i in range(len(nums)):
            clrs[nums[i]] += 1

        pos = 0
        for i in range(len(clrs)):
            for j in range(pos, pos + clrs[i]):
                pos += 1
                nums[j] = i

        return nums
