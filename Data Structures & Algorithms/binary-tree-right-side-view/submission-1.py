# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = [root]
        if not root:
            return res
        while stk:
            same = []
            for _ in range(len(stk)):
                p = stk.pop(0)
                if p.left:
                    stk.append(p.left)
                if p.right:
                    stk.append(p.right)
                same.append(p.val)
            res.append(same)
        arr = []
        for x in res:
            arr.append(x[len(x) - 1])
        return arr