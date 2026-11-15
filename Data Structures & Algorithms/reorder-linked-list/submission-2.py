# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        h = head
        while h:
            arr.append(h.val)
            h = h.next
        n = []
        while arr:
            if arr:
                n.append(arr.pop(0))
            if arr:
                n.append(arr.pop())
        h = head
        while h:
            h.val = n.pop(0)
            h = h.next