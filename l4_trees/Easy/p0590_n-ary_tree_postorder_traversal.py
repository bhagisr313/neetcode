
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def helper(root):
            if not root:
                return
            for i in root.children:
                helper(i)
                result.append(i.val)
        helper(root)
        if root:
            result.append(root.val)
        return result