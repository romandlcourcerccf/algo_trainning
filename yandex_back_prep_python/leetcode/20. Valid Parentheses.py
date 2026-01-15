class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        p = ['()', '[]', '{}']

        for c in s:
            
            if c in ['{', '[', '(']:
                st.append(c)
            else:
                if not st:
                    return False

                _c = st.pop()
        
                if _c+c not in p:
                    return False

        return len(st) == 0



            