class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        overall_sum = sum(nums)
        pivot = 0
        sum_left = 0
        sum_right = overall_sum - nums[pivot]
        while pivot+1 < len(nums) and sum_left != sum_right:
            sum_left += nums[pivot]
            sum_right -= nums[pivot + 1]
            pivot += 1
        if sum_left != sum_right:
            return -1
        return pivot
            