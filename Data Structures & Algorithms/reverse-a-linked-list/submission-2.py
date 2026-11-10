# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.reverse()
        if not arr:
            return ListNode().next
        for x in range(len(arr)):
            arr[x] = ListNode(arr[x])
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]