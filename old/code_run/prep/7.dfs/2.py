import os
import sys
from collections import defaultdict

def get_rows()->list[str]:
    
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, '1.txt')

    with open(file_name, 'r') as reader:
        rows = reader.readlines()
        rows = [tuple(map(int,r.split())) for r in rows]
        
    return rows

rows = get_rows()
verts = set()

graph = defaultdict(set)

for r in rows:
    verts.add(r[0])
    verts.add(r[1])

    graph[r[0]].add(r[1])
    # graph[r[1]].add(r[0])

adjacency_list = [None] * (len(verts)+1)
print(graph)

print(adjacency_list)

def dfs(root: int, vert_num: int):
    adjacency_list[root] = vert_num
    for v in graph[root]:
        if not adjacency_list[v]:
            dfs(v, vert_num)

vert_num = 1
for v in verts:
    if not adjacency_list[v]:
        vert_num += 1
        dfs(v, vert_num)

print(adjacency_list)


