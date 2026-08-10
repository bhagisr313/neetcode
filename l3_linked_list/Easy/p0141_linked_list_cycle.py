
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        my_set = set()
        while curr is not None:
            if curr not in my_set:
                my_set.add(curr)
            else:
                return True
            curr = curr.next
        return False
    
# Floyd's Tortoise and Hare Algorithm:
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False