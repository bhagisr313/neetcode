class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        counter = 0
        maxCounter = 0
        for ele in my_set:
            if (ele-1) not in my_set:
                counter = 1
                first_num = ele
                while((first_num + 1) in my_set):
                    first_num += 1
                    counter += 1
                maxCounter = max(counter, maxCounter)
        return maxCounter