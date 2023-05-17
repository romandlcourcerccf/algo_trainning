# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_path = None
        q_path = None

        nodes = {}

        def traverce(node, path, level):
            
            nonlocal nodes
            nodes[node.val] = node

            path.add((node.val, level))

            if node.val == p.val:
                nonlocal p_path
                p_path = path
            
            if node.val == q.val:
                nonlocal q_path
                q_path = path

            if node.left:
                traverce(node.left, path.copy(), level+1)
            if node.right:
                traverce(node.right, path.copy(), level+1)
        
        path = set()
        traverce(root, path, 0)

        common = p_path & q_path
        common = list(common)
        common.sort(key=lambda x: x[1])
        common = common[0]
       
        return nodes[common[0]]