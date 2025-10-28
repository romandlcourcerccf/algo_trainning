# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.res = []

        self.q_track = None
        self.p_track = None

        def dfs(root, track):
            if not root:
                return

            track.append(root)

            if root.val == p.val:
                self.p_track = track.copy()

            if root.val == q.val:
                self.q_track = track.copy()

            dfs(root.left, track.copy())
            dfs(root.right, track.copy())

        dfs(root, [])

        pos = 0
        min_eq = -1

        while pos < len(self.p_track) and pos < len(self.q_track):
            if self.p_track[pos] == self.q_track[pos]:
                min_eq = pos

            pos += 1

        print("min_eq :", min_eq)

        return self.q_track[min_eq]
