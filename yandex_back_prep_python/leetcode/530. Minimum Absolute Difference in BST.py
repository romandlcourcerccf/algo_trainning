# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []

        def dfs(root):
            if not root:
                return

            vals.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        vals.sort()

        min_dist = float("inf")

        for i in range(1, len(vals)):
            min_dist = min(min_dist, abs(vals[i] - vals[i - 1]))

        return min_dist
