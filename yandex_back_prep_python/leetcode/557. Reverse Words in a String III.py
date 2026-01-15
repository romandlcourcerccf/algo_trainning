class Solution:
    def reverseWords(self, s: str) -> str:
        l = r = 0
        res = []

        while r < len(s):
            while r < len(s) and s[r] != " ":
                r += 1

            res.append(s[l:r][::-1])

            l = r
            while r < len(s) and s[r] == " ":
                r += 1
                l += 1
