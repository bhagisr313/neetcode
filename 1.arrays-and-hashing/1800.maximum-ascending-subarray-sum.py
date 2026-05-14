# 1800. Maximum Ascending Subarray Sum
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result_inc_sum = nums[0]
        max_sum = nums[0]
        j = 1
        for i in range(0,len(nums)-1):
            j = i + 1
            if nums[i] < nums[j]:
                result_inc_sum += nums[j]
            else :
                result_inc_sum = nums[j]
            max_sum = max(max_sum, result_inc_sum)
        return max_sum