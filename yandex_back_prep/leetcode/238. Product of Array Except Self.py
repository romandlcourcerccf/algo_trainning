class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lr = [1] * len(nums)
        ll = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                lr[i] = nums[i]
            else:
                lr[i] = nums[i] * lr[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                ll[i] = nums[i]
            else:
                ll[i] = nums[i]*ll[i+1]

        for i in range(len(nums)):
            if i == 0:
                res[i] = ll[i+1]
            elif i == len(nums)-1:
                res[i] = lr[i-1]
            else:
                res[i] = lr[i-1] * ll[i+1]
        
        return res