from typing import List


class Solution:
    def calc_diff(self, l: int, r: int, pref_sum: List[int]) -> int:
        return (r - l + 1) - (pref_sum[r] - pref_sum[l - 1])

    def getMaxConsequteveOnesII(self, arr: List[int]) -> int:
        max_cons_len = float("-inf")

        pref_sum = [0] * (len(arr) + 1)

        for i in range(1, len(arr) + 1):
            pref_sum[i] = pref_sum[i - 1] + arr[i - 1]

        l = 0

        for r in range(1, len(pref_sum)):
            diff = self.calc_diff(l, r, pref_sum)

            if diff <= 2:
                max_cons_len = max(max_cons_len, r - l + 1)

            else:
                while diff >= 2 or l == r:
                    l += 1
                    diff = self.calc_diff(l, r, pref_sum)
                    max_cons_len = max(max_cons_len, r - l + 1)

        return max_cons_len
