class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        k = 0
        for i, c in enumerate(t):
            if k < len(s) and s[k] == c:
                k += 1

        return k == len(s)
