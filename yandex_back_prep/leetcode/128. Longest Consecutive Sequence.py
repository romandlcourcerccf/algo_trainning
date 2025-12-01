class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for n in s:
            if n - 1 not in s:
                l = 1
                while n + l in s:
                    l += 1

                max_len = max(l, max_len)

        return max_len
