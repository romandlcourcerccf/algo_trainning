import sys
from collections import deque
from typing import List

operations  ={
    '+': lambda x,y : x+y,
    '-': lambda x,y : x-y,
    '*': lambda x,y : x*y
}

priority = {
    '+': 0,
    '-': 0,
    '*': 1
}

def is_digit(a):
    try:
        int(a)
        return True
    except:
        return False
    
def push_all_higher(op: str, stack: List[str]) -> List[str]:
    print(f'op {op} stack {stack}')
    res = []

    while stack and stack[-1] in operations.keys() and priority[stack[-1]] >= priority[op]:
        res.append(stack[-1])
        stack.pop()
    print(f'<<<<<111<<<<<')
    return res

def push_all_until_enclosing(op: str, stack: List[str]) -> List[str]:
    print(f'>>>>222>>>>>')
    res = []
    while stack and stack[-1] != '(':
        res.append(stack[-1])
        stack.pop()

    if  stack[-1] == '(':
        stack.pop()
    
    print(f'<<<<<222<<<<')

    return res

def convert_to_polish(exp):
    res = []
    stack = []
    for op in exp:
        if is_digit(op):
            res.append(op)
        elif op in operations.keys():
            res.extend(push_all_higher(op, stack))
            stack.append(op)
        elif op == '(':
            stack.append(op)
        elif op == ')':
            res.extend(push_all_until_enclosing(op, stack))
        else:
            if op != ' ':
                print('WRONG')
                return
            pass
        # print(f'op : {op} res {res} stack {stack}')
    
    res.extend(stack[::-1])

    return res

def main():
   
    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '6.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()

    expression = rows[0]
    print(f'expression : {expression}')
    polish = convert_to_polish(expression)
    print(f'polish : {polish}')

if __name__ == '__main__':
    main()

