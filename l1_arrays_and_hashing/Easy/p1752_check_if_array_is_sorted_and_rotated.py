class Solution:
    def check(self, nums: List[int]) -> bool:
        counter = 0
        for i in range(-1,len(nums)-1):
            if nums[i+1] - nums[i] < 0:
                counter += 1
        return True if counter <= 1 else False