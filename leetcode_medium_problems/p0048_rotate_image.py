class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0,len(matrix)//2):
            for j in range(0,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][j]
                matrix[n-1-i][j] = temp
        for k in range(1,n):
            for l in range(0,k):
                temp = matrix[k][l]
                matrix[k][l] = matrix[l][k]
                matrix[l][k] = temp
        print(matrix)