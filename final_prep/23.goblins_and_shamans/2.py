import sys
import os
from collections import defaultdict, Counter


def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    # rows = sys.stdin.readlines()
    # rows = [r.rstrip() for r in rows]

    from collections import deque
    n = int(rows[0])

    q, qt = deque(),  deque()
    k1, k2 = 0, 0

    res = []
    for i in range(n):
        print('q :', q, 'qt :', qt)
        t1 = rows[i+1].split()
        if '-' in t1:
            res.append(q.popleft())
            k1 -=1
        elif '+' in t1:
            qt.append(t1[-1])
            k2 +=1
        else:
            qt.appendleft(t1[-1])
            k2+=1
        if k1 < k2:
            q.append(qt.popleft())
            k2 -=1
            k1 +=1
    
    print(*res, sep='\n')






if __name__ == '__main__':
    main()