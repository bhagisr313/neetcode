class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = 0
        majority_ele = nums[0]
        for i in nums:
            if count == 0:
                majority_ele = i
            count += (1 if i == majority_ele else -1)
        count = nums.count(majority_ele)
        numLength = len(nums)
        l_count, r_count = 0, count
        for j in range(0, len(nums)-1):
            if nums[j] == majority_ele:
                l_count += 1
                r_count -= 1
            if (l_count/(j+1)) > 0.5 and (r_count/(numLength - j - 1)) > 0.5:
                return j
        return -1 