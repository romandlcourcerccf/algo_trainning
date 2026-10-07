import os
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right

class Tree:
    def __init__(self):
        self._root = None
        self._depth = 0

    # def add_val(self, val):

    #     if not self._root:
    #         self._root = TreeNode(val=val)
    #         return 1

    #     cur = self._root
    #     _local_depth = 1
    #     while cur:
    #         _local_depth +=1
    #         if cur._val == val:
    #             break
    #         elif cur._val < val:
    #             if not cur._left:
    #                 cur._left = TreeNode(val=val)
    #                 break
    #             else:
    #                 cur = cur._left
                    
    #         else:
    #             if not cur._right:
    #                 cur._right = TreeNode(val=val)
    #                 break
    #             else:
    #                 cur = cur._right
                    
    #     return _local_depth
        
    def add_val(self, val):

        if not self._root:
            self._root = TreeNode(val=val)
            return 1
        
        self._depth = 1
        def iterate(root, depth, val):

            if not root:
                return
            
            if root._val == val:
                self._depth = -1
                return 
            
            self._depth+=1

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

        return self._depth
        
def main():

    dir_name = os.path.dirname(__file__)
    # filename = os.path.join(dir_name, "9.txt")
    filename = os.path.join(dir_name, "input.txt")
    
    with open(filename ,'r') as reader:
        rows = reader.readlines()
        rows = [r.rstrip() for r in rows]

    tree_info = list(map(int, rows[0].split()))
    tree_info = list(map(int, tree_info))

    tree = Tree()

    res = []
    for n in tree_info[:-1]:
        d = tree.add_val(n)
        if d > 0:
            res.append(d)
    
    print(*res)
  


if __name__ == '__main__':
    main()