# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        head = res

        rem = 0
        pos1, pos2 = l1, l2

        while pos1 and pos2:

            print('>>')
        
            d = pos1.val + pos2.val + rem

            if d < 10:
               res.next =  ListNode(val=d)
               res = res.next
            else:
                floor = d // 10
                _rem = d % 10
                res.next =  ListNode(val=_rem)
                res = res.next
                rem = floor

            pos1 = pos1.next
            pos2 = pos2.next

        while pos1:
            d = pos1.val + rem

            if d < 10:
               res.next =  ListNode(val=d)
               res = res.next
            else:
                floor = d // 10
                _rem = d % 10
                res.next =  ListNode(val=_rem)
                res = res.next
                rem = floor

            pos1 = pos1.next

        while pos2:
            d = pos2.val + rem

            if d < 10:
               res.next =  ListNode(val=d)
               res = res.next
               rem = 0
            else:
                floor = d // 10
                _rem = d % 10
                res.next =  ListNode(val=_rem)
                res = res.next
                rem = floor

            pos2 = pos2.next


        print('rem :', rem)

        if rem > 0:
            res.next =  ListNode(val=rem)
            res = res.next

        return head.next