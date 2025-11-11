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
        self.p_path = None
        self.q_path = None

        def up(current, target, track):
            if not current:
                return

            track.append(current)
            if current.val == target.val:
                return

            up(current.parent, target, track)

        p_track = []
        up(p, q, p_track)
        print("p_track : ", [n.val for n in p_track])

        q_track = []
        up(q, p, q_track)
        print("q_track : ", [n.val for n in q_track])

        if p_track[-1].val == q.val:
            return q
        elif q_track[-1].val == p.val:
            return p
        else:
            pos1 = pos2 = 0
            p_track = p_track[::-1]
            q_track = q_track[::-1]

            cur_node = None
            while pos1 <= len(p_track) and pos2 < len(q_track):
                if p_track[pos1].val == q_track[pos2].val:
                    cur_node = p_track[pos1]
                    pos1 += 1
                    pos2 += 1
                else:
                    break

        return cur_node
