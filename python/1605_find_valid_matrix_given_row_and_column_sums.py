class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        m = len(rowSum)
        n = len(colSum)

        c = 0
        matrix = [[0] * n for i in range(m)]

        for r in range(m):
            while rowSum[r] > colSum[c]:
                rowSum[r] -= colSum[c]
                matrix[r][c] = colSum[c]
                c += 1
            matrix[r][c] = rowSum[r]
            colSum[c] -= rowSum[r]

        return matrix