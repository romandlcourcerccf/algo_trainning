from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = defaultdict(int)

        for n in nums:
            if h[n] > 0:
                return True
            h[n] += 1

        return False
