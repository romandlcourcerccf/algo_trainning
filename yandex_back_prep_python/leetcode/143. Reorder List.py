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

        reardered_list = []
        res = ListNode()

        temp = head
        while temp:
            reardered_list.append(temp)
            temp = temp.next

        temp = res
        l, r = 0, len(reardered_list) - 1

        while l <= r:
            temp.next = reardered_list[l]
            temp = temp.next
            temp.next = reardered_list[r]
            temp = temp.next
            temp.next = None

            l += 1
            r -= 1

        return res.next
