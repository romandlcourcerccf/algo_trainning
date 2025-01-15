import sys
from collections import defaultdict
import copy


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right

def search(val, root):

    if root._val is None:
        print('NO')
        return
    
    if root._val == val:
        print('YES')
        return
    
    elif root._val < val:
        if root._left:
            search(val, root._left)
        else:
            print('NO')
    else:
        if root._right:
            search(val, root._right)
        else:
            print('NO')

root = TreeNode()
print_path = []

def add(val, root):

    if root._val is None:
        root._val = val
        print('DONE')
        return
    
    if root._val == val:
        print('ALREADY')
        return

    elif root._val < val:
        if root._left:
            add(val, root._left)
        else:
            root._left = TreeNode(val=val)
            print('DONE')
    else:
        if root._right:
            add(val, root._right)
        else:
            root._right = TreeNode(val=val)
            print('DONE')


def print_tree(root, depth):

    if not root:
        return

    print_tree(root._left, depth+1)
    # print(f'{"." * depth} {root._val}')
    print_path.append(f'{"." * depth}{root._val}')
    print_tree(root._right, depth+1)


def main():
   
    rows = sys.stdin.readlines()

    # import os
    # dname = os.path.dirname(__file__)
    # filename = os.path.join(dname, '3.txt')
   
    # with open(filename, 'r') as f:
    #     rows = f.readlines()
    
    for row in rows:
        row = row.split()
        if len(row) == 1:
            op = row[0]
        else:
            op, val = row[0], int(row[1]) 

        match op:
            case 'ADD':
                add(val, root)
            case 'SEARCH':
                search(val, root)
            case 'PRINTTREE':
                print_path.clear()
                print_tree(root, 0)
                for p in print_path[::-1]:
                    print(p)
            

if __name__ == '__main__':
    main()
