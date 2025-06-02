# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root

        cur = root
        parent = cur

        while True:
            if key > cur.val:
                if not cur.right:
                    return root
                parent = cur
                cur = cur.right
            elif key < cur.val:
                if not cur.left:
                    return root
                parent = cur
                cur = cur.left
            else:
                if cur.val == parent.val:
                    print(f'>>>> root>>> { cur.val }')
                if not cur.left and  not cur.right:
                    if parent.left == cur:
                        parent.left = None
                    elif  parent.right == cur:
                        parent.right = None
                    
                else:
                    if parent.right == cur:
                        parent.right = cur.right
                        self.insert(cur.right, cur.left)
                    elif parent.left == cur:
                        parent.left = cur.left
                        self.insert(cur.left, cur.right)

                return root

    def insert(self, root, node):
        if not node:
            return
        cur = root
        while True:
            if node.val > root.val:
                if not cur.right:
                    cur.right = node
                    return
                cur = cur.right
            else:
                if not cur.left:
                     cur.left = node
                     return 
                cur = cur.left



