import os
from collections import defaultdict

import sys

sys.setrecursionlimit(100000)


def read_lines(file:str)->list[str]:

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, file)
   
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    return rows

cash = dict()

def iterate(root, ierarchy):

    if root in cash:
        return cash[root]

    path = []
    def _iterate(root):
        path.append(root)
        for child in ierarchy[root]:
            _iterate(child)
    
    _iterate(root)


    cash[root] = len(path)-1
    return len(path)-1
   
   
def main():

    rows = read_lines('1.txt')

    ierarchy = defaultdict(set)
    kings = set()
    

    for row in rows[1:]:

        decsendant, ansestor = row.split()
        kings.add(decsendant)
        kings.add(ansestor)
        ierarchy[ansestor].add(decsendant)

    res = []
    for king in kings:
        res.append((king, iterate(king, ierarchy)))
        
    
    res = sorted(res, key= lambda x: x[0], reverse=False)

    for r in res:
        print(*r)

  
if __name__ == '__main__':
    main()