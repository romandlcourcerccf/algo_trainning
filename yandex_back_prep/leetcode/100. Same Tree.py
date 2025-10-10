# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.res = True

        def dfs(p, q):

            if not p and not q:
                return 

            if p and not q or not p and q or p.val != q.val:
                print('Bingo!')
                self.res = False
                return 
            
            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)

        return self.res