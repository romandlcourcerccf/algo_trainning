class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        l_mult = [1] * len(nums)
        r_mult = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                l_mult[i] = nums[i]
            else:
                l_mult[i] = l_mult[i - 1] * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                r_mult[i] = nums[i]
            else:
                r_mult[i] = r_mult[i + 1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                res[i] = r_mult[i + 1]
            elif i == len(nums) - 1:
                res[i] = l_mult[i - 1]
            else:
                res[i] = l_mult[i - 1] * r_mult[i + 1]

        return res
