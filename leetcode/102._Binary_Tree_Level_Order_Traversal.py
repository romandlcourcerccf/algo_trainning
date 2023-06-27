from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not(root):
            return []
            
        d = defaultdict(list)

        def dfs(node, depth = 0):

            d[depth].append(node.val)
            
            if node.left:
                dfs(node.left, depth+1)
        
            if node.right:
                dfs(node.right, depth+1)

        dfs(root, 0)

        print(list(d.values()))

        return list(d.values())