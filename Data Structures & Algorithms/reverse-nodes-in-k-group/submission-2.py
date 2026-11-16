# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(ListNode(head.val))
            head = head.next
        if not arr:
            return ListNode().next
        for x in range(len(arr) // k):
            l,r = (x * k), (x * k) + k - 1
            while l < r:
                arr[l],arr[r] = arr[r],arr[l]
                l += 1
                r -= 1
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]