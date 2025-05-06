import sys
import os

class TreeNode:

    def __init__(self, val: None, left: None, right: None):
        self.val = val
        self.left = left
        self.right = right
    

def insert(val, root):

    if val <= root.val:
        if not root.left:
            root.left = TreeNode(val=val)
            return
        else:
            root = root.left
    else:
        if not root.right:
            root.right = TreeNode(val=val)
            return
        else:
            root = root.right


def iterate(root):

    if not root:
        return
    
    print(root.val)
    iterate(root.left)
    iterate(root.right)


def main():


    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")

    with open(filename ,'r') as reader:
        rows = reader.readlines()
    
    numbers = map(int, rows[0].split())

    print(numbers)

        
        
        




if __name__ == '__main__':
    main()