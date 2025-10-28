class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_cons_len = float("-inf")

        if len(nums) == 1 and nums[0] == 1:
            return 1

        elif len(nums) == 1 and nums[0] == 0:
            return 1 if k >= 1 else 0

        pref_sum = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            pref_sum[i] = pref_sum[i - 1] + nums[i - 1]

        print(pref_sum)

        l = 0
        for r in range(1, len(pref_sum)):
            print(f"r {r} l {l}")
            d1 = pref_sum[r] - pref_sum[l - 1]
            d2 = r - l + 1
            c_zeros = d2 - d1
            print("c_zeros :", c_zeros)
            if c_zeros <= k:
                max_cons_len = max(max_cons_len, r - l + 1)
            else:
                l += 1

        print(max_cons_len)

        return max_cons_len if max_cons_len != float("-inf") else 0
