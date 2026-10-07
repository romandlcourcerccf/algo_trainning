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
        cur = p
        p_track = []

        while cur:
            p_track.append(cur)
            if cur.val == q.val:
                return q

            cur = cur.parent

        cur = q
        q_track = []
        while cur:
            q_track.append(cur)
            if cur.val == p.val:
                return p

            cur = cur.parent

        print([n.val for n in p_track])
        print([n.val for n in q_track])

        p_track = p_track[::-1]
        q_track = q_track[::-1]

        pos = 0
        while p_track[pos].val == q_track[pos].val:
            pos += 1

        return p_track[pos - 1]
