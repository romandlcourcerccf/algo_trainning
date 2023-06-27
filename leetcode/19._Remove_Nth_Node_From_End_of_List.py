# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        l = dummy
        r = dummy
        for i in range(n):
            r = r.next
        
        while r.next:
            l = l.next
            r = r.next
            
        tmp = l.next
        if tmp:
            l.next = tmp.next

        print('l.val :',l.val)

        return dummy.next