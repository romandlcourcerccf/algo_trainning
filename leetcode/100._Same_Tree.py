# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.is_same = True

        def dfs(l, r):

            if not l and not r:
                return

            if (l and not r) or (r and not l) or l.val != r.val:
                self.is_same = False
                return 
            
            dfs(l.left, r.left)
            dfs(l.right, r.right)


        dfs(p, q)

        return self.is_same 
