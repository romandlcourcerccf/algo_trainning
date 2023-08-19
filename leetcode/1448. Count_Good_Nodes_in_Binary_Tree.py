# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = []

        def dfs(root, path):

            if not root:
                return

            if not path:
                good_nodes.append(root.val)
            else:
                if root.val >= max(path):
                        good_nodes.append(root.val)


            path.append(root.val)

            if root.left:
                dfs(root.left, path.copy())

            if root.right:
                dfs(root.right, path.copy())

        dfs(root, [])


        return len(good_nodes)