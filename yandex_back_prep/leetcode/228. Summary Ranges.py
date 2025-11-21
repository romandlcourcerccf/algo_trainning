class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        nums.append(100)

        partial_sum = []
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                partial_sum.append(nums[i])
                if len(partial_sum) > 1:
                    res.append(f"{partial_sum[0]}->{partial_sum[-1]}")
                else:
                    res.append(f"{partial_sum[0]}")

                partial_sum = []
            else:
                partial_sum.append(nums[i])

        return res
