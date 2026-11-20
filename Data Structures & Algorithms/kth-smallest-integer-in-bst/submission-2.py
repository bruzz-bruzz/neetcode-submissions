# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def recur(r):
            if not r:
                return 
            recur(r.left)
            arr.append(r.val)
            recur(r.right)
        recur(root)
        return arr[k - 1]