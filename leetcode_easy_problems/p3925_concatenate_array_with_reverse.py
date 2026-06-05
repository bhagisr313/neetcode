class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return [*nums, *nums[-1: -len(nums)-1: -1]]