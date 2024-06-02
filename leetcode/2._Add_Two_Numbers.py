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
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy

        rem = 0
        while l1 and l2:
            s = l1.val + l2.val + rem
            if s < 10:
                cur.next = ListNode(s)
                cur = cur.next
                rem = 0
            else:
                cur.next = ListNode(s-10)
                cur = cur.next
                rem=1
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            l = l1
        else:
            l = l2

        while l:
            s = l.val+rem
            if s < 10:
                cur.next = ListNode(s)
                cur = cur.next
                rem = 0
            else:
                cur.next = ListNode(s-10)
                cur = cur.next
                rem=1
            l = l.next
        
        if rem > 0:
            cur.next = ListNode(rem)
            cur = cur.next

        return dummy.next