class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_len = 0

        for n in nums:
            if n-1 not in num_set:
                cons_len = 0
                while n + cons_len in num_set:
                    num_set.remove(n + cons_len)
                    cons_len +=1
                    
                max_len = max(cons_len, max_len)

        return max_len

