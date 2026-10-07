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
            return 1

        cur = self._root
        _local_depth = 1
        while cur:
            _local_depth +=1
            if cur._val == val:
                break
            elif cur._val < val:
                if not cur._left:
                    cur._left = TreeNode(val=val)
                    break
                else:
                    cur = cur._left
                    
            else:
                if not cur._right:
                    cur._right = TreeNode(val=val)
                    break
                else:
                    cur = cur._right
                    
        return _local_depth
        
    def iter(self):
    
        path = []
        def _iter(root):
            if not root:
                return
            
            _iter(root._left)
            path.append(root._val)
            _iter(root._right)

        _iter(self._root)
        return path[1]


        
def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "1.txt")
    filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    tree_info = list(map(int, rows[0].split()))
    tree_info = list(map(int, tree_info))


    tree = Tree()

    res = []
    for n in tree_info[:-1]:
        res.append(tree.add_val(n))
    
    print(tree.iter())

  
if __name__ == '__main__':
    main()