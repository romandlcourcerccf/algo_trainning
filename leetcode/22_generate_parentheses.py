class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def gen(l, r, p):
            if l + r == 2 * n:
                res.append(p)
            elif l>r:
                if l == n:
                    gen(l, r+1, p+')')
                else:
                    gen(l+1, r, p+'(')
                    gen(l, r+1, p+')')
            elif l == r:
                gen(l+1, r, p+'(')

        gen(0,0,'')
        return res