
from collections import deque

g = [{1}, {0,2}, {1}, {4}, {3}] 
g_size = 5

def bfs(root):

    q = deque()
    q.append(root)

    d = [-1] * g_size
    p = [-1] * g_size

    d[root] = 0

    while q:
        v = q.pop()
        print('v :', v)
        for u in g[v]:
            print('u >> :',u)
            if d[u] == -1:
                q.append(u)
                d[u] = d[v] + 1
                p[u] = v
                
    return d, p 

d, p = bfs(0)

print('d :',d)
print('p :',p)

v = 2
while v !=0:
    print(v)
    v = p[v]

# d, p = bfs(3)

# print('d :',d)
# print('p :',p)

