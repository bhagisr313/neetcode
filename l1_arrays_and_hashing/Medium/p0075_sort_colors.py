class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r, k = 0, len(nums)-1, 0
        while(k <= r):
            if nums[k] == 0:
                nums[k], nums[l] = nums[l], nums[k]
                l+= 1
            if nums[k] == 2:
                nums[k], nums[r] = nums[r], nums[k]
                r-=1 
                k-=1               
            k+=1