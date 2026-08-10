#brute force
from collections import defaultdict
from itertools import count


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = dict()
        result_array = []
        for ele in nums:
            nums_dict[ele]  = nums_dict.get(ele,0) + 1
        for k, v in nums_dict.items():
            if v > len(nums)//3:
                result_array.append(k)
        return result_array


#efficient solution
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = defaultdict(int)
        result = []
        for ele in nums:
            nums_dict[ele] += 1
        if len(nums_dict) > 2:
            nums_dict_copy = nums_dict
            for keys in nums_dict.items():
                nums_dict[keys] -= 1
                if nums_dict[keys] > 0:
                    nums_dict_copy.pop(keys)
            nums_dict = nums_dict_copy
        for k, v in nums_dict.items():
            if v > len(nums)//3 :
                result.append(k)
        return result

#boyer-moore method
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0
        result_array = []
        #phase1: finding candidate
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 += 1
            elif count2 == 0:
                cand2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        #phase 2: validating count
        count1 = 0
        count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        if count1 > (len(nums)//3):
            result_array.append(cand1)
        if count2 > (len(nums)//3):
            result_array.append(cand2)
        return result_array