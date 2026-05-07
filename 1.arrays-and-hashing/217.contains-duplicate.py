# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in nums:
            if i not in my_set:
                my_set.add(i)
            else:
                return True
        return False
# can be solved using brute force as well but that would be O(n^2) time complexity, using a set gives us O(n) time complexity and O(n) space complexity
