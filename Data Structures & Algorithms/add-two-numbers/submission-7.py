# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l,r = [],[]
        while l1:
            l.insert(0,str(l1.val))
            l1 = l1.next
        while l2:
            r.insert(0,str(l2.val))
            l2 = l2.next
        l = ''.join(l)
        r = ''.join(r)
        c = list(str(int(l) + int(r)))
        c = c[::-1]
        for x in range(len(c)):
            c[x] = ListNode(c[x])
        for x in range(len(c) - 1):
            c[x].next = c[x+1]
        return c[0]