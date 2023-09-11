# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        path = []

        def dfs(root, path):
            if not root:
                return 

            dfs(root.left, path)
            path.append(root.val)
            dfs(root.right, path)

        dfs(root, path)
        print(path)

        return path[k-1]