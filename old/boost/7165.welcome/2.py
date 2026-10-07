import os
import sys
from collections import defaultdict
import math

def get_rows()->list[str]:
    
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, '7.txt')

    with open(file_name, 'r') as reader:
        rows = reader.readlines()
        rows = [tuple(map(int,r.split())) for r in rows]
        
    return rows

rows = get_rows()

rows = rows[0]

n, m  = rows[0], rows[1]

def get_side(num):
    return math.floor(math.sqrt(num))

def solution(n, m):

    if n == 0 and m == 0:
        return 0

    if n == 0 or m == 0:
        return 1

    _min = n if n <= m else m

    even =  2*_min
    odd  =  (2*_min)+1

    return max(get_side(even), get_side(odd))



    

print(solution(n, m))