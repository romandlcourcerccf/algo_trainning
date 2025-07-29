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

n,m = rows[0]
p = rows[1]

def solution(n: int) -> int:
    
    cash = defaultdict(int)
    pow_10_9 = pow(10,9) - 7538

    a = 1
    for i in range(2, n+1):
       
        a_i_3 = cash[i // 3]
        a_i_2 = cash[i // 2]
        a_i_4 = cash[i // 4]

        cash[i] = (pow(a_i_2, a_i_3) + 5*a_i_4 + n) % pow_10_9

    print(cash[n+1])


