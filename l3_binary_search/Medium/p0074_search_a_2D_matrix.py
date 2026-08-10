class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        v_low, v_mid, v_high = 0, 0, len(matrix)-1
        v_lowbound = 0
        while(v_low <= v_high):
            v_mid = (v_low + v_high)//2
            if target < matrix[v_mid][0]:
                v_high = v_mid - 1
            elif target > matrix[v_mid][0]:
                v_low = v_mid + 1
                v_lowbound = v_mid
            else:
                return True
            
        h_low, h_mid, h_high = 0, 0, len(matrix[v_lowbound])-1
        while(h_low <= h_high):
            h_mid = (h_low + h_high)//2
            if target < matrix[v_lowbound][h_mid]:
                h_high = h_mid - 1
            elif target > matrix[v_lowbound][h_mid]:
                h_low = h_mid + 1
            else:
                return True
        return False

# ============================================================
# RELATED EASY PROBLEM
# ============================================================
# Binary Search
#
# Review this Easy problem first if you need to revisit
# the basic pattern behind this Medium problem.
# ============================================================
