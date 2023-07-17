class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        res = max(nums)
        cur_max, cur_min = 1,1

        for n in nums:
            if n == 0:
               cur_max, cur_min = 1,1
               continue

            tmp_max = cur_max * n
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(tmp_max, cur_min * n, n)
            res = max(res, cur_max)
        
        return res