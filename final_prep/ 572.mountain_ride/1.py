import os
import sys
from collections import Counter

def get_rows()->list[str]:
    
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, '3.txt')

    with open(file_name, 'r') as reader:
        rows = reader.readlines()
        rows = [tuple(map(int,r.split())) for r in rows]
        
    return rows

def count_fullfillment(times_count: dict[int], times_scale: list[int], stay_time: int):
    
    fullfill_for_dates = [0]*len(times_scale)
    for i in range(len(times_scale)):
        _inh_collect = 0 
        for _i in range(max(0, times_scale[i]-stay_time+1),times_scale[i]+1):
            if _i in times_count:
                _inh_collect += times_count[_i]
        fullfill_for_dates[i] = _inh_collect

    return max(fullfill_for_dates)

rows = get_rows()

number, capacity = rows[0]
print(f'number {number} capacity {capacity}')

times = [r[0] for r in rows[1:]]

times_count = Counter(times)

print(f'times_count {times_count}')

times_scale = list(times_count.keys())
times_scale.sort()

max_time = -1

l,r = 0, len(times_scale)

while l<r:
    mid = (l+r) // 2

    _max_time = count_fullfillment(times_count,times_scale,mid)
    print(f'>>max_time : {_max_time}')

    if _max_time > capacity:
        r = mid -1
    elif _max_time < capacity:
        l = mid+1
        max_time = max(max_time, _max_time)
    else:
        max_time = _max_time
        break

print(f'max_time : {max_time}')
