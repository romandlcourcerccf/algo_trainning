from typing import List

a = [3,7,8,9,8]
b = [2,4,8]

def merge(a: List[int], b: List[int]) -> List[int]:
    res = []
    p1, p2 = 0, 0

    while p1 <= len(a)-1 and p2 <= len(b)-1:
        if a[p1] <= b[p2]:
            res.append(a[p1])
            p1+=1
        else:
            res.append(b[p2])
            p2+=1

    
    if p1 < len(a)-1:
        res = res + a[p1:]
    else:
        res = res + b[p2:]
    
    print(*res)
        

merge(a,b)