import os
import copy
from collections import deque

def get_rows():

    print('os.path.dirname(__file__) ',os.path.dirname(__file__))

    file_name = os.path.join(os.path.dirname(__file__), '1.txt')
    print('file_name :',file_name)
    with open(file_name, 'r') as reader:
        rows = reader.readlines()
    
    return rows

rows = get_rows()

r, c = list(map(int, rows[0].split()))
s_x, s_y = list(map(int, rows[-2].split()))
d_x, d_y = list(map(int, rows[-1].split()))

print('start :', s_x, s_y)
print('end   :', d_x, d_y)

fields = [r.strip() for r in rows[1:-2]]
fields = [list(r) for r in fields]

dist = copy.deepcopy(fields)

for r in range(len(dist)):
    dist[r] = list(dist[r])
    for c in range(len(dist[r])):
        dist[r][c] = -1

def get_neighbors(point, fields, rows, cols):
    res = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            res.append((x+ point[0], y+point[1]))
    
    res = [r  for r in res if 0<=r[0]<=rows and 0<=r[1]<=cols and fields[r[0]][r[1]] != 'X' and r != point ]

    return res

def dfs(root, fields):
    q = deque()
    q.append(root)

    dist = copy.deepcopy(fields)

    for r in range(len(dist)):
        dist[r] = list(dist[r])
        for c in range(len(dist[r])):
            dist[r][c] = -1

    dist[root[0]][root[1]] = 0

    while q:
        p = q.pop()
        neighbors = get_neighbors(p, fields, r, c)
        
        for n in neighbors:
            if dist[n[0]][n[1]] == -1:
                dist[n[0]][n[1]]  = dist[p[0]][p[1]] + 1 
                q.append(n)

print(fields)
dfs((s_x, s_y), fields)





    

