class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pol_len = float("-inf")
        max_pol = None

        if len(s) == 1:
            return s

        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                l, r = i, i + 1
                while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                    if r - l + 1 >= max_pol_len:
                        max_pol_len = r - l + 1
                        max_pol = s[l : r + 1]
                    l -= 1
                    r += 1

            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if r - l + 1 >= max_pol_len:
                    max_pol_len = r - l + 1
                    max_pol = s[l : r + 1]
                l -= 1
                r += 1

        return max_pol
