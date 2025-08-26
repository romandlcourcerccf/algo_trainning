import os
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right

class Tree:
    def __init__(self):
        self._root = None

    def add_val(self, val):

        if not self._root:
            self._root = TreeNode(val=val)
            return
        
        def iterate(root, depth, val):

            if not root:
                return
            
            if root._val == val:
                return
            
            if root._val < val:
                if not root._left:
                    root._left = TreeNode(val=val)
                    return
                else:
                    iterate(root._left, depth+1, val)

            elif root._val > val:
                if not root._right:
                    root._right = TreeNode(val=val)
                    return
                else:
                    iterate(root._right, depth+1, val)
        
        iterate(self._root, 1, val)

    
    def is_balanced(self):
    
        is_avl = True
        def _iter(root):

            if not root:
                return 0
            
            right_height = _iter(root._right)
            left_height = _iter(root._left)

            if abs(right_height-left_height) > 1:
                is_avl = False
                
            return max(right_height, left_height) + 1

        _iter(self._root)

        return is_avl


def main():

    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "1.txt")
    # filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    tree_info = list(map(int, rows[0].split()))
    tree_info = list(map(int, tree_info))


    tree = Tree()

    res = []
    for n in tree_info[:-1]:
        res.append(tree.add_val(n))
    
    print('YES' if tree.is_balanced() else 'NO')

  
if __name__ == '__main__':
    main()