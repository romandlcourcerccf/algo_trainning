class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ps = [0] * (len(nums)+1)

        for i in range(1, len(ps)):
            ps[i] = nums[i-1] + ps[i-1]

        print(ps)

        l, r = 0,1
        cnt = 0
        
        while r < len(ps):
            s = ps[r] - ps[l]
            if s == k:
                r +=1
            elif s < k:
                r+=1
            else:
                l +=1

        return cnt
