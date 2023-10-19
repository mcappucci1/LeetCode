class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
                    
        m = len(grid)
        n = len(grid[0])
        best = 0
        counts = [[0] * n for i in range(m)]
        
        def update(grid, counts, row, col, count):
            if grid[row][col] == 'E':
                count += 1
            elif grid[row][col] == 'W':
                count = 0
            else:
                counts[row][col] += count
            return count
        
        # Count rows
        for row in range(m):
            left, right = 0, 0
            for col in range(n):
                left = update(grid, counts, row, col, left)
                right = update(grid, counts, row, n-col-1, right)
                best = max(best, counts[row][n-col-1], counts[row][col])
        
        # Count cols
        for col in range(n):
            left, right = 0, 0
            for row in range(m):
                left = update(grid, counts, row, col, left)
                right = update(grid, counts, m-row-1, col, right)
                best = max(best, counts[m-row-1][col], counts[row][col])
        
        return best