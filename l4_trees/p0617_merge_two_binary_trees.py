# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root1, root2):

            if root1 is None and root2 is None:
                return
            elif root1 is None:
                return TreeNode(root2.val, dfs(None, root2.left), dfs(None, root2.right) )
            elif root2 is None:
                return TreeNode(root1.val, dfs(root1.left, None), dfs(root1.right, None))
            else:
                return TreeNode(root1.val + root2.val, dfs(root1.left, root2.left), dfs(root1.right, root2.right))
        
        return dfs(root1, root2)