class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            row_set = set()
            column_set = set()
            for j in range(0,len(board)):
                if board[i][j] not in row_set:
                    if board[i][j] != ".":
                        row_set.add(board[i][j])
                else:
                    return False
                if board[j][i] not in column_set:
                    if board[j][i] != ".":
                        column_set.add(board[j][i])
                else:
                    return False
                
        for i in range(0,9,3):
            for j in range(0,9,3):
                box_set = set()
                for k in range(i,i+3,1):
                    for l in range(j,j+3,1):
                        if board[k][l] not in box_set:
                            if board[k][l] != ".":
                                box_set.add(board[k][l])
                        else:
                            return False
        return True