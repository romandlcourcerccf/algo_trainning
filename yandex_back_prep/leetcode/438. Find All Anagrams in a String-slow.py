class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) >= len(s):
            return []

        res = []

        cp = Counter(p)

        for i in range(0, len(s) - len(p) + 1):
            if cp == Counter(s[i : i + len(p)]):
                res.append(i)

        return res
