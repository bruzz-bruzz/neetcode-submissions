# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        r = root
        while r:
            if r.val > val:
                if r.left:
                    r = r.left
                else:
                    r.left = TreeNode(val)
                    break
            else:
                if r.right:
                    r = r.right
                else:
                    r.right = TreeNode(val)
                    break
        return root