# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def recur(r,m):
            if not r:
                return
            if r.val >= m:
                res.append(r.val)
            recur(r.left,max(r.val,m))
            recur(r.right,max(r.val,m))
        recur(root,float('-inf'))
        return len(res)