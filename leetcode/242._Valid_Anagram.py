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
       
