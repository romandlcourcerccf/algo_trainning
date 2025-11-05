# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return head

        pos = head
        while pos.next:
            pos = pos.next

        hew_head = pos

        start = head
        end = None
        while start != hew_head:
            if not hew_head.next:
                hew_head.next = start
                _tmp = start
                start = start.next
                _tmp.next = None
                end = _tmp
            else:
                hew_head.next = start
                _tmp = start
                start = start.next
                _tmp.next = end
                end = _tmp

        return hew_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        old_head = new_head = head

        while new_head.next:
            new_head = new_head.next

        while old_head != new_head:
            if not new_head.next:
                tmp = old_head.next
                new_head.next = old_head
                old_head.next = None
                old_head = tmp
            else:
                tmp = old_head.next
                tmp2 = new_head.next
                new_head.next = old_head
                old_head.next = tmp2
                old_head = tmp

        return new_head
