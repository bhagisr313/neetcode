# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1,numRows):
            temp = [0, *result[i-1], 0]
            arr = []
            for j in range(0,len(temp)-1):
                arr.append(temp[j]+temp[j+1])
            result.append(arr)
        return result