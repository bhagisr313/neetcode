# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         my_set = set()

#         for i in nums:
#             if i not in my_set:
#                 my_set.add(i)
#             else:
#                 my_set.remove(i)
#         return my_set.pop()

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) -1
        
        while( l <= h ):
            m = l + ((h - l)//2)
            
