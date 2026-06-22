class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = set()
        l = 0
        for r in range(0,len(nums)):
            if r - l > k:
                my_set.remove(nums[l])
                l += 1
            if nums[r] in my_set:
                return True
            my_set.add(nums[r])
        return False