import sys
import os

class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def insert(val, root):

    if val <= root.val:
        if not root.left:
            root.left = TreeNode(val=val)
            return
        else:
            insert(val, root.left)
    else:
        if not root.right:
            root.right = TreeNode(val=val)
            return
        else:
            insert(val, root.right)


def iterate(root):

    if not root:
        return

    iterate(root.left)
    print(root.val)
    iterate(root.right)

def main():


    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "5.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()

    # rows = sys.stdin.readlines()
    
    vals = list(map(int, rows[0].split()))
    vals = vals[:-1]
    
    root = None
    for val in vals:
        if not root:
            root = TreeNode(val=val)
        else:
            insert(val, root)

    iterate(root)


        
        
        




if __name__ == '__main__':
    main()