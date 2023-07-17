from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        h1 = defaultdict(int)
        h2 = defaultdict(int)

        for i in range(len(s)):
            h1[s[i]] +=1
            h2[t[i]] +=1
          
        for c in h1.keys():
            if c not in h2 or h2[c] != h1[c]:
                return False
      
        return True