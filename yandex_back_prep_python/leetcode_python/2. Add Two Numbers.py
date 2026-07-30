# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        list_1_cur, list_2_cur = l1, l2

        remainder = 0
        while l1 and l2:
            digit_val = l1.val + l2.val + remainder
            remainder = 0

           
            if digit_val < 10:
                cur.next = ListNode(val=digit_val)
                cur = cur.next
            else:
                print("digit_val :", digit_val)

                digit_val_rem_part = digit_val // 10
                digit_val_int_part = digit_val % 10

                remainder = digit_val_rem_part

                cur.next = ListNode(val=digit_val_int_part)
                cur = cur.next

            l1 = l1.next
            l2 = l2.next

        l_rest = l1 if l1 else l2

        while l_rest:
            digit_val = l_rest.val + remainder
            remainder = 0

            if digit_val < 10:
                cur.next = ListNode(val=digit_val)
                cur = cur.next
            else:
                digit_val_rem_part = digit_val // 10
                digit_val_int_part = digit_val % 10

                remainder = digit_val_rem_part

                cur.next = ListNode(val=digit_val_int_part)
                cur = cur.next

            l_rest = l_rest.next

        if remainder > 0:
            cur.next = ListNode(val=remainder)
            cur = cur.next

        return head.next
