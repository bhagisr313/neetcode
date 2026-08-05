class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        count_of_zero = nums.count(0)
        for num in nums:
            if num != 0:
                product *= num
        if count_of_zero == 0:
            for j in range(0, len(nums)):
                result.append(product//nums[j])
        elif count_of_zero == 1:
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            return [0] * len(nums)
        return result