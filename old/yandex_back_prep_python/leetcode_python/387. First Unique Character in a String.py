class Solution:
    def firstUniqChar(self, s: str) -> int:

        h = {}

        for c in s:
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1

        for i, c in enumerate(s):
            if h[c] == 1:
                return i

        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:

        h = Counter(s)

        for i, c in enumerate(s):
            if h[c] == 1:
                return i

        return -1
