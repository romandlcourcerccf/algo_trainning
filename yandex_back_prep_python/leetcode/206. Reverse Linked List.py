# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        new_head = head

        while new_head.next:
            new_head = new_head.next

        while cur != new_head:
            if not new_head.next:
                tmp = cur.next
                new_head.next = cur
                cur.next = None
                cur = tmp
            else:
                tmp = cur.next
                tmp2 = new_head.next
                new_head.next = cur
                cur.next = tmp2
                cur = tmp

        return new_head
