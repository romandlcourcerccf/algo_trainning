 class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                tr_sum = nums[l] + nums[r] + a 
                if tr_sum > 0:
                    r -=1
                elif tr_sum < 0:
                    l +=1
                else:
                    res.append([nums[l], nums[r], a])  # Hard part 
                    l +=1
                    while nums[l] == nums[l-1] and l < r:  # Hard part 
                        l +=1
        
        return res