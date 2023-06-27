from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_l = 0
        frek_map = defaultdict(int)

        l = 0
        for r in range(len(s)):
            frek_map[s[r]] +=1

            while r-l+1 - max(frek_map.values()) > k:
                frek_map[s[l]] -= 1
                l +=1

            max_l = max(r-l+1, max_l)

        return max_l