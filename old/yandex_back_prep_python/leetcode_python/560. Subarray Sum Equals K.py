class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cur_sum = 0, 0

        pref_sums = {0: 1}

        for n in nums:
            print(pref_sums)

            cur_sum += n
            diff = cur_sum - k

            res += pref_sums.get(diff, 0)
            pref_sums[cur_sum] = 1 + pref_sums.get(cur_sum, 0)

        return res
