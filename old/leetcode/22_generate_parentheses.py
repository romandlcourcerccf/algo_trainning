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
    
    //Me solution

    class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(sol):
            if len(sol) == n * 2:
                if  sol.count('(') == sol.count(')'):
                    res.append(sol)
                else:
                    return 

            if len(sol) < n * 2:
                if sol.count('(') < sol.count(')') :
                    return
                else:
                    backtrack(sol + ')')
                    backtrack(sol + '(')


        backtrack('(')

        return res
    

    class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def back(seq):

            if len(seq) == 2*n:
                if seq.count('(') == seq.count(')'):
                    res.append(seq)
                return
                
            elif seq.count('(') < seq.count(')'):
                return
            else:
                back(seq + '(')
                back(seq + ')')

        back('')

        return res
