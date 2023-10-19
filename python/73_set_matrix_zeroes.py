class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def zeroRow(row, start, end):
            for i in range(start, end):
                matrix[row][i] = 0
        
        def zeroCol(col, start, end):
            for i in range(start, end):
                matrix[i][col] = 0

        m = len(matrix)
        n = len(matrix[0])
        firstRow, firstCol = False, False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    firstRow, firstCol = firstRow or i == 0, firstCol or j == 0
                    matrix[0][j], matrix[i][0] = 0, 0

        for row in range(1, m):
            if matrix[row][0] == 0: zeroRow(row, 1, n)

        for col in range(1, n):
            if matrix[0][col] == 0: zeroCol(col, 1, m)
        
        if firstRow: zeroRow(0, 1, n)
        if firstCol: zeroCol(0, 1, m)