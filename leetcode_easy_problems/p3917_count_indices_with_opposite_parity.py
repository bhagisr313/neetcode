class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd_count = 0
        even_count = 0
        result = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] % 2 == 0:
                even_count += 1
                result.append(odd_count)
            else:
                odd_count += 1
                result.append(even_count)
        return result[::-1]
            