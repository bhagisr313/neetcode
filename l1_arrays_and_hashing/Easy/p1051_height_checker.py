class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_array = []
        count = [0] * 101
        for h in heights:
            count[h] += 1
        for i in count:
            for _ in range(i):
                sorted_array.append(i)
        res = 0
        for i in range(0,len(heights)):
            if heights[i] != sorted_array[i]:
                res += 1
        return res
    

#brute force method 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_array = sorted(heights)
        res = 0
        for i in range(0,len(heights)):
            if heights[i] != sorted_array[i]:
                res += 1
        return res 