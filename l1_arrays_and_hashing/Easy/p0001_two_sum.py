# 1. Two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# faster solution using a dictionary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(0,len(nums)):
            key = i
            value = nums[i]
            if target - value not in my_dict:
                my_dict[value] = key
            else:
                return [key, my_dict[target - value]]