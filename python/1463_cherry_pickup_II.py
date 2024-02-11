class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        last = [[0] * n for i in range(n)]

        for r in range(m-1, -1, -1):
            dp = [[0] * n for i in range(n)]
            for c1 in range(min(n, m)):
                for c2 in range(n-1, max(-1, n-m-1), -1):
                    total = (grid[r][c1] + grid[r][c2]) if c1 != c2 else grid[r][c1]
                    for a in range(max(0, c1-1), min(c1+2, n)):
                        for b in range(max(0, c2-1), min(c2+2, n)):
                            dp[c1][c2] = max(dp[c1][c2], total + last[a][b])
            last = dp

        return last[0][n-1]