class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      my_dict = dict()
      for i in nums:
        my_dict[i] = my_dict.get(i,0) + 1
      for k, v in my_dict.items():
        if v == 1:
          return k