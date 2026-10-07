class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        if len(p) == len(s):
            return [0] if Counter(p) == Counter(s) else []

        res = []
        cp = Counter(p)

        _cp = Counter(s[0 : len(p)])
        for i in range(0, len(s) - len(p) + 1):
            if i > 0:
                prev = _cp[s[i - 1]]
                if _cp[s[i - 1]] > 1:
                    _cp[s[i - 1]] -= 1
                else:
                    del _cp[s[i - 1]]

                _cp[s[i + len(p) - 1]] += 1

            if cp == _cp:
                res.append(i)

        return res
