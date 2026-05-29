class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(0,len(matrix)):
            row_set = set()
            column_set = set()
            for j in range(0,len(matrix)):
                if matrix[i][j] not in row_set:
                    row_set.add(matrix[i][j])
                else:
                    return False
                if matrix[j][i] not in column_set:
                    column_set.add(matrix[j][i])
                else:
                    return False
        return True                