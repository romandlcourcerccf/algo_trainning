class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = defaultdict(list)

        for s in strs:
            h[''.join(sorted(list(s)))].append(s)

        return list(h.values())
    