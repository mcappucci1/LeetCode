class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        rows = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows.append(r)
        
        cols = []
        for c in range(n):
            for r in range(m):
                if grid[r][c] == 1:
                    cols.append(c)
        
        avg_r = rows[len(rows) // 2]
        avg_c = cols[len(cols) // 2]

        dist = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dist += abs(avg_r - r) + abs(avg_c - c)
        
        return dist