class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        result = []

        r_lo, r_hi = 0, m-1
        c_lo, c_hi = 0, n-1

        while r_lo <= r_hi and c_lo <= c_hi:
            # Add top row
            for c in range(c_lo, c_hi+1):
                result.append(matrix[r_lo][c])
            r_lo += 1
            
            # Add last column
            for r in range(r_lo, r_hi+1):
                result.append(matrix[r][c_hi])
            c_hi -= 1

            # Add bottom row
            if r_lo <= r_hi:
                for c in range(c_hi, c_lo-1, -1):
                    result.append(matrix[r_hi][c])
                r_hi -= 1

            # Add first column
            if c_lo <= c_hi:
                for r in range(r_hi, r_lo-1, -1):
                    result.append(matrix[r][c_lo])
                c_lo += 1
        
        return result