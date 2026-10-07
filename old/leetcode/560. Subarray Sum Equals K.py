class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res, cur_sum = 0, 0

        prefixes = defaultdict(int)
        prefixes[0] = 1

        for n in nums:
            cur_sum +=n
            diff = cur_sum - k
            res += prefixes[diff]
            prefixes[cur_sum] += 1
        
        return res