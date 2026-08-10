# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeightAndBalanced(node):
            if node is None:
                return [True, 0]
            leftValue = getHeightAndBalanced(node.left)
            rightValue = getHeightAndBalanced(node.right)

            checkBalance = leftValue[0] and rightValue[0] and abs(leftValue[1] - rightValue[1]) <= 1
            return [checkBalance, max(leftValue[1], rightValue[1])+1]

        finalResult = getHeightAndBalanced(root)
        return finalResult[0]