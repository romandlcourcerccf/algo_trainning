# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode()
        res = dummy
        cur1 = l1
        cur2 = l2

        mem = 0

        while cur1 and cur2:
            s = cur1.val + cur2.val
            print('cur1.val :', cur1.val, ' cur2.val :', cur2.val)
            _mem = mem
            s = s + _mem
            if s >= 10:
                mem = s // 10
                rem = s % 10
                dummy.next = ListNode(rem)
            else:
                mem = 0
                dummy.next = ListNode(s)
            
            dummy = dummy.next
            cur1 = cur1.next
            cur2 = cur2.next

        return res.next