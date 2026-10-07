class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }

        stack = []

        for token in tokens:
            if token in ops.keys():
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(ops[token](int(op1), int(op2)))
            else:
                stack.append(token)

        return int(stack[0])
