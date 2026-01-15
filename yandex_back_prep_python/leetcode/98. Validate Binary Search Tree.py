# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.is_valid = True

        def dfs(root):

            if not root:
                return float('inf'), float('-inf')
                
            min_left, max_left = dfs(root.left)
            min_right, max_right = dfs(root.right)

            print(f'root {root.val} max_left {max_left} min_right {min_right}')

            if root.val >= min_right or root.val <= max_left:
                self.is_valid = False
                return 

            return min(min_left, root.val) , max(max_right, root.val)

        dfs(root)

        return self.is_valid