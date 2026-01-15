from typing import List


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t) + 1:
            for i in range(len(s)):
                if s[:i] + s[i + 1 :] == t:
                    return True
            return False
        elif len(s) + 1 == len(t):
            for i in range(len(t)):
                if t[:i] + t[i + 1 :] == s:
                    return True
            return False
        elif len(s) == len(t):
            for _s in s:
                for i in range(len(t)):
                    if t[:i] + _s + t[i + 1 :] == s:
                        return True

            for _t in t:
                for i in range(len(s)):
                    if s[:i] + _t + s[i + 1 :] == t:
                        return True

            return False
        else:
            return False
