# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        arr = []
        
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        l,r = 0, len(arr)-1
        prev = None
        head = None

        print('len :', len(arr))

        if len(arr) == 1:
            return head

        while l <= r:
            print('l :', l, 'r :', r)
            if l == 0:
                head = arr[l]
                arr[l].next = arr[r]
                prev = arr[r]
            else:
                prev.next = arr[l]
                arr[l].next = arr[r]
                prev = arr[r]
        
            l +=1
            r -=1

        arr[l].next = None

        if l == r+2:
            arr[l].next = arr[r+1]
            arr[r+1].next = None

        return head