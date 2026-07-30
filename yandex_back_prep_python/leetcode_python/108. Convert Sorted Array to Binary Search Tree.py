# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_tree(l, r, root):
            if l > r:
                return None

            m = (l + r) // 2

            root = TreeNode(nums[m])

            root.left = create_tree(l, m - 1, nums)
            root.right = create_tree(m + 1, r, nums)

            return root

        return create_tree(0, len(nums) - 1, nums)
