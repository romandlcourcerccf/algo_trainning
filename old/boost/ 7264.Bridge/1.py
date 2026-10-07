import os
import sys
from collections import defaultdict
import math

def get_rows()->list[str]:
    
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, '1.txt')

    with open(file_name, 'r') as reader:
        rows = reader.readlines()
        rows = [list(map(int,r.split())) for r in rows]
        
    return rows

rows = get_rows()

print(rows[0])
print(rows[1])


def solution(n, a):
    a.sort() 

    print(f'n :{n} a : {a}')

    d = [0] * (n-1)

    for i in range(0, n-1):
        d[i] = abs(a[i+1] - a[i])

    print(f'a : {a}')
    print(f' d : {d}')

    _arg_max, _min = 0, 0
    _max, _min = float('-inf'), float('inf')

    for i in range(len(d)):
        if d[i] >= _max:
            _max = d[i]
            _arg_max = i
        
        if d[i] <= _min and d[i] > 1: 
            _min = d[i]
            _arg_min = i
    
    print(f'max: {_max} argmax: {_arg_max}')
    print(f'min: {_min} argmin: {_arg_min}')

    print(f'a : {a}')
    a.insert(_min, _arg_min)
    print(f'a : {a}')
    print('>> ' ,_arg_max + 1)

    a[_arg_max + 2] = -1

    print(f'a : {a}')    

solution(rows[0][0] , rows[1])