# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.is_balansed = True

        def dfs(root):

            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            if abs(l-r) >=2:
                self.is_balansed = False
            
            return max(l, r)+1

        dfs(root)

        return self.is_balansed