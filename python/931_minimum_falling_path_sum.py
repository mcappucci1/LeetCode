class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        for row in range(n-2, -1, -1):
            for col in range(n):
                min_move = matrix[row+1][col]
                if col > 0:
                    min_move = min(min_move, matrix[row+1][col-1])
                if col < n-1:
                    min_move = min(min_move, matrix[row+1][col+1])
                matrix[row][col] += min_move
        
        return min(matrix[0])