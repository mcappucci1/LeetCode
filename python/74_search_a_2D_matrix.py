class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        row_lo, row_hi = 0, m-1
        while row_lo <= row_hi:
            row_m = (row_hi + row_lo) // 2
            if matrix[row_m][0] > target:
                row_hi = row_m - 1
            elif matrix[row_m][-1] < target:
                row_lo = row_m + 1
            else:
                lo, hi = 0, n - 1
                while lo <= hi:
                    m = (hi + lo) // 2
                    if matrix[row_m][m] > target:
                        hi = m - 1
                    elif matrix[row_m][m] < target:
                        lo = m + 1
                    else:
                        return True
                return False
        return False