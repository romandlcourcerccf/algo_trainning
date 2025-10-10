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





        