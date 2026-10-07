# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        lns = []
        for l in lists:
            lns.append(len(l))

        while lns:
            tmp = []
            for i in range(len(lists)):
                if lns[i] > 0:
                    tmp = lists[i].pop()
                    lns[i] -= 1
                else:
                    del lns[i]
                    del lists[i]

            res += sorted(tmp)

        return res
