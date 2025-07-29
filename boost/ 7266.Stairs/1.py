import os
import sys
from collections import defaultdict
import math

def get_rows()->list[str]:
    
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, '3.txt')

    with open(file_name, 'r') as reader:
        rows = reader.readlines()
        rows = [tuple(map(int,r.split())) for r in rows]
        
    return rows

def solution(n, a):
    result = [0] * (n+1)

    if n == 1:
        return [1, a[0]]
    
    if n == 2:
        if a[0] > a[1]: 
            a[0], a[1] = -a[0], -a[1] 
        
        return [1, a[0], a[1]]
        

    for i in range(0, n-2):

        if abs(a[i])<abs(a[i+1])>abs(a[i+2]):
            return result
        
        if a[i]>a[i+1]>a[i+2]:
             a[i], a[i+1], a[i+2] = -a[i], -a[i+1], -a[i+2]
        elif a[i]<a[i+1]>a[i+2]:
            a[i+2] = -a[i+2]
        elif a[i] > a[i+1]==a[i+2]:
            a[i+1], a[i+2] =  -a[i+1], -a[i+2]
        elif a[i] == a[i+1]>a[i+2]:
            a[i], a[i+1] =  -a[i], -a[i+1]

        
    for i in range(1, n+1):
        result[i] = a[i-1]
    
    result[0] = 1

    return result


rows = get_rows()
rows = list(rows[1])

print(rows)

print(solution(len(rows), rows))


        

 


