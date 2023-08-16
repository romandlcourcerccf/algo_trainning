# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        m_stones = set([p.val, q.val])
        tracks = []
        nodes = {}

        def dfs(root, path, level):

            if not root:
                return 
            
            nodes[root.val] = root

            path.append((root.val, level))

            if root.val in m_stones:
                m_stones.remove(root.val)
                tracks.append(path.copy())

            if not m_stones:
                return

            if root.left:
                dfs(root.left, path.copy(), level+1)

            if root.right:
                dfs(root.right, path.copy(), level+1)

            
        dfs(root, [], 0)
        print(tracks)

        merged = set(tracks[0]) & set(tracks[1])
        merged = list(merged)
        merged.sort(key=lambda x: x[1], reverse=True)

        return nodes[merged[0][0]]