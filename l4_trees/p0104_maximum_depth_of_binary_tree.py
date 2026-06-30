# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxHeight(node):
            if node is None:
                return 0
            leftHeight = maxHeight(node.left)
            rightHeight = maxHeight(node.right)
            return max(leftHeight, rightHeight) + 1
        return maxHeight(root)