# Definition for a binary tree node.
# Using global range_sum
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.running_sum = 0
        def dfs(root):
            if root is None:
                return
            if root.val >= low and root.val <= high:
                self.running_sum += root.val

            if root.val < low:
                dfs(root.right)
            elif root.val > high:
                dfs(root.left)
            else:
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.running_sum
    
# without using global range_sum
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if root is None:
                return 0
            if root.val < low:
                return dfs(root.right)
            elif root.val > high:
                return dfs(root.left)
            else:
                return root.val + dfs(root.left) + dfs(root.right)
        return dfs(root)