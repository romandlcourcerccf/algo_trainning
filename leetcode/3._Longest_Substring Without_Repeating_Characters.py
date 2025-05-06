class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        sh = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in sh:
                sh.remove(s[l])
                l += 1

            sh.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
