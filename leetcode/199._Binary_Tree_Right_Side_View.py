# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        path = []

        d = defaultdict(list)

        def dfs(root, level):
            if not root:
                return

            d[level].append(root.val)

            if root.left:
                dfs(root.left, level + 1)

            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 0)

        res = []

        levels = sorted(list(d.keys()))

        for level in levels:
            res.append(d[level][-1])

        return res

        return path


# Easier solutiobn


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        h = defaultdict(list)

        def dfs(root, level):
            if not root:
                return

            h[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        res = []

        for v in h.values():
            res.append(v[-1])

        return res
