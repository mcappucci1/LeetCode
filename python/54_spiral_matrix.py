class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        result = []
        r_t, r_b, c_l, c_r = 0, m-1, 0, n-1

        while (r_t <= r_b) and (c_l <= c_r):
            # top row
            for c in range(c_l, c_r+1):
                result.append(matrix[r_t][c])
            r_t += 1

            if r_t > r_b:
                break

            # right column
            for r in range(r_t, r_b+1):
                result.append(matrix[r][c_r])
            c_r -= 1

            if c_r < c_l:
                break

            # bottom row
            for c in range(c_r, c_l-1, -1):
                result.append(matrix[r_b][c])
            r_b -= 1

            # left column
            for r in range(r_b, r_t-1, -1):
                result.append(matrix[r][c_l])
            c_l += 1


        return result