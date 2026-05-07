# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans
#can be solved as nums + nums as well