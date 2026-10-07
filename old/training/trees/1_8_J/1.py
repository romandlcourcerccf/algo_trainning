import os
import sys

from collections import defaultdict
sys.setrecursionlimit(100000)


def read_lines(file:str)->list[str]:

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, file)
   
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    return rows

depths = dict()

def iterate(root, ierarchy):

    if root in depths:
        return depths[root]

    depth = 0
    def _iterate(root):

        nonlocal depth
        depth +=1
        child = ierarchy[root]
        if not child:
            return 
        
        if child in depths:
            depth += depths[child]
            return depth -1
        else:
            _iterate(child)
    
    _iterate(root)

    return depth-1
   
   
def main():

    rows = read_lines('input.txt')

    ierarchy = defaultdict(str)
    kings = set()
    
    for row in rows[1:]:

        decsendant, ansestor = row.split()
        kings.add(decsendant)
        kings.add(ansestor)
        ierarchy[decsendant] = ansestor


    res = []
    for king in kings:
        res.append((king, iterate(king, ierarchy)))
        
    
    res = sorted(res, key= lambda x: x[0], reverse=False)

    for r in res:
        print(*r)

  
if __name__ == '__main__':
    main()