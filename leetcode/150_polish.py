class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: float(x)/float(y),
        }

       
        s = []

        for tok in tokens:
            if tok not in ops.keys():
                s.append(int(tok))
            else:
                op1 = s.pop()
                op2 = s.pop()
                s.append(ops[tok](int(op2), int(op1)))
        
        return int(s[-1])

