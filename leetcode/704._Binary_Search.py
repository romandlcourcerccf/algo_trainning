class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while left <= right:
        
            pos = (left + right)//2
            if nums[pos] == target:
                 return pos
            elif nums[pos] < target:
                left = pos+1
            else: 
                right = pos-1

        return -1