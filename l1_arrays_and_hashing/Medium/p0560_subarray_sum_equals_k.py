class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {0:1}
        prefix_sum = 0
        result = 0
        for ele in nums:
            prefix_sum += ele
            diff = prefix_sum - k
            result += my_dict.get(diff, 0)
            my_dict[prefix_sum] = my_dict.get(prefix_sum, 0) + 1
        return result


#Alternate solution:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {0:1}
        prefix_sum = 0
        result = 0
        for ele in nums:
            prefix_sum += ele
            diff = prefix_sum - k
            if diff in my_dict:
                result += my_dict[diff]
            my_dict[prefix_sum] = my_dict.get(prefix_sum, 0) + 1
        return result