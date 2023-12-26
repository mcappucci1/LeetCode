class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    grid[r][c] = 2
                    closed = True
                    stack = [(r,c)]
                    while stack:
                        i, j = stack.pop()
                        for a, b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                            if not (0 <= a < m and 0 <= b < n):
                                closed = False
                            elif grid[a][b] == 0:
                                grid[a][b] = 2
                                stack.append((a,b))
                    if closed:
                        total += 1
        return total