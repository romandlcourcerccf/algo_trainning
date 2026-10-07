class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }

        s = []
        for t in tokens:
            if t not in ops.keys():
                s.append(t)
            else:
                op1 = s.pop()
                op2 = s.pop()
                s.append(ops[t](int(op2), int(op1)))

        return int(s[0])
