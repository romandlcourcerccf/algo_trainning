import sys
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)

def main():
   
    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '3.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()
    
    tree = defaultdict(set)
  
    mirrored_tree =  defaultdict(set)

    adges_list = []
    for row in rows[1:]:
        row[0], row[1] = row.split()
        adges_list.append((row[0], row[1]))
    
    while adges_list:
        adge = adges_list.pop()
        print(adge)
        if adge[0] not in tree and adge[1] not in mirrored_tree:
            adges_list.append(adge)
            continue
        el
        
    
    for row in rows[1:]:
        row[0], row[1] = row.split()
        if row[0] == 1:
            tree[row[0]].add(row[1])
            mirrored_tree[[1]].add(row[0])
        else:
            if row[0] in 
        

    # print(hierachy)

    # res = {}

    # def dfs(root):

    #     print(f'-->{root}')
        
    #     if root not in hierachy:
    #         res[root] = 1
    #         return 1
        
    #     # print(f'-->{root}')

    #     _vert_sum = sum([dfs(c) for c in hierachy[root]]) + 1

    #     res[root] = _vert_sum

    #     return _vert_sum

    # dfs(1)

    # vertices = sorted(list(res.keys()))
    # depth = [str(res[v]) for v in vertices]

    # print(' '.join(depth))

if __name__ == '__main__':
    main()
