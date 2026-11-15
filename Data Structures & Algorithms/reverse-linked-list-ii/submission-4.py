# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(ListNode(head.val))
            head = head.next
        if not arr:
            return ListNode().next
        left -= 1
        right -= 1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]