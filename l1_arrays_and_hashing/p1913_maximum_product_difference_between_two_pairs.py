class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_max = 0
        second_max = 0
        first_small = float("inf")
        second_small = float("inf")

        for i in range(0,len(nums)):

            if nums[i] > second_max:
                second_max = nums[i]
            if nums[i] > first_max:
                second_max = first_max
                first_max = nums[i]
            if nums[i] < second_small:
                second_small = nums[i]
            if nums[i] < first_small:
                second_small = first_small
                first_small = nums[i]
        
        return first_max * second_max - first_small * second_small