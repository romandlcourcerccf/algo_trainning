# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root, source):
            if not root:
                return

            if source == "left" and not root.left and not root.right:
                self.res += root.val

            dfs(root.left, "left")
            dfs(root.right, "right")

        dfs(root, "")

        return self.res
