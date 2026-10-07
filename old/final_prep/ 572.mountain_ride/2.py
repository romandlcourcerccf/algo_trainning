import os
import sys
from collections import Counter

def get_rows()->list[str]:
    
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, '1.txt')

    with open(file_name, 'r') as reader:
        rows = reader.readlines()
        rows = [tuple(map(int,r.split())) for r in rows]
        
    return rows

def count_fullfillment(times_count, stay_time):
    times_scale = list(times_count.keys())
    times_scale.sort()
    print(f'times_scale :{times_scale}')
    
    
rows = get_rows()
print(rows)

number, capacity = rows[0]
print(f'number {number} capacity {capacity}')

times = [r[0] for r in rows[1:]]


times_count = Counter(times)

print(f'times_count {times_count}')

count_fullfillment(times_count, 3)


