# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balansed = True

        def dfs(root):
            if not root:
                return 0

            # if self.is_balansed == False:
            #     return 0

            dp_left = dfs(root.left)
            dp_right = dfs(root.right)

            if abs(dp_left - dp_right) >= 2:
                self.is_balansed = False

            return max(dp_left, dp_right) + 1

        dfs(root)

        return self.is_balansed
