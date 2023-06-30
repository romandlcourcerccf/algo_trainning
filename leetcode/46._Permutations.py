class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [nums.copy()]

        res = []
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            res = res + [p + [n] for p in perms]
            nums.append(n)
        return res
    