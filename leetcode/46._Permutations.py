class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def pms(nums):

            res = []

            if len(nums) == 1:
                return [nums.copy()]
            
            for i in range(len(nums)):
                n = nums.pop(0)
                perms = pms(nums)

                for perm in perms:
                    perm.append(n)

                res.extend(perms)
                nums.append(n)

            return res 

        return pms(nums)

        return res