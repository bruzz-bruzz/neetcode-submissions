# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        c = []
        for x in lists:
            while x:
                c.append(x.val)
                x = x.next
        c.sort()
        if not c:
            return ListNode().next
        for x in range(len(c)):
            c[x] = ListNode(c[x])
        for x in range(len(c) - 1):
            c[x].next = c[x+1]
        return c[0]