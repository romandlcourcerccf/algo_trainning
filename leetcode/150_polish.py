from typing import Any, Dict, List, Optional

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
       
        ops = {
            '+' : lambda x,y : x+y,
            '-' : lambda x,y : x-y,
            '*' : lambda x,y : x*y,
            '/' : lambda x,y : float(x) / float(y)
                }

        for e in tokens:
            if e in ops.keys():
                op1 = stack.pop()
                op2 = stack.pop()
                res = int(ops[e](int(op2), int(op1)))
                stack.append(res)
            else:
                stack.append(int(e))

        return int(stack[-1])
    


s = Solution()
l = ["4","13","5","/","+"] 
# (4 + (13 / 5)) = 6
print(s.evalRPN(l))

print(int(13/5))

