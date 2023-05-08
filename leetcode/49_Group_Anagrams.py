class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            s_key = ''.join(sorted(s))
            if s_key not in res:
                res[s_key] = []
            res[s_key].append(s)

        res = [v for k,v in res.items()]
        print(res)

        return res