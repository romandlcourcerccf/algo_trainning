# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head

        if not cur:
            return head

        prev = cur
        cur = cur.next
        prev.next = None

        while cur:
            print(cur.val)
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # c=0
        # while prev:
        #     if c > 5:
        #         break
        #     c += 1
        #     print('>',prev.val)
        #     prev = prev.next 

        # print('+')
        return prev


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
        nxt = cur.next

        while nxt:


            tmp = nxt.next
            nxt.next = cur
        
            cur = nxt
            nxt = tmp
        
        head.next = None
        
        return cur

        
            