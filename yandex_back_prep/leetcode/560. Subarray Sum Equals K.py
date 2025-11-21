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


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0 

        if len(nums) == 1:
            return 0 if k != nums[0] else 1

        pref_sum = [0] * (len(nums)+1)

        for i in range(1, len(pref_sum)):
            pref_sum[i] = pref_sum[i-1] + nums[i-1]

        print(pref_sum)
        
        l = 0
        for r in range(len(pref_sum)):
            print(f'r: {r} l: {l}   {pref_sum[r] - pref_sum[l]} ')
            while l <= r and pref_sum[r] - pref_sum[l] > k:
                l +=1
            
            if pref_sum[r] - pref_sum[l] == k:
                res +=1
        
        return res