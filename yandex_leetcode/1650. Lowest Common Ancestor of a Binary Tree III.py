"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":

        track = []

        def up(node):
            if not node:
                return

            track.append((node.val, node))
            up(node.parent)

        up(p)
        track1 = track

        track = []
        up(q)
        track2 = track

        self.lowest = None

        while track1 and track2:
            if track1[-1][0] == track2[-1][0]:
                self.lowest = track1[-1][1]

            track1.pop()
            track2.pop()

        return self.lowest
