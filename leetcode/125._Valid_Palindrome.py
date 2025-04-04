import re

regex = re.compile("[^a-zA-Z0-9]")


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = regex.sub("", s)

        if len(s) < 2:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [i.lower() for i in re.findall("[A-z0-9]", s) if i.isalnum()]
        return x[::-1] == x
