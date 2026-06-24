class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l = 0
        r = k - 1
        sorted_nums = sorted(nums)
        min_diff = float("inf")
        if k == 1:
            return 0
        while( r < len(sorted_nums)):
            min_diff = min(sorted_nums[r] - sorted_nums[l],min_diff)
            l+=1
            r+=1
        return min_diff