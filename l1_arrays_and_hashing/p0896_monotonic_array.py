class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = False, False
        if len(nums) <= 2:
            return True
        for i in range(0,len(nums)-1):
            j = i+1
            if nums[j] - nums[i] > 0:
                inc = True
            elif nums[j] - nums[i] < 0:
                dec = True
        return not (inc and dec)
 