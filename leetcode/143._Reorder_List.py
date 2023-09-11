# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        res = ListNode()
        
        lst = []

        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next
        
        l,r = 0, len(lst)-1
        cur = res
        while l < r:
            cur.next = lst[l]
            cur = cur.next
            cur.next = lst[r]
            cur = cur.next
            l +=1
            r -=1
        
        print('l :', l, 'r :', r)

        if l == r:
            cur.next = lst[l]
            cur = cur.next
            
        cur.next = None

        return res.next
