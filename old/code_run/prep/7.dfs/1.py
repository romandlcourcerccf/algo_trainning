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
graph = defaultdict(set)

for r in rows:
    graph[r[0]].add(r[1])
    # graph[r[1]].add(r[0])

print(graph)

def dfs(root, path):

    path.add(root)

    if root not in  graph:
        return
    
    for v in graph[root]:
        if v not in path:
           
            dfs(v, path)


path = set()
root = 1

dfs(1, path)

print(path)
