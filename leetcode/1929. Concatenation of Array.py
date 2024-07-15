class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums) * 2

        for i in range(len(nums) * 2):
            if i <= len(nums)-1:
                res[i] = nums[i] 
            else:
                res[i] = nums[i-len(nums)] 
        
        return res