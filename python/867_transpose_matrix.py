class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]