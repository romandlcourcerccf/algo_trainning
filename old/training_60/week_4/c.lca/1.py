import sys
from collections import defaultdict
import copy


sys.setrecursionlimit(100000)

def main():
   
    # rows = sys.stdin.readlines()

    import os
    dname = os.path.dirname(__file__)
    filename = os.path.join(dname, '1.txt')
   
    with open(filename, 'r') as f:
        rows = f.readlines()
    
    hierachy = defaultdict(list)
    nodes_set = set()
   
    for row in rows[1:]:
        row = row.split()
        nodes_set.add(row[0])
        nodes_set.add(row[1])
        hierachy[row[1]].append(row[0])
    

    result = set()

    _path = []
    def dfs(root, target, path, depth):
        
        nonlocal _path
        if root == target or root not in hierachy:
            _path.extend(path)
            return

        for child in hierachy[root]:

            l_path = copy.copy(path)
            l_path.append((root, depth))
        
            dfs(child, target, l_path, depth+1)

    saved_paths = {}
    
    for row in rows[1:]:
        row = row.split()
        mon1 = row[0]
        mon2 = row[1]

        if mon1 not in saved_paths:
            

         
        

    

      
       

    


   
    
   
if __name__ == '__main__':
    main()
