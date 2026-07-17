# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def in_order(root):
            if root is None:
                return 
            in_order(root.left)
            if root.left is None and root.right is None:
                leaves.append(root.val)
            in_order(root.right)
            return leaves
        leaves = []
        leaves1 = in_order(root1)
        leaves = []
        leaves2 = in_order(root2)

        if len(leaves1) != len(leaves2):
            return False
        
        for i in range(0,len(leaves1)):
            if leaves1[i] != leaves2[i]:
                return False
        return True