# 3442. Maximum Difference Between Even and Odd Frequency I
class Solution:
    def maxDifference(self, s: str) -> int:
        my_dict = {}
        odd_max = 0
        even_min = float("inf")
        for i in s:
            my_dict[i] = my_dict.get(i,0) + 1
            
        for k,v in my_dict.items():
            if v > odd_max and v % 2 != 0:
                odd_max = v
            if v < even_min and v % 2 == 0:
                even_min = v
        return (odd_max - even_min)