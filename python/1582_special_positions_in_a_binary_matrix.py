class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])

        special_pos = 0
        special_cols = set()

        for c in range(n):
            total = 0
            for r in range(m):
                total += mat[r][c]
            if total == 1:
                special_cols.add(c)
        
        for r in range(m):
            total = 0
            i = -1
            for c in range(n):
                if mat[r][c] == 1:
                    total += 1
                    i = c
            if total == 1 and i in special_cols:
                special_pos += 1

        return special_pos