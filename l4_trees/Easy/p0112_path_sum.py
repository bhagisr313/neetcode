# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, running_sum):
            if root is None:
                return False
            running_sum += root.val
            if root.left is None and root.right is None:
                if running_sum == targetSum:
                    return True
                else:
                    return False
            return dfs(root.left, running_sum) or dfs(root.right, running_sum)
        return dfs(root,0)