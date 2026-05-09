# 485. Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        counters = []
        for i in nums:
            if i == 1:
                counter += 1
            else:
                counters.append(counter)
                counter = 0
        counters.append(counter)
        return (max(counters))