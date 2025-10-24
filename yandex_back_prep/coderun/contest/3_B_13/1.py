import os 
dir_name = os.path.dirname(__file__)
file = os.path.join(dir_name, 'input.txt')
# file = os.path.join(dir_name, '1.txt')
# file = os.path.join(dir_name, '2.txt')
# file = os.path.join(dir_name, '3.txt')
# file = os.path.join(dir_name, '4.txt')

with open(file, 'r') as reader:
    rows = reader.readlines()
    rows = [r.rstrip() for r in rows]

def calc_expr(expr):
    expr = expr.split()
    s = []
    for op in expr:
        
        if op not in ['+','-', '*']:
            s.append(op)
        else:
            op2 = int(s.pop())
            op1 = int(s.pop())

            match op:
                case '+':
                    s.append(op1 + op2)
                case '-':
                    s.append(op1 - op2)
                case '*':    
                    s.append(op1 * op2)


    return s[0]

print(calc_expr(rows[0]))
            