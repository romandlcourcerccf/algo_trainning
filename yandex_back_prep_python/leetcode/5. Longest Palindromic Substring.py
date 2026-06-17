class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = float("-inf")
        max_str = None

        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                i1, i2 = i, i + 1
                while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
                    if i2 - i1 + 1 >= max_len:
                        max_len = i2 - i1 + 1
                        max_str = s[i1 : i2 + 1]

                    i1 -= 1
                    i2 += 1

            i1 = i2 = i
            while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
                if i2 - i1 + 1 >= max_len:
                    max_len = i2 - i1 + 1
                    max_str = s[i1 : i2 + 1]

                i1 -= 1
                i2 += 1

        return max_str


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = float("-inf")
        max_pol = ""
        for i, c in enumerate(s):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                p1, p2 = i, i + 1
                while p1 >= 0 and p2 <= len(s) - 1 and s[p1] == s[p2]:
                    if p2 - p1 + 1 >= max_len:
                        max_len = p2 - p1 + 1
                        max_pol = s[p1 : p2 + 1]

                    p1 -= 1
                    p2 += 1

            p1, p2 = i, i
            while p1 >= 0 and p2 <= len(s) - 1 and s[p1] == s[p2]:
                if p2 - p1 + 1 >= max_len:
                    max_len = p2 - p1 + 1
                    max_pol = s[p1 : p2 + 1]

                p1 -= 1
                p2 += 1

        return max_pol
