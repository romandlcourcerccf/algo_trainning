# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_same = False

        def is_same(p, q):
            if not p and not q:
                return

            if p and not q or not p and q or p.val != q.val:
                self._is_same = False
                return

            is_same(p.left, q.left)
            is_same(p.right, q.right)

        def dfs(root, sub_root):
            if not root:
                return

            if root.val == sub_root.val:
                self._is_same = True
                is_same(root, sub_root)

                if self._is_same:
                    self.is_same = True
                    return

            dfs(root.left, sub_root)
            dfs(root.right, sub_root)

        dfs(root, subRoot)

        return self.is_same
