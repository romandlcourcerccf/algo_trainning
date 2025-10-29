class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = defaultdict(list)

        for s in strs:
            h[''.join(sorted(list(s)))].append(s)

        return list(h.values())
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}

        for s in strs:
            _s = '.'.join(sorted(s))
            if _s not in h:
                h[_s]=[s]
            else:
                h[_s].append(s)
        
        return list(h.values())
