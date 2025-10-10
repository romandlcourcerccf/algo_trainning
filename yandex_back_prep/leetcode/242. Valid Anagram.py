class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        cs = Counter(s)
        ct = Counter(t)

        for c in s:
            if c not in ct or ct[c] != cs[c]:
                return False
        
        for c in t:
            if c not in cs or cs[c] != ct[c]:
                return False

        return True