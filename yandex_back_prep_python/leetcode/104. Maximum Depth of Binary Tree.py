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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = 1 + self.maxDepth(root.left)
        right_height = 1 + self.maxDepth(root.right)

        return max(left_height, right_height)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = float("-inf")

        def dfs(root, depth):
            if not root:
                return

            self.max_depth = max(self.max_depth, depth)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)

        return self.max_depth if self.max_depth != float("-inf") else 0
