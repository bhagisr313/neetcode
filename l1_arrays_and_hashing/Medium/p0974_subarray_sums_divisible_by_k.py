class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        my_dict = {0:1}
        prefix_sum = 0
        result = 0
        for ele in nums:
            prefix_sum += ele
            diff = prefix_sum % k
            if diff in my_dict:
                result += my_dict[diff]
            my_dict[prefix_sum % k] = my_dict.get(prefix_sum % k, 0) + 1
        return result