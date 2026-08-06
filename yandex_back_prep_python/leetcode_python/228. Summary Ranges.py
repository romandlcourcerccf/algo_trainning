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
    
    class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        i = 0
        while i < len(nums):
            _res = []
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                _res.append(nums[i])
                i+=1
            _res.append(nums[i])
    
            if len(_res) > 1:
                res.append(f'{_res[0]}->{_res[-1]}')
            else:
                res.append(f'{_res[0]}')

            i+=1

        return res


        



