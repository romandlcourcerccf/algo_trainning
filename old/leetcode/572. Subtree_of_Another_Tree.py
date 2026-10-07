# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.same = True
        self.hits = 0

        def the_same(l, r):
            if not l and not r:
                return

            if (not l and r) or (l and not r) or (l.val != r.val):
                self.same = False
                return

            the_same(l.left, r.left)
            the_same(l.right, r.right)

        def dfs(root):
            if not root:
                return

            if root.val == subRoot.val:
                self.same = True
                the_same(root, subRoot)
                self.hits += int(self.same)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return self.hits > 0
