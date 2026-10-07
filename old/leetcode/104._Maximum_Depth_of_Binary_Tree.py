# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.max_d = float('-inf')

        def dfs(root, depth):

            if not root:
                self.max_d = max(self.max_d, depth)
                return 

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)

        return self.max_d
    

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.max_depth = float('-inf')

        def dfs(root, depth):

            if not root:
                return 

            self.max_depth = max(self.max_depth, depth)

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root, 1)
        
        return self.max_depth if self.max_depth != float('-inf') else 0
    
  class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))