from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        d1, d2 = defaultdict(int), defaultdict(int)


        for i in range(len(s)):
            d1[s[i]] +=1
            d2[t[i]] +=1
        
        return d1 == d2 
       


££££££££££££££££££££££££££££££££££££££££
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = defaultdict(int)
        h2 = defaultdict(int)

        for c in s:
            h1[c] +=1
        
        for c in t:
            h2[c] +=1

        if len(h1) != len(h2):
            return False
        
        for c in h1:
            if h1[c] != h2[c]:
                return False
        
        for c in h2:
            if h2[c] != h1[c]:
                return False

        return True

