class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            der_index = abs(i) - 1
            nums[der_index] = -abs(nums[der_index])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res