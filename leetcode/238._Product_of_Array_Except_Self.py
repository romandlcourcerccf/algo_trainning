
# O(n) O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l, r = [0] * len(nums), [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                l[i] = nums[i]
            else:
                l[i] = l[i-1] * nums[i]

        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                r[i] = nums[i]
            else:
                r[i] = r[i+1] * nums[i]

        print('l: ', l)
        print('r: ', r)

        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = r[i+1]
            elif i == len(nums)-1:
                res[i] = l[i-1]
            else:
                res[i] = l[i-1] * r[i+1]

        return res
 

#  O(n) O(1)



