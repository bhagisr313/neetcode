class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if i == j:
                    result += mat[i][j]
                elif i + j == len(mat) - 1:
                    result += mat[i][j]
        return result