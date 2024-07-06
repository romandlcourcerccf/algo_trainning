class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        rec = []

        for op in operations:

            if op == 'C':
                rec.pop()
            elif op == 'D':
                op1 = rec[-1]
                rec.append(int(op1)*2)
            elif op == '+':
                op1 = rec[-1]
                op2 = rec[-2]
                rec.append(int(op1)+int(op2))
            else:
                rec.append(int(op))
        
        return sum(rec)