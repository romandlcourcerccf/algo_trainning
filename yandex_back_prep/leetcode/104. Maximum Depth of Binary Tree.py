# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_dephth = float("-inf")

        def dfs(root, depth):
            if not root:
                return

            depth += 1

            self.max_dephth = max(self.max_dephth, depth)

            dfs(root.left, depth)
            dfs(root.right, depth)

        dfs(root, 0)

        return self.max_dephth if self.max_dephth != float("-inf") else 0
