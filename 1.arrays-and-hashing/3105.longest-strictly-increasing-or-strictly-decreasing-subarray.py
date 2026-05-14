# 3105. Longest Strictly Increasing or Stricly Decreasing Subarray
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_count = 1
        decreasing_count = 1
        max_so_far = 1
        for i in range(0,len(nums)-1):
            j = i + 1
            if nums[i] < nums[j]:
                max_so_far = max(max_so_far,decreasing_count)
                decreasing_count = 1
                increasing_count += 1 
            elif nums[i] > nums[j]:
                max_so_far = max(max_so_far,increasing_count)
                increasing_count = 1
                decreasing_count +=1
            elif nums[i] == nums[j]:
                max_so_far = max(max_so_far, increasing_count, decreasing_count)
                increasing_count = 1
                decreasing_count = 1
        return max(max_so_far,increasing_count,decreasing_count)