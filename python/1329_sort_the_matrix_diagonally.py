class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        def sortDiagonal(r, c):
            counts = [0] * 100
            for i in range(min(m - r, n - c)):
                counts[mat[r+i][c+i] - 1] += 1
            x = 0
            for i in range(min(m - r, n - c)):
                while counts[x] == 0:
                    x += 1
                mat[r+i][c+i] = x+1
                counts[x] -= 1

        
        for i in range(n):
            sortDiagonal(0, i)
        
        for i in range(1, m):
            sortDiagonal(i, 0)

        return mat