# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # when both roots are empty
        if not p and not q:
            return True 
        # when either one of them is empty(not both are empty ) and unequal values
        if not p or not q or p.val != q.val:
                return False
        # when both are non-empty
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))