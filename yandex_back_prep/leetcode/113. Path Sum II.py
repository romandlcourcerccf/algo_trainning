# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    
        res = []

        def dfs(root, acc):

            if not root:
                return

            acc.append(root.val)

            if not root.left and not root.right and sum(acc) == targetSum:
                res.append(acc)
            
            dfs(root.left, acc.copy())
            dfs(root.right, acc.copy())

        dfs(root, [])

        return res


            

