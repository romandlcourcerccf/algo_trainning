# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        self.is_summetric = True

        def dfs(p , q):

            if not p and not q:
                return 

            if p and not q or not p and q or p.val != q.val:
                self.is_summetric = False
                return 

            dfs(p.left , q.right)
            dfs(p.right , q.left)

        
        dfs(root , root)

        return self.is_summetric
        