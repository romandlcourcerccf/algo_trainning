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


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = [w[::-1] for w in s]
        s = " ".join(s)
        return s
