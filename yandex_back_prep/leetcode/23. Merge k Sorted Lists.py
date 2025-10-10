# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge_2_lists(self, list1, list2):
        res = ListNode()
        cur = res

        pos1 = list1
        pos2 = list2

        while pos1 and pos2:
            if pos1.val <= pos2.val:
                cur.next = ListNode(val=list1.val)
                cur = cur.next
                pos1 = pos1.next
            else:
                cur.next = ListNode(val=list2.val)
                cur = cur.next
                pos2 = pos2.next

        if pos1:
            while pos1:
                cur.next = ListNode(val=list1.val)
                cur = cur.next
                pos1 = pos1.next
                
        elif pos2:
            while pos2:
                cur.next = ListNode(val=list2.val)
                cur = cur.next
                pos2 = pos2.next

        return res.next

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()

            merged_list = self.merge_2_lists(l1, l2)
            lists.append(merged_list)

        print(len(lists))

        return lists[0]

