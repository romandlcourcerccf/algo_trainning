import sys
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)

def main():
   
    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '2.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()
    
    tree = defaultdict(set)
    result = defaultdict(int)

    def dfs(root, visited):

        parent_number = 0

        for c in tree[root]:
            if c not in visited:
                visited.add(c)
                parent_number += dfs(c, visited)
               
        result[root] = parent_number + 1
        return parent_number + 1

    # vertices = list(range(1, int(rows[0])+1))
 
    for row in rows[1:]:
        row = row.split()
        _start_node = int(row[0])
        _end_node = int(row[1])
        
        tree[_start_node].add(_end_node)
        tree[_end_node].add(_start_node)
        

    # print(tree)

    v  = set()
    v.add(1)
    dfs(1, v)

    result = [ (k,v)  for (k,v) in result.items()]
    result.sort(key= lambda x: x[0])
    result = [i[1] for i in result]
    result = ' '.join([str(r) for r in result])

    print(result)


if __name__ == '__main__':
    main()
