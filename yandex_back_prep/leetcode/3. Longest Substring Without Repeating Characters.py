class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        l = 0
        h = set()

        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1

            h.add(s[r])

            max_len = max(max_len, r - l + 1)

        return max_len
