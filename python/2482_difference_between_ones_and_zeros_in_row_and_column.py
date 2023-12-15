class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for r in range(m):
            for c in range(n):
                rows[r] += grid[r][c]
                cols[c] += grid[r][c]
        for r in range(m):
            for c in range(n):
                grid[r][c] = 2 * rows[r] + 2 * cols[c] - n - m
        return grid