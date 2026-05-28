class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(0,len(grid)):
            for j in range(0,len(grid)):
                if (i == j or i + j == len(grid) - 1) and grid[i][j] == 0: 
                    return False
                elif(not (i==j or i+j == len(grid)-1)) and grid[i][j] !=0:
                    return False
        return True