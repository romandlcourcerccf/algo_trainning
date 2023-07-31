from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        h = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):

            h[s[r]] +=1

            while (r-l+1)-max(h.values()) > k:
                h[s[l]]-=1
                l+=1  
            
            res = max(res, r-l+1)

        return res