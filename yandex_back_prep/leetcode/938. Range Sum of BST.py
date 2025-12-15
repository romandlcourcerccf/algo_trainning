# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """

        self.acc = 0

        def dfs(root):
            if not root:
                return

            if low <= root.val <= high:
                self.acc += root.val

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return self.acc

    # Definition for a binary tree node.


# Iterartion


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.range_sum = 0

        # def dfs(root):
        #     if not root:
        #         return

        #     if low <= root.val <= high:
        #         self.range_sum += root.val

        #     dfs(root.left)
        #     dfs(root.right)

        # dfs(root)

        def dfs(root):
            stack = [root]

            cur = stack.pop()
            while cur:
                if low <= cur.val <= high:
                    self.range_sum += cur.val

                if cur.left:
                    stack.append(cur.left)

                if cur.right:
                    stack.append(cur.right)

                if stack:
                    cur = stack.pop()
                else:
                    cur = None

        dfs(root)

        return self.range_sum
