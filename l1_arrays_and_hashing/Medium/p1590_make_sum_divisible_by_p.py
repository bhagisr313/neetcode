class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        my_dict = dict()
        if total_sum % p == 0:
            return 0
        prefix_sum_array = []
        for i in nums:
            prefix_sum += i
            prefix_sum_array.append(prefix_sum)
        for ele in range(0, len(nums)):
            if prefix_sum_array[ele] % total_sum - p not in my_dict():