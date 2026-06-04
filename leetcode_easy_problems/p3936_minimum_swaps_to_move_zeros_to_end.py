class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        length_of_nums = len(nums)
        zeros_count = nums.count(0)

        zero_position_array = nums[length_of_nums - 1: length_of_nums - 1 - zeros_count:-1]

        return sum(x != 0 for x in zero_position_array)
     