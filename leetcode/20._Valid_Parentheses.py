class Solution:
    def isValid(self, s: str) -> bool:
        
        op = {'(', '[', '{'}
        comp = {'()', '[]', '{}'}

        h = []
        for c in s:
            if c in op:
                h.append(c)
            else:
                if len(h) == 0:
                    return False
                _c = h.pop()
               
                if _c+c not in comp:
                    return False

        if len(h) > 0:
            return False

        return True